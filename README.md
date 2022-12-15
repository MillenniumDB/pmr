# Replicating the experiments

- Clone this repo
- Enter to this project root directory
    - `cd pmr`

- Set PMR_HOME with the path of this project root directory
    - `export PMR_HOME=$(pwd)`

## MillenniumDB
These instructions works on Ubuntu 20.04. Other linux distros might need to install dependencies differently. Libboost version used is 1.71.0, with other versions MillenniumDB might not compile.

- Install MillenniumDB dependencies.
    - `sudo apt update`
    - `sudo apt install g++ cmake libboost-all-dev`

- Change directory to the MillenniumDB folder
    - `cd MillenniumDB`

- Compile MillenniumDB:
    - `cmake -Bbuild/Release -DCMAKE_BUILD_TYPE=Release && cmake --build build/Release/`

- Create Diamond1000 database:
    - `build/Release/bin/create_db ../data/diamond_1000.mdb dbs/diamond_1000`

- Create Facebook database
    - `build/Release/bin/create_db ../data/facebook.mdb dbs/facebook`

- Go back to this project root directory
    - `cd ..`

- Run diamond1000 benchmark:
    - `python3 scripts/benchmark_mdb_diamond.py`
- Run facebook benchmark:
    - `python3 scripts/benchmark_mdb_facebook.py`


## Neo4J
- Install Neo4J python driver
    - `pip3 install neo4j`

- Download and extract the neo4j linux executable: https://neo4j.com/download-center/#community

- Set NEO4J_HOME with the path of the folder extracted
    - `export NEO4J_HOME=/path/to/neo4j/folder`

- Change directory to that folder:
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
- Run the benchmar with facebook graph:
    - Start the neo4j server
        - `bin/neo4j console`

    - Wait until the server is ready and run the benchmark in another terminal:
        - `python3 scripts/benchmark_neo4j_facebook.py`

    - After the benchmark is finished, kill the neo4j server with CTRL-C.

- Run the benchmar with facebook graph:
    - Edit `conf/neo4j.conf` and replace `dbms.default_database=facebook` with `dbms.default_database=diamond1000`

    - Start the neo4j server
        - `bin/neo4j console`
    - Wait until the server is ready and run the benchmark in another terminal:
        - `python3 scripts/benchmark_neo4j_diamond.py`

    - After the benchmark is finished, kill the neo4j server with CTRL-C.
