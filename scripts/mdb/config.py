import os

# Port that the server will listen on
PORT = 8080

# Maximum time in seconds that the server will wait for a query
TIMEOUT = 60

# Assume that the script is run from the root directory
MDB_DIR = '/data2/benchmark/AllShortestPathsBenchmark/MillenniumDB-Dev'
DBS_FOLDER = os.path.join(MDB_DIR, "tests/dbs")
EXECUTABLES_DIR   = os.path.join(MDB_DIR, "build/Release/bin")
SERVER_EXECUTABLE = os.path.join(EXECUTABLES_DIR, "server")
QUERY_EXECUTABLE  = os.path.join(EXECUTABLES_DIR, "query")

RESULTS_TMP = 'result.tmp'
QUERY_TMP = 'query.tmp'
