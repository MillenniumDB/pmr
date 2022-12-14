import os

import mdb.benchmark as mdb_benchmark
import mdb_queries.facebook_queries as facebook_queries

if __name__ == "__main__":
    mdb_benchmark.run_benchmark(
        'facebook',
        'MDB_FACEBOOK_RESULTS.tsv',
        facebook_queries.queries
    )
