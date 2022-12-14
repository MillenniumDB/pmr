queries = [
# Q1
'MATCH (N0)=[ANY :A*]=>(?x) RETURN ?x LIMIT 100000',

# Q2, k = 10
'MATCH (N0)=[ANY ?p :A{0,10}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,10}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,10}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,10}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,10}]=>(?x) RETURN ?x,?p',

# Q2, k = 20
'MATCH (N0)=[ANY ?p :A{0,20}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,20}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,20}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,20}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,20}]=>(?x) RETURN ?x,?p',

# Q2, k = 30
'MATCH (N0)=[ANY ?p :A{0,30}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,30}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,30}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,30}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,30}]=>(?x) RETURN ?x,?p',

# Q2, k = 40
'MATCH (N0)=[ANY ?p :A{0,40}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,40}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,40}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,40}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,40}]=>(?x) RETURN ?x,?p',

# Q2, k = 50
'MATCH (N0)=[ANY ?p :A{0,50}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,50}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,50}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,50}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,50}]=>(?x) RETURN ?x,?p',

# Q2, k = 60
'MATCH (N0)=[ANY ?p :A{0,60}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,60}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,60}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,60}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,60}]=>(?x) RETURN ?x,?p',

# Q2, k = 70
'MATCH (N0)=[ANY ?p :A{0,70}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,70}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,70}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,70}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,70}]=>(?x) RETURN ?x,?p',

# Q2, k = 80
'MATCH (N0)=[ANY ?p :A{0,80}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,80}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,80}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,80}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,80}]=>(?x) RETURN ?x,?p',

# Q2, k = 90
'MATCH (N0)=[ANY ?p :A{0,90}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,90}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,90}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,90}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,90}]=>(?x) RETURN ?x,?p',

# Q2, k = 100
'MATCH (N0)=[ANY ?p :A{0,100}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,100}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{0,100}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{0,100}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{0,100}]=>(?x) RETURN ?x,?p',

# Q3, k = 10
'MATCH (N0)=[ANY ?p :A{10,10}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{10,10}]=>(?x) RETURN ?x LIMIT 100000',

# Q3, k = 20
'MATCH (N0)=[ANY ?p :A{20,20}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{20,20}]=>(?x) RETURN ?x LIMIT 100000',

# Q3, k = 30
'MATCH (N0)=[ANY ?p :A{30,30}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{30,30}]=>(?x) RETURN ?x LIMIT 100000',

# Q3, k = 40
'MATCH (N0)=[ANY ?p :A{40,40}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{40,40}]=>(?x) RETURN ?x LIMIT 100000',

# Q3, k = 50
'MATCH (N0)=[ANY ?p :A{50,50}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{50,50}]=>(?x) RETURN ?x LIMIT 100000',

# Q3, k = 60
'MATCH (N0)=[ANY ?p :A{60,60}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{60,60}]=>(?x) RETURN ?x LIMIT 100000',

# Q3, k = 70
'MATCH (N0)=[ANY ?p :A{70,70}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{70,70}]=>(?x) RETURN ?x LIMIT 100000',

# Q3, k = 80
'MATCH (N0)=[ANY ?p :A{80,80}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{80,80}]=>(?x) RETURN ?x LIMIT 100000',

# Q3, k = 90
'MATCH (N0)=[ANY ?p :A{90,90}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{90,90}]=>(?x) RETURN ?x LIMIT 100000',

# Q3, k = 100
'MATCH (N0)=[ANY ?p :A{100,100}]=>(?x) RETURN ?x LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{100,100}]=>(?x) RETURN ?x LIMIT 100000',

# Q4, k = 10
'MATCH (N0)=[ANY ?p :A{10,10}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{10,10}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{10,10}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{10,10}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{10,10}]=>(?x) RETURN ?x,?p',

# Q4, k = 20
'MATCH (N0)=[ANY ?p :A{20,20}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{20,20}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{20,20}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{20,20}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{20,20}]=>(?x) RETURN ?x,?p',

# Q4, k = 30
'MATCH (N0)=[ANY ?p :A{30,30}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{30,30}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{30,30}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{30,30}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{30,30}]=>(?x) RETURN ?x,?p',

# Q4, k = 40
'MATCH (N0)=[ANY ?p :A{40,40}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{40,40}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{40,40}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{40,40}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{40,40}]=>(?x) RETURN ?x,?p',

# Q4, k = 50
'MATCH (N0)=[ANY ?p :A{50,50}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{50,50}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{50,50}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{50,50}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{50,50}]=>(?x) RETURN ?x,?p',

# Q4, k = 60
'MATCH (N0)=[ANY ?p :A{60,60}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{60,60}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{60,60}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{60,60}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{60,60}]=>(?x) RETURN ?x,?p',

# Q4, k = 70
'MATCH (N0)=[ANY ?p :A{70,70}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{70,70}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{70,70}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{70,70}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{70,70}]=>(?x) RETURN ?x,?p',

# Q4, k = 80
'MATCH (N0)=[ANY ?p :A{80,80}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{80,80}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{80,80}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{80,80}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{80,80}]=>(?x) RETURN ?x,?p',

# Q4, k = 90
'MATCH (N0)=[ANY ?p :A{90,90}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{90,90}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{90,90}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{90,90}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{90,90}]=>(?x) RETURN ?x,?p',

# Q4, k = 100
'MATCH (N0)=[ANY ?p :A{100,100}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{100,100}]=>(?x) RETURN ?x,?p LIMIT 100000',
'MATCH (N0)=[ALL ?p :A{100,100}]=>(?x) RETURN COUNT(*)',
'MATCH (N0)=[ALL_COUNT ?p :A{100,100}]=>(?x) RETURN ?x,?p',
'MATCH (N0)=[ALL_FILL_VISITED ?p :A{100,100}]=>(?x) RETURN ?x,?p',

# Q5
'MATCH (N0)=[ANY ?p :A{10,10}]=>(?x) RETURN ?x,?p LIMIT 1',
'MATCH (N0)=[ANY ?p :A{20,20}]=>(?x) RETURN ?x,?p LIMIT 1',
'MATCH (N0)=[ANY ?p :A{30,30}]=>(?x) RETURN ?x,?p LIMIT 1',
'MATCH (N0)=[ANY ?p :A{40,40}]=>(?x) RETURN ?x,?p LIMIT 1',
'MATCH (N0)=[ANY ?p :A{50,50}]=>(?x) RETURN ?x,?p LIMIT 1',
'MATCH (N0)=[ANY ?p :A{60,60}]=>(?x) RETURN ?x,?p LIMIT 1',
'MATCH (N0)=[ANY ?p :A{70,70}]=>(?x) RETURN ?x,?p LIMIT 1',
'MATCH (N0)=[ANY ?p :A{80,80}]=>(?x) RETURN ?x,?p LIMIT 1',
'MATCH (N0)=[ANY ?p :A{90,90}]=>(?x) RETURN ?x,?p LIMIT 1',
'MATCH (N0)=[ANY ?p :A{100,100}]=>(?x) RETURN ?x,?p LIMIT 1',
]
