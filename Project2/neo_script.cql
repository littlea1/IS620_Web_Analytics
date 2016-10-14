// Neo4j build script
// Builds neo4j database from local files

LOAD CSV WITH HEADERS FROM "file:/actor_nodes.csv" as node
CREATE (actor: Actor { name:node.actor_id, type: "actor" });

LOAD CSV WITH HEADERS FROM "file:/movie_nodes.csv" as node 
CREATE (movie: Movie { name:node.movie_id, type: "movie" });


LOAD CSV WITH HEADERS FROM "file:/actor_el.csv" as edge
MATCH (actor1: Actor {name:edge.src }), (actor2: Actor {name: edge.trgt })
CREATE (actor1)-[:AFFILIATED]-(actor2);

LOAD CSV WITH HEADERS FROM "file:/movie_el.csv" as edge
MATCH (movie1: Movie {name:edge.src }), (movie2: Movie {name: edge.trgt })
CREATE (movie1)-[:SIMILIAR_CAST]->(movie2);

// ego graph build script

LOAD CSV WITH HEADERS FROM "file:/ego_nodes.csv" as node
CREATE (n:EGO { name:node.node_id, type:node.node_type});

MATCH (n {type:'actor'})
SET n :Actor_Ego;

MATCH (n {type:'movie'})
SET n :Movie_Ego;

LOAD CSV WITH HEADERS FROM "file:/ego_el.csv" as edge
MATCH (n:EGO {name:edge.src}), (m:EGO{name: edge.trgt})
CREATE (n)-[:IN]->(m);






