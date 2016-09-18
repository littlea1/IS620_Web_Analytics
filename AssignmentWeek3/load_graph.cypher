LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/bsnacks000/IS620_Web_Analytics/master/AssignmentWeek3/vertices.csv"   AS nodes  
CREATE (usr: User {id:nodes.Id, out_degree:nodes.out_degree, in_degree:nodes.in_degree, pagerank:nodes.pagerank});

LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/bsnacks000/IS620_Web_Analytics/master/AssignmentWeek3/edges.csv" AS edges 
MATCH (a: User {id:edges.Source}) 
MATCH (b: User {id:edges.Target}) 
CREATE (a)-[:VOTED_FOR]-> (b);

MATCH(n)-[r]->(m) WHERE n.name = "3" return n,r,m

MATCH(n)<-[r]-(m) WHERE n.name = "3" AND m.pagerank > 0.35 RETURN n,r,m
