import os

import mdb.benchmark as mdb_benchmark
import mdb_queries.diamond_queries as diamond_queries

if __name__ == "__main__":
    mdb_benchmark.run_benchmark(
        'diamond_1000',
        'MDB_DIAMOND1000_RESULTS.tsv',
        diamond_queries.queries
    )
