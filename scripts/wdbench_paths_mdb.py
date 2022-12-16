from SPARQLWrapper import SPARQLWrapper, JSON
import os
import re
import sys
import socket
import subprocess
import time
import traceback

if len(sys.argv) < 3:
    print('usage:')
    print('python3 scripts/wdbench_paths_mdb.py <QUERIES_FILE_PATH> <PATH_SEMANTIC>')
    exit(1)

QUERIES_FILE = sys.argv[1]
PATH_SEMANTIC = sys.argv[2].upper()

if PATH_SEMANTIC == 'ENDPOINTS':
    MDB_PATH_SEMANTIC = 'ANY'
    RETURN_PATH = False
elif PATH_SEMANTIC == 'SINGLE_SHORTEST':
    MDB_PATH_SEMANTIC = 'ANY'
    RETURN_PATH = True
elif PATH_SEMANTIC == 'ALL_SHORTEST':
    MDB_PATH_SEMANTIC = 'ALL'
    RETURN_PATH = True
elif PATH_SEMANTIC == 'COUNT':
    MDB_PATH_SEMANTIC = 'ALL_COUNT'
    RETURN_PATH = True
elif PATH_SEMANTIC == 'CONSTRUCT_PMR':
    MDB_PATH_SEMANTIC = 'ALL_FILL_VISITED'
    RETURN_PATH = False
else:
    print(f"path semantic '{PATH_SEMANTIC}' not recognized. Supported are: 'endpoints', 'single_shortest', 'all_shortest', 'count', 'construct_pmr'.")
    exit(1)

############################ EDIT THIS PARAMETERS #############################
LIMIT = 100000
TIMEOUT = 60 # Max time per query in seconds

BENCHMARK_ROOT = '/data2/benchmark/AllShortestPathsBenchmark/'

# MILLENNIUM DB options
MDB_QUERY_FILE    = f'mdb_query_file.tmp'  # temp file to write the query
MDB_WIKIDATA_PATH = f'MillenniumDB/dbs/wikidata'
MDB_BUFFER_SIZE = 8388608 # Buffer used by MillenniumDB 8388608 == 32GB
                          # using 32GB instead of 64GB because
                          # this is only for the buffer manager and MillenniumDB
                          # needs more RAM for other things (e.g. ObjectFile)

# Prefer use absolute paths to avoid problems with current directory
PORT = 8080

QUERY_EXECUTABLE  = f'MillenniumDB/build/Release/bin/query'
SERVER_EXECUTABLE = f'MillenniumDB/build/Release/bin/server'

# Path to needed output and input files
MDB_RESULTS_FILE = f'mdb_results.tmp'
RESUME_FILE      = f'PATHS_MDB_{PATH_SEMANTIC}.csv'
ERROR_FILE       = f'WDBench/log/error_paths_MDB_{PATH_SEMANTIC}.log'
SERVER_LOG_FILE  = f'WDBench/log/server_paths_MDB_{PATH_SEMANTIC}.log'
######################## END OF EDITABLE PARAMETERS ###########################

# Does not return, it writes the query in MDB_QUERY_FILE
def parse_to_millenniumdb(query):
    query_parts   = query.strip().split(' ')
    from_string   = query_parts[0]
    property_path = " ".join(query_parts[1:len(query_parts) - 1])
    end_string    = query_parts[len(query_parts) - 1]

    var_count = 0
    vars = []

    if RETURN_PATH:
        vars.append('?p')

    # Parse subject
    if '?x' in from_string:
        var_count += 1
        vars.append(f'?x{var_count}')
        from_string = f'(?x{var_count})=[{MDB_PATH_SEMANTIC} ?p '
    else:
        from_string = '(' + from_string.split('/')[-1].replace('>', '') + f')=[{MDB_PATH_SEMANTIC} ?p '

    # Parse object
    if '?x' in end_string:
        var_count += 1
        vars.append(f'?x{var_count}')
        end_string  = f']=>(?x{var_count})'
    else:
        end_string  = ']=>(' + end_string.split('/')[-1].replace('>', '') + ')'

    # Parse property path
    pattern = r"\<[a-zA-Z0-9\/\.\:\#]*\>"
    path_edges = re.findall(pattern, property_path)
    clean_property_path = property_path

    for path in path_edges:
        clean_path          = ':' + path.split('/')[-1].replace('>', '')
        clean_property_path = re.sub(path, clean_path, clean_property_path, flags=re.MULTILINE)

    with open(MDB_QUERY_FILE, 'w') as file:
        print(f'MATCH {from_string}{clean_property_path}{end_string} RETURN { ",".join(vars) } LIMIT {LIMIT}')
        file.write(f'MATCH {from_string}{clean_property_path}{end_string} RETURN { ",".join(vars) }')
        if LIMIT != 0:
            file.write(f' LIMIT {LIMIT}')


def start_server(db_dir):
    print("starting server...")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    location = ("127.0.0.1", PORT)

    # Check if port is already in use
    if s.connect_ex(location) == 0:
        print(f"Port {PORT} is already in use")
        sys.exit(1)

    server_process = subprocess.Popen(
        [SERVER_EXECUTABLE, db_dir, "--timeout", str(TIMEOUT), "--port", str(PORT)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # Wait for server initialization
    while s.connect_ex(location) != 0:
        time.sleep(1)

    print(f"server started[pid={server_process.pid}]")
    return server_process


def kill_server(server_process):
    print(f"killing server[pid={server_process.pid}]...")
    server_process.kill()
    server_process.wait()
    print(f"server killed")


def execute_queries():
    with open(QUERIES_FILE) as queries_file:
        for line in queries_file:
            query_number, query = line.split(',')
            print(f'Executing query {query_number}')
            query_millennium(query, query_number)


def query_millennium(query, query_number):
    parse_to_millenniumdb(query)
    start_time = time.time()
    with open(MDB_RESULTS_FILE, 'w') as results_file, open(MDB_QUERY_FILE, 'r') as query_file:
        query_execution = subprocess.Popen(
            [QUERY_EXECUTABLE],
            stdin=query_file,
            stdout=results_file,
            stderr=subprocess.DEVNULL)
    exit_code = query_execution.wait()
    elapsed_time = int((time.time() - start_time) * 1000)
    p = subprocess.Popen(['wc', '-l', MDB_RESULTS_FILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result, _ = p.communicate()
    results_count = int(result.strip().split()[0]) - 6 # 1 line from header + 2 for separators + 3 for stats

    mem_cmd = f'grep ^VmRSS /proc/{server_process.pid}/status'.split(' ')
    process = subprocess.Popen(mem_cmd, universal_newlines=True, stdout=subprocess.PIPE)
    out_cmd, err_cmd = process.communicate()
    out_cmd = out_cmd.strip().split()[1]

    with open(RESUME_FILE, 'a') as file:
        if exit_code == 0:
            file.write(f'{query_number},{results_count},OK,{elapsed_time},{out_cmd}\n')
        else:
            if elapsed_time >= TIMEOUT:
                file.write(f'{query_number},{results_count},TIMEOUT,{elapsed_time},{out_cmd}\n')
            else:
                file.write(f'{query_number},0,ERROR,{elapsed_time},{out_cmd}\n')


def check_port_available():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    location = ("127.0.0.1", PORT)
    # Check if port is already in use
    if s.connect_ex(location) == 0:
        raise Exception("server port already in use")


########################## BEGIN BENCHMARK EXECUTION ##########################
if __name__ == "__main__":
    server_log = open(SERVER_LOG_FILE, 'w')

    check_port_available()

    # Check if output file already exists
    if os.path.exists(RESUME_FILE):
        print(f'File {RESUME_FILE} already exists.')
        sys.exit()

    with open(RESUME_FILE, 'w') as file:
        file.write('query_number,results,status,time,max_mem[kB]\n')

    with open(ERROR_FILE, 'w') as file:
        file.write('') # to replaces the old error file

    print('TIMEOUT', TIMEOUT, 'seconds')
    server_process = start_server(MDB_WIKIDATA_PATH)
    execute_queries()

    # Delete temp file
    subprocess.Popen(['rm', MDB_RESULTS_FILE], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.Popen(['rm', MDB_QUERY_FILE], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if server_process is not None:
        kill_server(server_process)

    server_log.close()
