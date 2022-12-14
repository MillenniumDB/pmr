import socket
import subprocess
import sys
import time

import mdb.config as conf

def server_start(db_dir):
    print("starting server...")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    location = ("127.0.0.1", conf.PORT)

    # Check if port is already in use
    if s.connect_ex(location) == 0:
        print(f"Port {conf.PORT} is already in use")
        sys.exit(1)

    server_process = subprocess.Popen(
        [conf.SERVER_EXECUTABLE, db_dir, "--timeout", str(conf.TIMEOUT), "--port", str(conf.PORT)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # Wait for server initialization
    while s.connect_ex(location) != 0:
        time.sleep(1)

    print(f"server started[pid={server_process.pid}]")
    return server_process


def server_kill(server_process):
    print(f"killing server[pid={server_process.pid}]...")
    server_process.kill()
    server_process.wait()
    print(f"server killed")


def execute_query(query, out, pid):
    if os.path.exists(conf.RESULTS_TMP):
        os.remove(conf.RESULTS_TMP)
    with open(conf.QUERY_TMP, "w") as query_file:
        query_file.write(query)

    start_time = time.time()
    with open(conf.RESULTS_TMP, "w") as results_file, \
         open(conf.QUERY_TMP, "r") as query_file:
        query_execution = subprocess.Popen(
            [conf.QUERY_EXECUTABLE],
            stdin=query_file,
            stdout=results_file,
            stderr=subprocess.DEVNULL,
        )
        exit_code = query_execution.wait()
        elapsed_time = int((time.time() - start_time) * 1000)

    p = subprocess.Popen(['wc', '-l', conf.RESULTS_TMP], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result, _ = p.communicate()
    results_count = int(result.strip().split()[0]) - 6 # 1 line from header + 2 for separators + 3 for stats

    mem_cmd = f'grep ^VmRSS /proc/{pid}/status'.split(' ')
    process = subprocess.Popen(mem_cmd, universal_newlines=True, stdout=subprocess.PIPE)
    out_cmd, err_cmd = process.communicate()
    out_cmd = out_cmd.strip().split()[1]

    if exit_code == 0:
        out.write(f'\'{query}\t{results_count}\tOK\t{elapsed_time}\t{out_cmd}\n')
    else:
        if elapsed_time >= conf.TIMEOUT:
            out.write(f'\'{query}\t{results_count}\tTIMEOUT\t{elapsed_time}\t{out_cmd}\n')
        else:
            out.write(f'\'{query}\t0\tERROR\t{elapsed_time}\t{out_cmd}\n')


def run_benchmark(db_name, output_filename, queries):
    with open(output_filename, 'w') as results_file:
        results_file.write('query\tresults\tstatus\ttime\tmax_mem[kB]\n')
        for query in queries:
            server_process = server_start(f'{conf.DBS_FOLDER}/{db_name}')
            print(query)
            execute_query(query, results_file, server_process.pid)
            server_kill(server_process)

    # Remove tmp files
    if os.path.exists(conf.RESULTS_TMP):
        os.remove(conf.RESULTS_TMP)
    if os.path.exists(conf.QUERY_TMP):
        os.remove(conf.QUERY_TMP)