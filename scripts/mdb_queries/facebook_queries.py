queries = [
# Q1
'MATCH (N0)=[ANY :A*]=>(?x) RETURN ?x LIMIT 100000',

# Q2, k = 1
'MATCH (N0)=[ANY ?p :A{0,1}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,1}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,1}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,1}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,1}]=>(?x) RETURN ?x,?p',

# Q2, k = 2
'MATCH (N0)=[ANY ?p :A{0,2}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,2}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,2}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,2}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,2}]=>(?x) RETURN ?x,?p',

# Q2, k = 3
'MATCH (N0)=[ANY ?p :A{0,3}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,3}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,3}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,3}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,3}]=>(?x) RETURN ?x,?p',

# Q2, k = 4
'MATCH (N0)=[ANY ?p :A{0,4}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,4}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,4}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,4}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,4}]=>(?x) RETURN ?x,?p',

# Q2, k = 5
'MATCH (N0)=[ANY ?p :A{0,5}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,5}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,5}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,5}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,5}]=>(?x) RETURN ?x,?p',

# Q2, k = 6
'MATCH (N0)=[ANY ?p :A{0,6}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,6}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,6}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,6}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,6}]=>(?x) RETURN ?x,?p',

# Q2, k = 7
'MATCH (N0)=[ANY ?p :A{0,7}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,7}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,7}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,7}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,7}]=>(?x) RETURN ?x,?p',

# Q2, k = 8
'MATCH (N0)=[ANY ?p :A{0,8}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,8}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,8}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,8}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,8}]=>(?x) RETURN ?x,?p',

# Q2, k = 9
'MATCH (N0)=[ANY ?p :A{0,9}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,9}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,9}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,9}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,9}]=>(?x) RETURN ?x,?p',

# Q2, k = 10
'MATCH (N0)=[ANY ?p :A{0,10}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,10}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,10}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,10}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,10}]=>(?x) RETURN ?x,?p',

# Q3, k = 1
'MATCH (N0)=[ANY ?p :A{1,1}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{1,1}]=>(?x) RETURN ?x LIMIT 100000',

# Q3, k = 2
'MATCH (N0)=[ANY ?p :A{2,2}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{2,2}]=>(?x) RETURN ?x LIMIT 100000',

# Q3, k = 3
'MATCH (N0)=[ANY ?p :A{3,3}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{3,3}]=>(?x) RETURN ?x LIMIT 100000',

# Q3, k = 4
'MATCH (N0)=[ANY ?p :A{4,4}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{4,4}]=>(?x) RETURN ?x LIMIT 100000',

# Q3, k = 5
'MATCH (N0)=[ANY ?p :A{5,5}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{5,5}]=>(?x) RETURN ?x LIMIT 100000',

# Q3, k = 6
'MATCH (N0)=[ANY ?p :A{6,6}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{6,6}]=>(?x) RETURN ?x LIMIT 100000',

# Q3, k = 7
'MATCH (N0)=[ANY ?p :A{7,7}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{7,7}]=>(?x) RETURN ?x LIMIT 100000',

# Q3, k = 8
'MATCH (N0)=[ANY ?p :A{8,8}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{8,8}]=>(?x) RETURN ?x LIMIT 100000',

# Q3, k = 9
'MATCH (N0)=[ANY ?p :A{9,9}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{9,9}]=>(?x) RETURN ?x LIMIT 100000',

# Q3, k = 10
'MATCH (N0)=[ANY ?p :A{10,10}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{10,10}]=>(?x) RETURN ?x LIMIT 100000',

# Q4, k = 1
'MATCH (N0)=[ANY ?p :A{1,1}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{1,1}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{1,1}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{1,1}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{1,1}]=>(?x) RETURN ?x,?p',

# Q4, k = 2
'MATCH (N0)=[ANY ?p :A{2,2}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{2,2}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{2,2}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{2,2}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{2,2}]=>(?x) RETURN ?x,?p',

# Q4, k = 3
'MATCH (N0)=[ANY ?p :A{3,3}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{3,3}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{3,3}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{3,3}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{3,3}]=>(?x) RETURN ?x,?p',

# Q4, k = 4
'MATCH (N0)=[ANY ?p :A{4,4}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{4,4}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{4,4}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{4,4}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{4,4}]=>(?x) RETURN ?x,?p',

# Q4, k = 5
'MATCH (N0)=[ANY ?p :A{5,5}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{5,5}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{5,5}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{5,5}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{5,5}]=>(?x) RETURN ?x,?p',

# Q4, k = 6
'MATCH (N0)=[ANY ?p :A{6,6}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{6,6}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{6,6}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{6,6}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{6,6}]=>(?x) RETURN ?x,?p',

# Q4, k = 7
'MATCH (N0)=[ANY ?p :A{7,7}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{7,7}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{7,7}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{7,7}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{7,7}]=>(?x) RETURN ?x,?p',

# Q4, k = 8
'MATCH (N0)=[ANY ?p :A{8,8}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{8,8}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{8,8}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{8,8}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{8,8}]=>(?x) RETURN ?x,?p',

# Q4, k = 9
'MATCH (N0)=[ANY ?p :A{9,9}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{9,9}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{9,9}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{9,9}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{9,9}]=>(?x) RETURN ?x,?p',

# Q4, k = 10
'MATCH (N0)=[ANY ?p :A{10,10}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{10,10}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{10,10}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{10,10}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{10,10}]=>(?x) RETURN ?x,?p',

# Q5
'MATCH (N0)=[ANY ?p :A{1,1}]=>(?x) RETURN ?x,?p LIMIT 1',
'MATCH (N0)=[ANY ?p :A{2,2}]=>(?x) RETURN ?x,?p LIMIT 1',
'MATCH (N0)=[ANY ?p :A{3,3}]=>(?x) RETURN ?x,?p LIMIT 1',
'MATCH (N0)=[ANY ?p :A{4,4}]=>(?x) RETURN ?x,?p LIMIT 1',
'MATCH (N0)=[ANY ?p :A{5,5}]=>(?x) RETURN ?x,?p LIMIT 1',
'MATCH (N0)=[ANY ?p :A{6,6}]=>(?x) RETURN ?x,?p LIMIT 1',
'MATCH (N0)=[ANY ?p :A{7,7}]=>(?x) RETURN ?x,?p LIMIT 1',
'MATCH (N0)=[ANY ?p :A{8,8}]=>(?x) RETURN ?x,?p LIMIT 1',
'MATCH (N0)=[ANY ?p :A{9,9}]=>(?x) RETURN ?x,?p LIMIT 1',
'MATCH (N0)=[ANY ?p :A{10,10}]=>(?x) RETURN ?x,?p LIMIT 1',
]
