queries = [
'MATCH ({id:"0"})-[*]->(x) RETURN DISTINCT x LIMIT 100000;',

# Q1
'MATCH ({id:"0"})-[:A*0..]->(x) RETURN x LIMIT 100000;',
'MATCH p=shortestPath( ({id:"0"})-[:A*0..]->(x) ) RETURN x LIMIT 100000;',

# Q2, k = 1
'MATCH p=shortestPath( ({id:"0"})-[:A*0..1]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..1]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..1]->(x) ) RETURN COUNT(p);',

# Q2, k = 2
'MATCH p=shortestPath( ({id:"0"})-[:A*0..2]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..2]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..2]->(x) ) RETURN COUNT(p);',

# Q2, k = 3
'MATCH p=shortestPath( ({id:"0"})-[:A*0..3]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..3]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..3]->(x) ) RETURN COUNT(p);',

# Q2, k = 4
'MATCH p=shortestPath( ({id:"0"})-[:A*0..4]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..4]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..4]->(x) ) RETURN COUNT(p);',

# Q2, k = 5
'MATCH p=shortestPath( ({id:"0"})-[:A*0..5]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..5]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..5]->(x) ) RETURN COUNT(p);',

# Q2, k = 6
'MATCH p=shortestPath( ({id:"0"})-[:A*0..6]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..6]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..6]->(x) ) RETURN COUNT(p);',

# Q2, k = 7
'MATCH p=shortestPath( ({id:"0"})-[:A*0..7]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..7]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..7]->(x) ) RETURN COUNT(p);',

# Q2, k = 8
'MATCH p=shortestPath( ({id:"0"})-[:A*0..8]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..8]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..8]->(x) ) RETURN COUNT(p);',

# Q2, k = 9
'MATCH p=shortestPath( ({id:"0"})-[:A*0..9]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..9]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..9]->(x) ) RETURN COUNT(p);',

# Q2, k = 10
'MATCH p=shortestPath( ({id:"0"})-[:A*0..10]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..10]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"0"})-[:A*0..10]->(x) ) RETURN COUNT(p);',


# Q3, k = 1
'MATCH ({id:"0"})-[:A*1..1]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1) RETURN x1 LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1) RETURN x1 LIMIT 100000;',

# Q3, k = 2
'MATCH ({id:"0"})-[:A*2..2]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"0"})\
-[:A]->(x1)\
-[:A]->(x2) RETURN x2 LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x19)-[:A]->(x2) RETURN x2 LIMIT 100000;',

# Q3, k = 3
'MATCH ({id:"0"})-[:A*3..3]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"0"})\
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3) RETURN x3 LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3) RETURN x3 LIMIT 100000;',

# Q3, k = 4
'MATCH ({id:"0"})-[:A*4..4]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"0"})\
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4) RETURN x4 LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4) RETURN x4 LIMIT 100000;',

# Q3, k = 5
'MATCH ({id:"0"})-[:A*5..5]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"0"})\
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
-[:A]->(x5) RETURN x5 LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5) RETURN x5 LIMIT 100000;',

# Q3, k = 6
'MATCH ({id:"0"})-[:A*6..6]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"0"})\
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
-[:A]->(x5)\
-[:A]->(x6) RETURN x6 LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6) RETURN x6 LIMIT 100000;',

# Q3, k = 7
'MATCH ({id:"0"})-[:A*7..7]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"0"})\
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
-[:A]->(x5)\
-[:A]->(x6)\
-[:A]->(x7) RETURN x7 LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7) RETURN x7 LIMIT 100000;',

 # Q3, k = 8
'MATCH ({id:"0"})-[:A*8..8]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"0"})\
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
-[:A]->(x5)\
-[:A]->(x6)\
-[:A]->(x7)\
-[:A]->(x8) RETURN x8 LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)  RETURN x8 LIMIT 100000;',

 # Q3, k = 9
'MATCH ({id:"0"})-[:A*9..9]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"0"})\
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
-[:A]->(x5)\
-[:A]->(x6)\
-[:A]->(x7)\
-[:A]->(x8)\
-[:A]->(x9) RETURN x9 LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9) RETURN x9 LIMIT 100000;',


 # Q3, k = 10
'MATCH ({id:"0"})-[:A*10..10]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"0"})\
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
-[:A]->(x5)\
-[:A]->(x6)\
-[:A]->(x7)\
-[:A]->(x8)\
-[:A]->(x9)\
-[:A]->(x10) RETURN x10 LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10) RETURN x10 LIMIT 100000;', 

# Q4 k = 1
'MATCH p=shortestPath( ({id:"0"})-[:A*1..1]->(x) ) WHERE length(p)=1 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"0"})-[:A]->(x1) ) RETURN x1,p LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1) RETURN * LIMIT 100000;',
'MATCH p=( ({id:"0"})-[:A]->(x1)) RETURN COUNT(p);',
'MATCH ({id:"0"})-[:A]->(x1) RETURN COUNT(*);',

# Q4 k = 2
'MATCH p=shortestPath( ({id:"0"})-[:A*1..2]->(x) ) WHERE length(p)=2 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"0"}) \
-[:A]->(x1)\
-[:A]->(x2)\
) RETURN x2,p LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 RETURN * LIMIT 100000;',
'MATCH p=( ({id:"0"}) \
-[:A]->(x1)\
-[:A]->(x2)\
) RETURN COUNT(p);',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 RETURN COUNT(*);',

# Q4 k = 3
'MATCH p=shortestPath( ({id:"0"})-[:A*1..3]->(x) ) WHERE length(p)=3 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"0"}) \
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
) RETURN x3,p LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 RETURN * LIMIT 100000;',
'MATCH p=( ({id:"0"}) \
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
) RETURN COUNT(*);',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 RETURN COUNT(*);',

# Q4 k = 4
'MATCH p=shortestPath( ({id:"0"})-[:A*1..4]->(x) ) WHERE length(p)=4 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"0"}) \
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
) RETURN x4,p LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 RETURN * LIMIT 100000;',
'MATCH p=( ({id:"0"}) \
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
) RETURN COUNT(p);',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 RETURN COUNT(*);',

# Q4 k = 5
'MATCH p=shortestPath( ({id:"0"})-[:A*1..5]->(x) ) WHERE length(p)=5 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"0"}) \
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
-[:A]->(x5)\
) RETURN x5,p LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 RETURN * LIMIT 100000;',
'MATCH p=( ({id:"0"}) \
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
-[:A]->(x5)\
) RETURN COUNT(p);',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 RETURN COUNT(*);',

# Q4 k = 6
'MATCH p=shortestPath( ({id:"0"})-[:A*1..6]->(x) ) WHERE length(p)=6 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"0"}) \
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
-[:A]->(x5)\
-[:A]->(x6)\
) RETURN x6,p LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 RETURN * LIMIT 100000;',
'MATCH p=( ({id:"0"}) \
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
-[:A]->(x5)\
-[:A]->(x6)\
) RETURN COUNT(p);',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 RETURN COUNT(*);',

# Q4 k = 7
'MATCH p=shortestPath( ({id:"0"})-[:A*1..7]->(x) ) WHERE length(p)=7 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"0"}) \
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
-[:A]->(x5)\
-[:A]->(x6)\
-[:A]->(x7)\
) RETURN x7,p LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 RETURN * LIMIT 100000;',
'MATCH p=( ({id:"0"}) \
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
-[:A]->(x5)\
-[:A]->(x6)\
-[:A]->(x7)\
) RETURN COUNT(p);',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 RETURN COUNT(*);',


# Q4 k = 8
'MATCH p=shortestPath( ({id:"0"})-[:A*1..8]->(x) ) WHERE length(p)=8 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"0"}) \
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
-[:A]->(x5)\
-[:A]->(x6)\
-[:A]->(x7)\
-[:A]->(x8)\
) RETURN x8,p LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 RETURN * LIMIT 100000;',
'MATCH p=( ({id:"0"}) \
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
-[:A]->(x5)\
-[:A]->(x6)\
-[:A]->(x7)\
-[:A]->(x8)\
) RETURN COUNT(p);',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 RETURN COUNT(*);',


# Q4 k = 9
'MATCH p=shortestPath( ({id:"0"})-[:A*1..9]->(x) ) WHERE length(p)=8 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"0"}) \
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
-[:A]->(x5)\
-[:A]->(x6)\
-[:A]->(x7)\
-[:A]->(x8)\
-[:A]->(x9)\
) RETURN x9,p LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 RETURN * LIMIT 100000;',
'MATCH p=( ({id:"0"}) \
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
-[:A]->(x5)\
-[:A]->(x6)\
-[:A]->(x7)\
-[:A]->(x8)\
-[:A]->(x9)\
) RETURN COUNT(p);',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 RETURN COUNT(*);',


# Q4 k = 10
'MATCH p=shortestPath( ({id:"0"})-[:A*1..10]->(x) ) WHERE length(p)=8 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"0"}) \
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
-[:A]->(x5)\
-[:A]->(x6)\
-[:A]->(x7)\
-[:A]->(x8)\
-[:A]->(x9)\
-[:A]->(x10)\
) RETURN x10,p LIMIT 100000;',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 RETURN * LIMIT 100000;',
'MATCH p=( ({id:"0"}) \
-[:A]->(x1)\
-[:A]->(x2)\
-[:A]->(x3)\
-[:A]->(x4)\
-[:A]->(x5)\
-[:A]->(x6)\
-[:A]->(x7)\
-[:A]->(x8)\
-[:A]->(x9)\
-[:A]->(x10)\
) RETURN COUNT(p);',
'MATCH ({id:"0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 RETURN COUNT(*);',

# limit 1
'MATCH ({id:"0"})-[:A]->(x1) RETURN * LIMIT 1;',
'MATCH ({id:"0"})-[:A]->(x1) MATCH (x1)-[:A]->(x2) RETURN * LIMIT 1;',
'MATCH ({id:"0"})-[:A]->(x1) MATCH (x1)-[:A]->(x2) MATCH (x2)-[:A]->(x3) RETURN * LIMIT 1;',
'MATCH ({id:"0"})-[:A]->(x1) MATCH (x1)-[:A]->(x2) MATCH (x2)-[:A]->(x3) MATCH (x3)-[:A]->(x4) RETURN * LIMIT 1;',
'MATCH ({id:"0"})-[:A]->(x1) MATCH (x1)-[:A]->(x2) MATCH (x2)-[:A]->(x3) MATCH (x3)-[:A]->(x4) MATCH (x4)-[:A]->(x5) RETURN * LIMIT 1;',
'MATCH ({id:"0"})-[:A]->(x1) MATCH (x1)-[:A]->(x2) MATCH (x2)-[:A]->(x3) MATCH (x3)-[:A]->(x4) MATCH (x4)-[:A]->(x5) MATCH (x5)-[:A]->(x6) RETURN * LIMIT 1;',
'MATCH ({id:"0"})-[:A]->(x1) MATCH (x1)-[:A]->(x2) MATCH (x2)-[:A]->(x3) MATCH (x3)-[:A]->(x4) MATCH (x4)-[:A]->(x5) MATCH (x5)-[:A]->(x6) MATCH (x6)-[:A]->(x7) RETURN * LIMIT 1;',
'MATCH ({id:"0"})-[:A]->(x1) MATCH (x1)-[:A]->(x2) MATCH (x2)-[:A]->(x3) MATCH (x3)-[:A]->(x4) MATCH (x4)-[:A]->(x5) MATCH (x5)-[:A]->(x6) MATCH (x6)-[:A]->(x7) MATCH (x7)-[:A]->(x8) RETURN * LIMIT 1;',
'MATCH ({id:"0"})-[:A]->(x1) MATCH (x1)-[:A]->(x2) MATCH (x2)-[:A]->(x3) MATCH (x3)-[:A]->(x4) MATCH (x4)-[:A]->(x5) MATCH (x5)-[:A]->(x6) MATCH (x6)-[:A]->(x7) MATCH (x7)-[:A]->(x8) MATCH (x8)-[:A]->(x9) RETURN * LIMIT 1;',
'MATCH ({id:"0"})-[:A]->(x1) MATCH (x1)-[:A]->(x2) MATCH (x2)-[:A]->(x3) MATCH (x3)-[:A]->(x4) MATCH (x4)-[:A]->(x5) MATCH (x5)-[:A]->(x6) MATCH (x6)-[:A]->(x7) MATCH (x7)-[:A]->(x8) MATCH (x8)-[:A]->(x9) MATCH (x9)-[:A]->(x10) RETURN * LIMIT 1;',
]