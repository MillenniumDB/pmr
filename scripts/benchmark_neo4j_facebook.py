from neo4j import GraphDatabase
import time
import neo4j_queries.facebook_queries as facebook_queries

def execute_query(session, query, results_file):
    result_count = 0
    start_time = time.time()
    try:
        results = session.execute_read(lambda tx: tx.run(query).data())
        for _ in results:
            result_count += 1
        elapsed_time = int((time.time() - start_time) * 1000)
        results_file.write(f'\'{query}\t{result_count}\tOK\t{elapsed_time}\n')

    except Exception as e:
        elapsed_time = int((time.time() - start_time) * 1000)
        results_file.write(f'\'{query}\t{result_count}\tERROR({type(e).__name__})\t{elapsed_time}\n')
        print(e)

    results_file.flush()


if __name__ == "__main__":
    database_name = 'facebook'
    with open('NEO4J_FACEBOOK_RESULTS.tsv', 'w') as results_file:
        results_file.write('query\tresults\tstatus\ttime\n')
        driver = GraphDatabase.driver('bolt://127.0.0.1:7687')
        with driver.session(database=database_name) as session:
            for query in facebook_queries.queries:
                print(query)
                execute_query(session, query, results_file)
        driver.close()

