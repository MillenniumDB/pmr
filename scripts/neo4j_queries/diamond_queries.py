queries = [
'MATCH ({id:"N0"})-[*]->(x) RETURN DISTINCT x LIMIT 100000;',

# Q1
'MATCH ({id:"N0"})-[:A*0..]->(x) RETURN x LIMIT 100000;',
'MATCH p=shortestPath( ({id:"N0"})-[:A*0..]->(x) ) RETURN x LIMIT 100000;',

# Q2, k = 10
'MATCH p=shortestPath( ({id:"N0"})-[:A*0..10]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..10]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..10]->(x) ) RETURN COUNT(p);',

# Q2, k = 20
'MATCH p=shortestPath( ({id:"N0"})-[:A*0..20]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..20]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..20]->(x) ) RETURN COUNT(p);',

# Q2, k = 30
'MATCH p=shortestPath( ({id:"N0"})-[:A*0..30]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..30]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..30]->(x) ) RETURN COUNT(p);',

# Q2, k = 40
'MATCH p=shortestPath( ({id:"N0"})-[:A*0..40]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..40]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..40]->(x) ) RETURN COUNT(p);',

# Q2, k = 50
'MATCH p=shortestPath( ({id:"N0"})-[:A*0..50]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..50]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..50]->(x) ) RETURN COUNT(p);',

# Q2, k = 60
'MATCH p=shortestPath( ({id:"N0"})-[:A*0..60]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..60]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..60]->(x) ) RETURN COUNT(p);',

# Q2, k = 70
'MATCH p=shortestPath( ({id:"N0"})-[:A*0..70]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..70]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..70]->(x) ) RETURN COUNT(p);',

# Q2, k = 80
'MATCH p=shortestPath( ({id:"N0"})-[:A*0..80]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..80]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..80]->(x) ) RETURN COUNT(p);',

# Q2, k = 90
'MATCH p=shortestPath( ({id:"N0"})-[:A*0..90]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..90]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..90]->(x) ) RETURN COUNT(p);',

# Q2, k = 100
'MATCH p=shortestPath( ({id:"N0"})-[:A*0..100]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..100]->(x) ) RETURN x,p LIMIT 100000;',
'MATCH p=allShortestPaths( ({id:"N0"})-[:A*0..100]->(x) ) RETURN COUNT(p);',

# Q3, k = 10
'MATCH ({id:"N0"})-[:A*10..10]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"N0"})\
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
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10) RETURN x10 LIMIT 100000;',

# Q3, k = 20
'MATCH ({id:"N0"})-[:A*20..20]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"N0"})\
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20) RETURN x20 LIMIT 100000;',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20) RETURN x20 LIMIT 100000;',

# Q3, k = 30
'MATCH ({id:"N0"})-[:A*30..30]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"N0"})\
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30) RETURN x30 LIMIT 100000;',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30) RETURN x30 LIMIT 100000;',

# Q3, k = 40
'MATCH ({id:"N0"})-[:A*40..40]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"N0"})\
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40) RETURN x40 LIMIT 100000;',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40) RETURN x40 LIMIT 100000;',

# Q3, k = 50
'MATCH ({id:"N0"})-[:A*50..50]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"N0"})\
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
-[:A]->(x41)\
-[:A]->(x42)\
-[:A]->(x43)\
-[:A]->(x44)\
-[:A]->(x45)\
-[:A]->(x46)\
-[:A]->(x47)\
-[:A]->(x48)\
-[:A]->(x49)\
-[:A]->(x50) RETURN x50 LIMIT 100000;',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50) RETURN x50 LIMIT 100000;',

# Q3, k = 60
'MATCH ({id:"N0"})-[:A*60..60]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"N0"})\
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
-[:A]->(x41)\
-[:A]->(x42)\
-[:A]->(x43)\
-[:A]->(x44)\
-[:A]->(x45)\
-[:A]->(x46)\
-[:A]->(x47)\
-[:A]->(x48)\
-[:A]->(x49)\
-[:A]->(x50)\
-[:A]->(x51)\
-[:A]->(x52)\
-[:A]->(x53)\
-[:A]->(x54)\
-[:A]->(x55)\
-[:A]->(x56)\
-[:A]->(x57)\
-[:A]->(x58)\
-[:A]->(x59)\
-[:A]->(x60) RETURN x60 LIMIT 100000;',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60) RETURN x60 LIMIT 100000;',

### Times out from here on (really bad timeouts)
# Q3, k = 70
'MATCH ({id:"N0"})-[:A*70..70]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"N0"})\
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
-[:A]->(x41)\
-[:A]->(x42)\
-[:A]->(x43)\
-[:A]->(x44)\
-[:A]->(x45)\
-[:A]->(x46)\
-[:A]->(x47)\
-[:A]->(x48)\
-[:A]->(x49)\
-[:A]->(x50)\
-[:A]->(x51)\
-[:A]->(x52)\
-[:A]->(x53)\
-[:A]->(x54)\
-[:A]->(x55)\
-[:A]->(x56)\
-[:A]->(x57)\
-[:A]->(x58)\
-[:A]->(x59)\
-[:A]->(x60)\
-[:A]->(x61)\
-[:A]->(x62)\
-[:A]->(x63)\
-[:A]->(x64)\
-[:A]->(x65)\
-[:A]->(x66)\
-[:A]->(x67)\
-[:A]->(x68)\
-[:A]->(x69)\
-[:A]->(x70) RETURN x70 LIMIT 100000;',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 MATCH (x60)-[:A]->(x61)\
 MATCH (x61)-[:A]->(x62)\
 MATCH (x62)-[:A]->(x63)\
 MATCH (x63)-[:A]->(x64)\
 MATCH (x64)-[:A]->(x65)\
 MATCH (x65)-[:A]->(x66)\
 MATCH (x66)-[:A]->(x67)\
 MATCH (x67)-[:A]->(x68)\
 MATCH (x68)-[:A]->(x69)\
 MATCH (x69)-[:A]->(x70) RETURN x70 LIMIT 100000;',

# Q3, k = 80
'MATCH ({id:"N0"})-[:A*80..80]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"N0"})\
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
-[:A]->(x41)\
-[:A]->(x42)\
-[:A]->(x43)\
-[:A]->(x44)\
-[:A]->(x45)\
-[:A]->(x46)\
-[:A]->(x47)\
-[:A]->(x48)\
-[:A]->(x49)\
-[:A]->(x50)\
-[:A]->(x51)\
-[:A]->(x52)\
-[:A]->(x53)\
-[:A]->(x54)\
-[:A]->(x55)\
-[:A]->(x56)\
-[:A]->(x57)\
-[:A]->(x58)\
-[:A]->(x59)\
-[:A]->(x60)\
-[:A]->(x61)\
-[:A]->(x62)\
-[:A]->(x63)\
-[:A]->(x64)\
-[:A]->(x65)\
-[:A]->(x66)\
-[:A]->(x67)\
-[:A]->(x68)\
-[:A]->(x69)\
-[:A]->(x70)\
-[:A]->(x71)\
-[:A]->(x72)\
-[:A]->(x73)\
-[:A]->(x74)\
-[:A]->(x75)\
-[:A]->(x76)\
-[:A]->(x77)\
-[:A]->(x78)\
-[:A]->(x79)\
-[:A]->(x80) RETURN x80 LIMIT 100000;',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 MATCH (x60)-[:A]->(x61)\
 MATCH (x61)-[:A]->(x62)\
 MATCH (x62)-[:A]->(x63)\
 MATCH (x63)-[:A]->(x64)\
 MATCH (x64)-[:A]->(x65)\
 MATCH (x65)-[:A]->(x66)\
 MATCH (x66)-[:A]->(x67)\
 MATCH (x67)-[:A]->(x68)\
 MATCH (x68)-[:A]->(x69)\
 MATCH (x69)-[:A]->(x70)\
 MATCH (x70)-[:A]->(x71)\
 MATCH (x71)-[:A]->(x72)\
 MATCH (x72)-[:A]->(x73)\
 MATCH (x73)-[:A]->(x74)\
 MATCH (x74)-[:A]->(x75)\
 MATCH (x75)-[:A]->(x76)\
 MATCH (x76)-[:A]->(x77)\
 MATCH (x77)-[:A]->(x78)\
 MATCH (x78)-[:A]->(x79)\
 MATCH (x79)-[:A]->(x80) RETURN x80 LIMIT 100000;',

# Q3, k = 90
'MATCH ({id:"N0"})-[:A*90..90]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"N0"})\
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
-[:A]->(x41)\
-[:A]->(x42)\
-[:A]->(x43)\
-[:A]->(x44)\
-[:A]->(x45)\
-[:A]->(x46)\
-[:A]->(x47)\
-[:A]->(x48)\
-[:A]->(x49)\
-[:A]->(x50)\
-[:A]->(x51)\
-[:A]->(x52)\
-[:A]->(x53)\
-[:A]->(x54)\
-[:A]->(x55)\
-[:A]->(x56)\
-[:A]->(x57)\
-[:A]->(x58)\
-[:A]->(x59)\
-[:A]->(x60)\
-[:A]->(x61)\
-[:A]->(x62)\
-[:A]->(x63)\
-[:A]->(x64)\
-[:A]->(x65)\
-[:A]->(x66)\
-[:A]->(x67)\
-[:A]->(x68)\
-[:A]->(x69)\
-[:A]->(x70)\
-[:A]->(x71)\
-[:A]->(x72)\
-[:A]->(x73)\
-[:A]->(x74)\
-[:A]->(x75)\
-[:A]->(x76)\
-[:A]->(x77)\
-[:A]->(x78)\
-[:A]->(x79)\
-[:A]->(x80)\
-[:A]->(x81)\
-[:A]->(x82)\
-[:A]->(x83)\
-[:A]->(x84)\
-[:A]->(x85)\
-[:A]->(x86)\
-[:A]->(x87)\
-[:A]->(x88)\
-[:A]->(x89)\
-[:A]->(x90) RETURN x90 LIMIT 100000;',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 MATCH (x60)-[:A]->(x61)\
 MATCH (x61)-[:A]->(x62)\
 MATCH (x62)-[:A]->(x63)\
 MATCH (x63)-[:A]->(x64)\
 MATCH (x64)-[:A]->(x65)\
 MATCH (x65)-[:A]->(x66)\
 MATCH (x66)-[:A]->(x67)\
 MATCH (x67)-[:A]->(x68)\
 MATCH (x68)-[:A]->(x69)\
 MATCH (x69)-[:A]->(x70)\
 MATCH (x70)-[:A]->(x71)\
 MATCH (x71)-[:A]->(x72)\
 MATCH (x72)-[:A]->(x73)\
 MATCH (x73)-[:A]->(x74)\
 MATCH (x74)-[:A]->(x75)\
 MATCH (x75)-[:A]->(x76)\
 MATCH (x76)-[:A]->(x77)\
 MATCH (x77)-[:A]->(x78)\
 MATCH (x78)-[:A]->(x79)\
 MATCH (x79)-[:A]->(x80)\
 MATCH (x80)-[:A]->(x81)\
 MATCH (x81)-[:A]->(x82)\
 MATCH (x82)-[:A]->(x83)\
 MATCH (x83)-[:A]->(x84)\
 MATCH (x84)-[:A]->(x85)\
 MATCH (x85)-[:A]->(x86)\
 MATCH (x86)-[:A]->(x87)\
 MATCH (x87)-[:A]->(x88)\
 MATCH (x88)-[:A]->(x89)\
 MATCH (x89)-[:A]->(x90) RETURN x90 LIMIT 100000;',

# Q3, k = 100
'MATCH ({id:"N0"})-[:A*100..100]->(x) RETURN x LIMIT 100000;',
'MATCH ({id:"N0"})\
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
-[:A]->(x41)\
-[:A]->(x42)\
-[:A]->(x43)\
-[:A]->(x44)\
-[:A]->(x45)\
-[:A]->(x46)\
-[:A]->(x47)\
-[:A]->(x48)\
-[:A]->(x49)\
-[:A]->(x50)\
-[:A]->(x51)\
-[:A]->(x52)\
-[:A]->(x53)\
-[:A]->(x54)\
-[:A]->(x55)\
-[:A]->(x56)\
-[:A]->(x57)\
-[:A]->(x58)\
-[:A]->(x59)\
-[:A]->(x60)\
-[:A]->(x61)\
-[:A]->(x62)\
-[:A]->(x63)\
-[:A]->(x64)\
-[:A]->(x65)\
-[:A]->(x66)\
-[:A]->(x67)\
-[:A]->(x68)\
-[:A]->(x69)\
-[:A]->(x70)\
-[:A]->(x71)\
-[:A]->(x72)\
-[:A]->(x73)\
-[:A]->(x74)\
-[:A]->(x75)\
-[:A]->(x76)\
-[:A]->(x77)\
-[:A]->(x78)\
-[:A]->(x79)\
-[:A]->(x80)\
-[:A]->(x81)\
-[:A]->(x82)\
-[:A]->(x83)\
-[:A]->(x84)\
-[:A]->(x85)\
-[:A]->(x86)\
-[:A]->(x87)\
-[:A]->(x88)\
-[:A]->(x89)\
-[:A]->(x90)\
-[:A]->(x91)\
-[:A]->(x92)\
-[:A]->(x93)\
-[:A]->(x94)\
-[:A]->(x95)\
-[:A]->(x96)\
-[:A]->(x97)\
-[:A]->(x98)\
-[:A]->(x99)\
-[:A]->(x100) RETURN x100 LIMIT 100000;',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 MATCH (x60)-[:A]->(x61)\
 MATCH (x61)-[:A]->(x62)\
 MATCH (x62)-[:A]->(x63)\
 MATCH (x63)-[:A]->(x64)\
 MATCH (x64)-[:A]->(x65)\
 MATCH (x65)-[:A]->(x66)\
 MATCH (x66)-[:A]->(x67)\
 MATCH (x67)-[:A]->(x68)\
 MATCH (x68)-[:A]->(x69)\
 MATCH (x69)-[:A]->(x70)\
 MATCH (x70)-[:A]->(x71)\
 MATCH (x71)-[:A]->(x72)\
 MATCH (x72)-[:A]->(x73)\
 MATCH (x73)-[:A]->(x74)\
 MATCH (x74)-[:A]->(x75)\
 MATCH (x75)-[:A]->(x76)\
 MATCH (x76)-[:A]->(x77)\
 MATCH (x77)-[:A]->(x78)\
 MATCH (x78)-[:A]->(x79)\
 MATCH (x79)-[:A]->(x80)\
 MATCH (x80)-[:A]->(x81)\
 MATCH (x81)-[:A]->(x82)\
 MATCH (x82)-[:A]->(x83)\
 MATCH (x83)-[:A]->(x84)\
 MATCH (x84)-[:A]->(x85)\
 MATCH (x85)-[:A]->(x86)\
 MATCH (x86)-[:A]->(x87)\
 MATCH (x87)-[:A]->(x88)\
 MATCH (x88)-[:A]->(x89)\
 MATCH (x89)-[:A]->(x90)\
 MATCH (x90)-[:A]->(x91)\
 MATCH (x91)-[:A]->(x92)\
 MATCH (x92)-[:A]->(x93)\
 MATCH (x93)-[:A]->(x94)\
 MATCH (x94)-[:A]->(x95)\
 MATCH (x95)-[:A]->(x96)\
 MATCH (x96)-[:A]->(x97)\
 MATCH (x97)-[:A]->(x98)\
 MATCH (x98)-[:A]->(x99)\
 MATCH (x99)-[:A]->(x100) RETURN x100 LIMIT 100000;',


# Q4 k = 10
'MATCH p=shortestPath( ({id:"N0"})-[:A*1..10]->(x) ) WHERE length(p)=10 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
'MATCH ({id:"N0"})-[:A]->(x1)\
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
'MATCH p=( ({id:"N0"}) \
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
'MATCH ({id:"N0"})-[:A]->(x1)\
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

# Q4 k = 20
'MATCH p=shortestPath( ({id:"N0"})-[:A*1..20]->(x) ) WHERE length(p)=20 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
) RETURN x20,p LIMIT 100000;',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 RETURN * LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
) RETURN COUNT(p);',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 RETURN COUNT(*);',

# Q4 k = 30
'MATCH p=shortestPath( ({id:"N0"})-[:A*1..30]->(x) ) WHERE length(p)=30 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
) RETURN x30,p LIMIT 100000;',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 RETURN * LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
) RETURN COUNT(*);',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 RETURN COUNT(*);',

# Q4 k = 40
'MATCH p=shortestPath( ({id:"N0"})-[:A*1..40]->(x) ) WHERE length(p)=40 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
) RETURN x40,p LIMIT 100000;',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 RETURN * LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
) RETURN COUNT(p);',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 RETURN COUNT(*);',

# Q4 k = 50
'MATCH p=shortestPath( ({id:"N0"})-[:A*1..50]->(x) ) WHERE length(p)=50 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
-[:A]->(x41)\
-[:A]->(x42)\
-[:A]->(x43)\
-[:A]->(x44)\
-[:A]->(x45)\
-[:A]->(x46)\
-[:A]->(x47)\
-[:A]->(x48)\
-[:A]->(x49)\
-[:A]->(x50)\
) RETURN x50,p LIMIT 100000;',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 RETURN * LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
-[:A]->(x41)\
-[:A]->(x42)\
-[:A]->(x43)\
-[:A]->(x44)\
-[:A]->(x45)\
-[:A]->(x46)\
-[:A]->(x47)\
-[:A]->(x48)\
-[:A]->(x49)\
-[:A]->(x50)\
) RETURN COUNT(p);',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 RETURN COUNT(*);',

# Q4 k = 60
'MATCH p=shortestPath( ({id:"N0"})-[:A*1..60]->(x) ) WHERE length(p)=60 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
-[:A]->(x41)\
-[:A]->(x42)\
-[:A]->(x43)\
-[:A]->(x44)\
-[:A]->(x45)\
-[:A]->(x46)\
-[:A]->(x47)\
-[:A]->(x48)\
-[:A]->(x49)\
-[:A]->(x50)\
-[:A]->(x51)\
-[:A]->(x52)\
-[:A]->(x53)\
-[:A]->(x54)\
-[:A]->(x55)\
-[:A]->(x56)\
-[:A]->(x57)\
-[:A]->(x58)\
-[:A]->(x59)\
-[:A]->(x60)\
) RETURN x60,p LIMIT 100000;',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 RETURN * LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
-[:A]->(x41)\
-[:A]->(x42)\
-[:A]->(x43)\
-[:A]->(x44)\
-[:A]->(x45)\
-[:A]->(x46)\
-[:A]->(x47)\
-[:A]->(x48)\
-[:A]->(x49)\
-[:A]->(x50)\
-[:A]->(x51)\
-[:A]->(x52)\
-[:A]->(x53)\
-[:A]->(x54)\
-[:A]->(x55)\
-[:A]->(x56)\
-[:A]->(x57)\
-[:A]->(x58)\
-[:A]->(x59)\
-[:A]->(x60)\
) RETURN COUNT(p);',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 RETURN COUNT(*);',

# Q4 k = 70
'MATCH p=shortestPath( ({id:"N0"})-[:A*1..70]->(x) ) WHERE length(p)=70 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
-[:A]->(x41)\
-[:A]->(x42)\
-[:A]->(x43)\
-[:A]->(x44)\
-[:A]->(x45)\
-[:A]->(x46)\
-[:A]->(x47)\
-[:A]->(x48)\
-[:A]->(x49)\
-[:A]->(x50)\
-[:A]->(x51)\
-[:A]->(x52)\
-[:A]->(x53)\
-[:A]->(x54)\
-[:A]->(x55)\
-[:A]->(x56)\
-[:A]->(x57)\
-[:A]->(x58)\
-[:A]->(x59)\
-[:A]->(x60)\
-[:A]->(x61)\
-[:A]->(x62)\
-[:A]->(x63)\
-[:A]->(x64)\
-[:A]->(x65)\
-[:A]->(x66)\
-[:A]->(x67)\
-[:A]->(x68)\
-[:A]->(x69)\
-[:A]->(x70)\
) RETURN x70,p LIMIT 100000;',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 MATCH (x60)-[:A]->(x61)\
 MATCH (x61)-[:A]->(x62)\
 MATCH (x62)-[:A]->(x63)\
 MATCH (x63)-[:A]->(x64)\
 MATCH (x64)-[:A]->(x65)\
 MATCH (x65)-[:A]->(x66)\
 MATCH (x66)-[:A]->(x67)\
 MATCH (x67)-[:A]->(x68)\
 MATCH (x68)-[:A]->(x69)\
 MATCH (x69)-[:A]->(x70)\
 RETURN * LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
-[:A]->(x41)\
-[:A]->(x42)\
-[:A]->(x43)\
-[:A]->(x44)\
-[:A]->(x45)\
-[:A]->(x46)\
-[:A]->(x47)\
-[:A]->(x48)\
-[:A]->(x49)\
-[:A]->(x50)\
-[:A]->(x51)\
-[:A]->(x52)\
-[:A]->(x53)\
-[:A]->(x54)\
-[:A]->(x55)\
-[:A]->(x56)\
-[:A]->(x57)\
-[:A]->(x58)\
-[:A]->(x59)\
-[:A]->(x60)\
-[:A]->(x61)\
-[:A]->(x62)\
-[:A]->(x63)\
-[:A]->(x64)\
-[:A]->(x65)\
-[:A]->(x66)\
-[:A]->(x67)\
-[:A]->(x68)\
-[:A]->(x69)\
-[:A]->(x70)\
) RETURN COUNT(p);',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 MATCH (x60)-[:A]->(x61)\
 MATCH (x61)-[:A]->(x62)\
 MATCH (x62)-[:A]->(x63)\
 MATCH (x63)-[:A]->(x64)\
 MATCH (x64)-[:A]->(x65)\
 MATCH (x65)-[:A]->(x66)\
 MATCH (x66)-[:A]->(x67)\
 MATCH (x67)-[:A]->(x68)\
 MATCH (x68)-[:A]->(x69)\
 MATCH (x69)-[:A]->(x70)\
 RETURN COUNT(*);',

# Q4 k = 80
'MATCH p=shortestPath( ({id:"N0"})-[:A*1..80]->(x) ) WHERE length(p)=80 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
-[:A]->(x41)\
-[:A]->(x42)\
-[:A]->(x43)\
-[:A]->(x44)\
-[:A]->(x45)\
-[:A]->(x46)\
-[:A]->(x47)\
-[:A]->(x48)\
-[:A]->(x49)\
-[:A]->(x50)\
-[:A]->(x51)\
-[:A]->(x52)\
-[:A]->(x53)\
-[:A]->(x54)\
-[:A]->(x55)\
-[:A]->(x56)\
-[:A]->(x57)\
-[:A]->(x58)\
-[:A]->(x59)\
-[:A]->(x60)\
-[:A]->(x61)\
-[:A]->(x62)\
-[:A]->(x63)\
-[:A]->(x64)\
-[:A]->(x65)\
-[:A]->(x66)\
-[:A]->(x67)\
-[:A]->(x68)\
-[:A]->(x69)\
-[:A]->(x70)\
-[:A]->(x71)\
-[:A]->(x72)\
-[:A]->(x73)\
-[:A]->(x74)\
-[:A]->(x75)\
-[:A]->(x76)\
-[:A]->(x77)\
-[:A]->(x78)\
-[:A]->(x79)\
-[:A]->(x80)\
) RETURN x80,p LIMIT 100000;',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 MATCH (x60)-[:A]->(x61)\
 MATCH (x61)-[:A]->(x62)\
 MATCH (x62)-[:A]->(x63)\
 MATCH (x63)-[:A]->(x64)\
 MATCH (x64)-[:A]->(x65)\
 MATCH (x65)-[:A]->(x66)\
 MATCH (x66)-[:A]->(x67)\
 MATCH (x67)-[:A]->(x68)\
 MATCH (x68)-[:A]->(x69)\
 MATCH (x69)-[:A]->(x70)\
 MATCH (x70)-[:A]->(x71)\
 MATCH (x71)-[:A]->(x72)\
 MATCH (x72)-[:A]->(x73)\
 MATCH (x73)-[:A]->(x74)\
 MATCH (x74)-[:A]->(x75)\
 MATCH (x75)-[:A]->(x76)\
 MATCH (x76)-[:A]->(x77)\
 MATCH (x77)-[:A]->(x78)\
 MATCH (x78)-[:A]->(x79)\
 MATCH (x79)-[:A]->(x80)\
 RETURN * LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
-[:A]->(x41)\
-[:A]->(x42)\
-[:A]->(x43)\
-[:A]->(x44)\
-[:A]->(x45)\
-[:A]->(x46)\
-[:A]->(x47)\
-[:A]->(x48)\
-[:A]->(x49)\
-[:A]->(x50)\
-[:A]->(x51)\
-[:A]->(x52)\
-[:A]->(x53)\
-[:A]->(x54)\
-[:A]->(x55)\
-[:A]->(x56)\
-[:A]->(x57)\
-[:A]->(x58)\
-[:A]->(x59)\
-[:A]->(x60)\
-[:A]->(x61)\
-[:A]->(x62)\
-[:A]->(x63)\
-[:A]->(x64)\
-[:A]->(x65)\
-[:A]->(x66)\
-[:A]->(x67)\
-[:A]->(x68)\
-[:A]->(x69)\
-[:A]->(x70)\
-[:A]->(x71)\
-[:A]->(x72)\
-[:A]->(x73)\
-[:A]->(x74)\
-[:A]->(x75)\
-[:A]->(x76)\
-[:A]->(x77)\
-[:A]->(x78)\
-[:A]->(x79)\
-[:A]->(x80)\
) RETURN COUNT(p);',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 MATCH (x60)-[:A]->(x61)\
 MATCH (x61)-[:A]->(x62)\
 MATCH (x62)-[:A]->(x63)\
 MATCH (x63)-[:A]->(x64)\
 MATCH (x64)-[:A]->(x65)\
 MATCH (x65)-[:A]->(x66)\
 MATCH (x66)-[:A]->(x67)\
 MATCH (x67)-[:A]->(x68)\
 MATCH (x68)-[:A]->(x69)\
 MATCH (x69)-[:A]->(x70)\
 MATCH (x70)-[:A]->(x71)\
 MATCH (x71)-[:A]->(x72)\
 MATCH (x72)-[:A]->(x73)\
 MATCH (x73)-[:A]->(x74)\
 MATCH (x74)-[:A]->(x75)\
 MATCH (x75)-[:A]->(x76)\
 MATCH (x76)-[:A]->(x77)\
 MATCH (x77)-[:A]->(x78)\
 MATCH (x78)-[:A]->(x79)\
 MATCH (x79)-[:A]->(x80)\
 RETURN COUNT(*);',

# Q4 k = 90
'MATCH p=shortestPath( ({id:"N0"})-[:A*1..90]->(x) ) WHERE length(p)=90 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
-[:A]->(x41)\
-[:A]->(x42)\
-[:A]->(x43)\
-[:A]->(x44)\
-[:A]->(x45)\
-[:A]->(x46)\
-[:A]->(x47)\
-[:A]->(x48)\
-[:A]->(x49)\
-[:A]->(x50)\
-[:A]->(x51)\
-[:A]->(x52)\
-[:A]->(x53)\
-[:A]->(x54)\
-[:A]->(x55)\
-[:A]->(x56)\
-[:A]->(x57)\
-[:A]->(x58)\
-[:A]->(x59)\
-[:A]->(x60)\
-[:A]->(x61)\
-[:A]->(x62)\
-[:A]->(x63)\
-[:A]->(x64)\
-[:A]->(x65)\
-[:A]->(x66)\
-[:A]->(x67)\
-[:A]->(x68)\
-[:A]->(x69)\
-[:A]->(x70)\
-[:A]->(x71)\
-[:A]->(x72)\
-[:A]->(x73)\
-[:A]->(x74)\
-[:A]->(x75)\
-[:A]->(x76)\
-[:A]->(x77)\
-[:A]->(x78)\
-[:A]->(x79)\
-[:A]->(x80)\
-[:A]->(x81)\
-[:A]->(x82)\
-[:A]->(x83)\
-[:A]->(x84)\
-[:A]->(x85)\
-[:A]->(x86)\
-[:A]->(x87)\
-[:A]->(x88)\
-[:A]->(x89)\
-[:A]->(x90)\
) RETURN x90,p LIMIT 100000;',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 MATCH (x60)-[:A]->(x61)\
 MATCH (x61)-[:A]->(x62)\
 MATCH (x62)-[:A]->(x63)\
 MATCH (x63)-[:A]->(x64)\
 MATCH (x64)-[:A]->(x65)\
 MATCH (x65)-[:A]->(x66)\
 MATCH (x66)-[:A]->(x67)\
 MATCH (x67)-[:A]->(x68)\
 MATCH (x68)-[:A]->(x69)\
 MATCH (x69)-[:A]->(x70)\
 MATCH (x70)-[:A]->(x71)\
 MATCH (x71)-[:A]->(x72)\
 MATCH (x72)-[:A]->(x73)\
 MATCH (x73)-[:A]->(x74)\
 MATCH (x74)-[:A]->(x75)\
 MATCH (x75)-[:A]->(x76)\
 MATCH (x76)-[:A]->(x77)\
 MATCH (x77)-[:A]->(x78)\
 MATCH (x78)-[:A]->(x79)\
 MATCH (x79)-[:A]->(x80)\
 MATCH (x80)-[:A]->(x81)\
 MATCH (x81)-[:A]->(x82)\
 MATCH (x82)-[:A]->(x83)\
 MATCH (x83)-[:A]->(x84)\
 MATCH (x84)-[:A]->(x85)\
 MATCH (x85)-[:A]->(x86)\
 MATCH (x86)-[:A]->(x87)\
 MATCH (x87)-[:A]->(x88)\
 MATCH (x88)-[:A]->(x89)\
 MATCH (x89)-[:A]->(x90)\
 RETURN * LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
-[:A]->(x41)\
-[:A]->(x42)\
-[:A]->(x43)\
-[:A]->(x44)\
-[:A]->(x45)\
-[:A]->(x46)\
-[:A]->(x47)\
-[:A]->(x48)\
-[:A]->(x49)\
-[:A]->(x50)\
-[:A]->(x51)\
-[:A]->(x52)\
-[:A]->(x53)\
-[:A]->(x54)\
-[:A]->(x55)\
-[:A]->(x56)\
-[:A]->(x57)\
-[:A]->(x58)\
-[:A]->(x59)\
-[:A]->(x60)\
-[:A]->(x61)\
-[:A]->(x62)\
-[:A]->(x63)\
-[:A]->(x64)\
-[:A]->(x65)\
-[:A]->(x66)\
-[:A]->(x67)\
-[:A]->(x68)\
-[:A]->(x69)\
-[:A]->(x70)\
-[:A]->(x71)\
-[:A]->(x72)\
-[:A]->(x73)\
-[:A]->(x74)\
-[:A]->(x75)\
-[:A]->(x76)\
-[:A]->(x77)\
-[:A]->(x78)\
-[:A]->(x79)\
-[:A]->(x80)\
-[:A]->(x81)\
-[:A]->(x82)\
-[:A]->(x83)\
-[:A]->(x84)\
-[:A]->(x85)\
-[:A]->(x86)\
-[:A]->(x87)\
-[:A]->(x88)\
-[:A]->(x89)\
-[:A]->(x90)\
) RETURN COUNT(p);',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 MATCH (x60)-[:A]->(x61)\
 MATCH (x61)-[:A]->(x62)\
 MATCH (x62)-[:A]->(x63)\
 MATCH (x63)-[:A]->(x64)\
 MATCH (x64)-[:A]->(x65)\
 MATCH (x65)-[:A]->(x66)\
 MATCH (x66)-[:A]->(x67)\
 MATCH (x67)-[:A]->(x68)\
 MATCH (x68)-[:A]->(x69)\
 MATCH (x69)-[:A]->(x70)\
 MATCH (x70)-[:A]->(x71)\
 MATCH (x71)-[:A]->(x72)\
 MATCH (x72)-[:A]->(x73)\
 MATCH (x73)-[:A]->(x74)\
 MATCH (x74)-[:A]->(x75)\
 MATCH (x75)-[:A]->(x76)\
 MATCH (x76)-[:A]->(x77)\
 MATCH (x77)-[:A]->(x78)\
 MATCH (x78)-[:A]->(x79)\
 MATCH (x79)-[:A]->(x80)\
 MATCH (x80)-[:A]->(x81)\
 MATCH (x81)-[:A]->(x82)\
 MATCH (x82)-[:A]->(x83)\
 MATCH (x83)-[:A]->(x84)\
 MATCH (x84)-[:A]->(x85)\
 MATCH (x85)-[:A]->(x86)\
 MATCH (x86)-[:A]->(x87)\
 MATCH (x87)-[:A]->(x88)\
 MATCH (x88)-[:A]->(x89)\
 MATCH (x89)-[:A]->(x90)\
 RETURN COUNT(*);',

# Q4 k = 100
'MATCH p=shortestPath( ({id:"N0"})-[:A*1..100]->(x) ) WHERE length(p)=100 RETURN x,p LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
-[:A]->(x41)\
-[:A]->(x42)\
-[:A]->(x43)\
-[:A]->(x44)\
-[:A]->(x45)\
-[:A]->(x46)\
-[:A]->(x47)\
-[:A]->(x48)\
-[:A]->(x49)\
-[:A]->(x50)\
-[:A]->(x51)\
-[:A]->(x52)\
-[:A]->(x53)\
-[:A]->(x54)\
-[:A]->(x55)\
-[:A]->(x56)\
-[:A]->(x57)\
-[:A]->(x58)\
-[:A]->(x59)\
-[:A]->(x60)\
-[:A]->(x61)\
-[:A]->(x62)\
-[:A]->(x63)\
-[:A]->(x64)\
-[:A]->(x65)\
-[:A]->(x66)\
-[:A]->(x67)\
-[:A]->(x68)\
-[:A]->(x69)\
-[:A]->(x70)\
-[:A]->(x71)\
-[:A]->(x72)\
-[:A]->(x73)\
-[:A]->(x74)\
-[:A]->(x75)\
-[:A]->(x76)\
-[:A]->(x77)\
-[:A]->(x78)\
-[:A]->(x79)\
-[:A]->(x80)\
-[:A]->(x81)\
-[:A]->(x82)\
-[:A]->(x83)\
-[:A]->(x84)\
-[:A]->(x85)\
-[:A]->(x86)\
-[:A]->(x87)\
-[:A]->(x88)\
-[:A]->(x89)\
-[:A]->(x90)\
-[:A]->(x91)\
-[:A]->(x92)\
-[:A]->(x93)\
-[:A]->(x94)\
-[:A]->(x95)\
-[:A]->(x96)\
-[:A]->(x97)\
-[:A]->(x98)\
-[:A]->(x99)\
-[:A]->(x100)\
) RETURN x100,p LIMIT 100000;',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 MATCH (x60)-[:A]->(x61)\
 MATCH (x61)-[:A]->(x62)\
 MATCH (x62)-[:A]->(x63)\
 MATCH (x63)-[:A]->(x64)\
 MATCH (x64)-[:A]->(x65)\
 MATCH (x65)-[:A]->(x66)\
 MATCH (x66)-[:A]->(x67)\
 MATCH (x67)-[:A]->(x68)\
 MATCH (x68)-[:A]->(x69)\
 MATCH (x69)-[:A]->(x70)\
 MATCH (x70)-[:A]->(x71)\
 MATCH (x71)-[:A]->(x72)\
 MATCH (x72)-[:A]->(x73)\
 MATCH (x73)-[:A]->(x74)\
 MATCH (x74)-[:A]->(x75)\
 MATCH (x75)-[:A]->(x76)\
 MATCH (x76)-[:A]->(x77)\
 MATCH (x77)-[:A]->(x78)\
 MATCH (x78)-[:A]->(x79)\
 MATCH (x79)-[:A]->(x80)\
 MATCH (x80)-[:A]->(x81)\
 MATCH (x81)-[:A]->(x82)\
 MATCH (x82)-[:A]->(x83)\
 MATCH (x83)-[:A]->(x84)\
 MATCH (x84)-[:A]->(x85)\
 MATCH (x85)-[:A]->(x86)\
 MATCH (x86)-[:A]->(x87)\
 MATCH (x87)-[:A]->(x88)\
 MATCH (x88)-[:A]->(x89)\
 MATCH (x89)-[:A]->(x90)\
 MATCH (x90)-[:A]->(x91)\
 MATCH (x91)-[:A]->(x92)\
 MATCH (x92)-[:A]->(x93)\
 MATCH (x93)-[:A]->(x94)\
 MATCH (x94)-[:A]->(x95)\
 MATCH (x95)-[:A]->(x96)\
 MATCH (x96)-[:A]->(x97)\
 MATCH (x97)-[:A]->(x98)\
 MATCH (x98)-[:A]->(x99)\
 MATCH (x99)-[:A]->(x100)\
 RETURN * LIMIT 100000;',
'MATCH p=( ({id:"N0"}) \
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
-[:A]->(x11)\
-[:A]->(x12)\
-[:A]->(x13)\
-[:A]->(x14)\
-[:A]->(x15)\
-[:A]->(x16)\
-[:A]->(x17)\
-[:A]->(x18)\
-[:A]->(x19)\
-[:A]->(x20)\
-[:A]->(x21)\
-[:A]->(x22)\
-[:A]->(x23)\
-[:A]->(x24)\
-[:A]->(x25)\
-[:A]->(x26)\
-[:A]->(x27)\
-[:A]->(x28)\
-[:A]->(x29)\
-[:A]->(x30)\
-[:A]->(x31)\
-[:A]->(x32)\
-[:A]->(x33)\
-[:A]->(x34)\
-[:A]->(x35)\
-[:A]->(x36)\
-[:A]->(x37)\
-[:A]->(x38)\
-[:A]->(x39)\
-[:A]->(x40)\
-[:A]->(x41)\
-[:A]->(x42)\
-[:A]->(x43)\
-[:A]->(x44)\
-[:A]->(x45)\
-[:A]->(x46)\
-[:A]->(x47)\
-[:A]->(x48)\
-[:A]->(x49)\
-[:A]->(x50)\
-[:A]->(x51)\
-[:A]->(x52)\
-[:A]->(x53)\
-[:A]->(x54)\
-[:A]->(x55)\
-[:A]->(x56)\
-[:A]->(x57)\
-[:A]->(x58)\
-[:A]->(x59)\
-[:A]->(x60)\
-[:A]->(x61)\
-[:A]->(x62)\
-[:A]->(x63)\
-[:A]->(x64)\
-[:A]->(x65)\
-[:A]->(x66)\
-[:A]->(x67)\
-[:A]->(x68)\
-[:A]->(x69)\
-[:A]->(x70)\
-[:A]->(x71)\
-[:A]->(x72)\
-[:A]->(x73)\
-[:A]->(x74)\
-[:A]->(x75)\
-[:A]->(x76)\
-[:A]->(x77)\
-[:A]->(x78)\
-[:A]->(x79)\
-[:A]->(x80)\
-[:A]->(x81)\
-[:A]->(x82)\
-[:A]->(x83)\
-[:A]->(x84)\
-[:A]->(x85)\
-[:A]->(x86)\
-[:A]->(x87)\
-[:A]->(x88)\
-[:A]->(x89)\
-[:A]->(x90)\
-[:A]->(x91)\
-[:A]->(x92)\
-[:A]->(x93)\
-[:A]->(x94)\
-[:A]->(x95)\
-[:A]->(x96)\
-[:A]->(x97)\
-[:A]->(x98)\
-[:A]->(x99)\
-[:A]->(x100)\
) RETURN COUNT(p);',
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 MATCH (x60)-[:A]->(x61)\
 MATCH (x61)-[:A]->(x62)\
 MATCH (x62)-[:A]->(x63)\
 MATCH (x63)-[:A]->(x64)\
 MATCH (x64)-[:A]->(x65)\
 MATCH (x65)-[:A]->(x66)\
 MATCH (x66)-[:A]->(x67)\
 MATCH (x67)-[:A]->(x68)\
 MATCH (x68)-[:A]->(x69)\
 MATCH (x69)-[:A]->(x70)\
 MATCH (x70)-[:A]->(x71)\
 MATCH (x71)-[:A]->(x72)\
 MATCH (x72)-[:A]->(x73)\
 MATCH (x73)-[:A]->(x74)\
 MATCH (x74)-[:A]->(x75)\
 MATCH (x75)-[:A]->(x76)\
 MATCH (x76)-[:A]->(x77)\
 MATCH (x77)-[:A]->(x78)\
 MATCH (x78)-[:A]->(x79)\
 MATCH (x79)-[:A]->(x80)\
 MATCH (x80)-[:A]->(x81)\
 MATCH (x81)-[:A]->(x82)\
 MATCH (x82)-[:A]->(x83)\
 MATCH (x83)-[:A]->(x84)\
 MATCH (x84)-[:A]->(x85)\
 MATCH (x85)-[:A]->(x86)\
 MATCH (x86)-[:A]->(x87)\
 MATCH (x87)-[:A]->(x88)\
 MATCH (x88)-[:A]->(x89)\
 MATCH (x89)-[:A]->(x90)\
 MATCH (x90)-[:A]->(x91)\
 MATCH (x91)-[:A]->(x92)\
 MATCH (x92)-[:A]->(x93)\
 MATCH (x93)-[:A]->(x94)\
 MATCH (x94)-[:A]->(x95)\
 MATCH (x95)-[:A]->(x96)\
 MATCH (x96)-[:A]->(x97)\
 MATCH (x97)-[:A]->(x98)\
 MATCH (x98)-[:A]->(x99)\
 MATCH (x99)-[:A]->(x100)\
 RETURN COUNT(*);',

# Q5
'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 RETURN * LIMIT 1;',

'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 RETURN * LIMIT 1;',

'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 RETURN * LIMIT 1;',

'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 RETURN * LIMIT 1;',

'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 RETURN * LIMIT 1;',

'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 RETURN * LIMIT 1;',

'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 RETURN * LIMIT 1;',

'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 MATCH (x60)-[:A]->(x61)\
 MATCH (x61)-[:A]->(x62)\
 MATCH (x62)-[:A]->(x63)\
 MATCH (x63)-[:A]->(x64)\
 MATCH (x64)-[:A]->(x65)\
 MATCH (x65)-[:A]->(x66)\
 MATCH (x66)-[:A]->(x67)\
 MATCH (x67)-[:A]->(x68)\
 MATCH (x68)-[:A]->(x69)\
 MATCH (x69)-[:A]->(x60)\
 RETURN * LIMIT 1;',

'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 MATCH (x60)-[:A]->(x61)\
 MATCH (x61)-[:A]->(x62)\
 MATCH (x62)-[:A]->(x63)\
 MATCH (x63)-[:A]->(x64)\
 MATCH (x64)-[:A]->(x65)\
 MATCH (x65)-[:A]->(x66)\
 MATCH (x66)-[:A]->(x67)\
 MATCH (x67)-[:A]->(x68)\
 MATCH (x68)-[:A]->(x69)\
 MATCH (x69)-[:A]->(x60)\
 MATCH (x70)-[:A]->(x71)\
 MATCH (x71)-[:A]->(x72)\
 MATCH (x72)-[:A]->(x73)\
 MATCH (x73)-[:A]->(x74)\
 MATCH (x74)-[:A]->(x75)\
 MATCH (x75)-[:A]->(x76)\
 MATCH (x76)-[:A]->(x77)\
 MATCH (x77)-[:A]->(x78)\
 MATCH (x78)-[:A]->(x79)\
 MATCH (x79)-[:A]->(x80)\
 RETURN * LIMIT 1;',

'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 MATCH (x60)-[:A]->(x61)\
 MATCH (x61)-[:A]->(x62)\
 MATCH (x62)-[:A]->(x63)\
 MATCH (x63)-[:A]->(x64)\
 MATCH (x64)-[:A]->(x65)\
 MATCH (x65)-[:A]->(x66)\
 MATCH (x66)-[:A]->(x67)\
 MATCH (x67)-[:A]->(x68)\
 MATCH (x68)-[:A]->(x69)\
 MATCH (x69)-[:A]->(x60)\
 MATCH (x70)-[:A]->(x71)\
 MATCH (x71)-[:A]->(x72)\
 MATCH (x72)-[:A]->(x73)\
 MATCH (x73)-[:A]->(x74)\
 MATCH (x74)-[:A]->(x75)\
 MATCH (x75)-[:A]->(x76)\
 MATCH (x76)-[:A]->(x77)\
 MATCH (x77)-[:A]->(x78)\
 MATCH (x78)-[:A]->(x79)\
 MATCH (x79)-[:A]->(x80)\
 MATCH (x80)-[:A]->(x81)\
 MATCH (x81)-[:A]->(x82)\
 MATCH (x82)-[:A]->(x83)\
 MATCH (x83)-[:A]->(x84)\
 MATCH (x84)-[:A]->(x85)\
 MATCH (x85)-[:A]->(x86)\
 MATCH (x86)-[:A]->(x87)\
 MATCH (x87)-[:A]->(x88)\
 MATCH (x88)-[:A]->(x89)\
 MATCH (x89)-[:A]->(x90)\
 RETURN * LIMIT 1;',

'MATCH ({id:"N0"})-[:A]->(x1)\
 MATCH (x1)-[:A]->(x2)\
 MATCH (x2)-[:A]->(x3)\
 MATCH (x3)-[:A]->(x4)\
 MATCH (x4)-[:A]->(x5)\
 MATCH (x5)-[:A]->(x6)\
 MATCH (x6)-[:A]->(x7)\
 MATCH (x7)-[:A]->(x8)\
 MATCH (x8)-[:A]->(x9)\
 MATCH (x9)-[:A]->(x10)\
 MATCH (x10)-[:A]->(x11)\
 MATCH (x11)-[:A]->(x12)\
 MATCH (x12)-[:A]->(x13)\
 MATCH (x13)-[:A]->(x14)\
 MATCH (x14)-[:A]->(x15)\
 MATCH (x15)-[:A]->(x16)\
 MATCH (x16)-[:A]->(x17)\
 MATCH (x17)-[:A]->(x18)\
 MATCH (x18)-[:A]->(x19)\
 MATCH (x19)-[:A]->(x20)\
 MATCH (x20)-[:A]->(x21)\
 MATCH (x21)-[:A]->(x22)\
 MATCH (x22)-[:A]->(x23)\
 MATCH (x23)-[:A]->(x24)\
 MATCH (x24)-[:A]->(x25)\
 MATCH (x25)-[:A]->(x26)\
 MATCH (x26)-[:A]->(x27)\
 MATCH (x27)-[:A]->(x28)\
 MATCH (x28)-[:A]->(x29)\
 MATCH (x29)-[:A]->(x30)\
 MATCH (x30)-[:A]->(x31)\
 MATCH (x31)-[:A]->(x32)\
 MATCH (x32)-[:A]->(x33)\
 MATCH (x33)-[:A]->(x34)\
 MATCH (x34)-[:A]->(x35)\
 MATCH (x35)-[:A]->(x36)\
 MATCH (x36)-[:A]->(x37)\
 MATCH (x37)-[:A]->(x38)\
 MATCH (x38)-[:A]->(x39)\
 MATCH (x39)-[:A]->(x40)\
 MATCH (x40)-[:A]->(x41)\
 MATCH (x41)-[:A]->(x42)\
 MATCH (x42)-[:A]->(x43)\
 MATCH (x43)-[:A]->(x44)\
 MATCH (x44)-[:A]->(x45)\
 MATCH (x45)-[:A]->(x46)\
 MATCH (x46)-[:A]->(x47)\
 MATCH (x47)-[:A]->(x48)\
 MATCH (x48)-[:A]->(x49)\
 MATCH (x49)-[:A]->(x50)\
 MATCH (x50)-[:A]->(x51)\
 MATCH (x51)-[:A]->(x52)\
 MATCH (x52)-[:A]->(x53)\
 MATCH (x53)-[:A]->(x54)\
 MATCH (x54)-[:A]->(x55)\
 MATCH (x55)-[:A]->(x56)\
 MATCH (x56)-[:A]->(x57)\
 MATCH (x57)-[:A]->(x58)\
 MATCH (x58)-[:A]->(x59)\
 MATCH (x59)-[:A]->(x60)\
 MATCH (x60)-[:A]->(x61)\
 MATCH (x61)-[:A]->(x62)\
 MATCH (x62)-[:A]->(x63)\
 MATCH (x63)-[:A]->(x64)\
 MATCH (x64)-[:A]->(x65)\
 MATCH (x65)-[:A]->(x66)\
 MATCH (x66)-[:A]->(x67)\
 MATCH (x67)-[:A]->(x68)\
 MATCH (x68)-[:A]->(x69)\
 MATCH (x69)-[:A]->(x60)\
 MATCH (x70)-[:A]->(x71)\
 MATCH (x71)-[:A]->(x72)\
 MATCH (x72)-[:A]->(x73)\
 MATCH (x73)-[:A]->(x74)\
 MATCH (x74)-[:A]->(x75)\
 MATCH (x75)-[:A]->(x76)\
 MATCH (x76)-[:A]->(x77)\
 MATCH (x77)-[:A]->(x78)\
 MATCH (x78)-[:A]->(x79)\
 MATCH (x79)-[:A]->(x80)\
 MATCH (x80)-[:A]->(x81)\
 MATCH (x81)-[:A]->(x82)\
 MATCH (x82)-[:A]->(x83)\
 MATCH (x83)-[:A]->(x84)\
 MATCH (x84)-[:A]->(x85)\
 MATCH (x85)-[:A]->(x86)\
 MATCH (x86)-[:A]->(x87)\
 MATCH (x87)-[:A]->(x88)\
 MATCH (x88)-[:A]->(x89)\
 MATCH (x89)-[:A]->(x90)\
 MATCH (x90)-[:A]->(x91)\
 MATCH (x91)-[:A]->(x92)\
 MATCH (x92)-[:A]->(x93)\
 MATCH (x93)-[:A]->(x94)\
 MATCH (x94)-[:A]->(x95)\
 MATCH (x95)-[:A]->(x96)\
 MATCH (x96)-[:A]->(x97)\
 MATCH (x97)-[:A]->(x98)\
 MATCH (x98)-[:A]->(x99)\
 MATCH (x99)-[:A]->(x100)\
 RETURN * LIMIT 1;',
]
