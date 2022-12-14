# Replicating the experiments

- Clone this repo
- `cd pmr`
- `export PMR_HOME=$(pwd)`

## MillenniumDB
- Install MillenniumDB dependencies:
`sudo apt update`
`sudo apt install git g++ cmake libboost-all-dev`

- `cd MillenniumDB`
- compile MDB: `cmake -Bbuild/Release -DCMAKE_BUILD_TYPE=Release && cmake --build build/Release/`
- Create Diamond1000 database: `build/Release/bin/create_db ../data/diamond_1000.mdb dbs/diamond_1000`
- Create Facebook database `build/Release/bin/create_db ../data/facebook.mdb dbs/facebook`

- `cd ..`

- Run diamond1000 benchmark:
    - `python3 scripts/benchmark_mdb_diamond.py`
- Run facebook benchmark:
    - `python3 scripts/benchmark_mdb_facebook.py`


## Neo4J
- `pip3 install neo4j`
- Download and extract the neo4j linux executable: https://neo4j.com/download-center/#community

- Set NEO4J_HOME (`export NEO4J_HOME=/path/to/neo4j/folder`)

- `cd $NEO4J_HOME`

- Create facebook database
    ```
    bin/neo4j-admin import --database facebook \
    --nodes $PMR_HOME/data/facebook_neo4j_nodes.csv \
    --relationships $PMR_HOME/data/facebook_neo4j_edges.csv
    ```

- Create diamond1000 database
    ```
    bin/neo4j-admin import --database diamond1000 \
    --nodes $PMR_HOME/data/diamond_1000_neo4j_nodes.csv \
    --relationships $PMR_HOME/data/diamond_1000_neo4j_edges.csv
    ```

- Edit `conf/neo4j.conf`
    ```
    dbms.transaction.timeout=1m
    dbms.default_database=facebook
    dbms.security.auth_enabled=false
    cypher.forbid_shortestpath_common_nodes=false
    ```

- `bin/neo4j console`
- wait until the server is ready and run the benchmark in another terminal: `python3 scripts/benchmark_neo4j_facebook.py`

- Once the benchmark finish, interrupt the neo4j server with CTRL-C.

- Edit `conf/neo4j.conf` and replace `dbms.default_database=facebook` with `dbms.default_database=diamond1000`

- `bin/neo4j console`
- wait until the server is ready and run the benchmark in another terminal: `python3 scripts/benchmark_neo4j_diamond.py`
