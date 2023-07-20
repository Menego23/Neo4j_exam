# Funzioni di gestione degli input

# Configurazione del database Neo4j
USERNAME = "neo4j"
PASSWORD = "oAcFTwdlvOYd4LOHfzSAx6_jv8umS-S_1E5g1HbYKn4"
DATABASE_URL = "neo4j+s://3d212299.databases.neo4j.io"

# Le funzioni di gestione degli input devono ritornare queste strinhe di esempio:
QUERY_FIND_SUSPECT = """
MATCH (p:Persona {nome: $nome})
MATCH (p)-[:Collegata]->(cella:Cella)
RETURN cella.id AS cella_id
"""

QUERY_FIND_SUSPECT_BY_LOCATION = """
MATCH (p:Persona)-[:Collegata]->(cella:Cella)
WHERE distance(point({latitude: $latitudine, longitude: $longitudine}), point({latitude: cella.latitudine, longitude: cella.longitudine})) <= $raggio
AND $inizio <= cella.Inizio_collegamento <= $fine
RETURN DISTINCT p.nome AS nome, p.cognome AS cognome, p.Sim AS sim
"""

QUERY_FIND_SIM_BY_CELL_AND_TIME = f"""
MATCH (p:Persona)-[:Collegata]->(cella:Cella {{id: {cella_id}})
WHERE $inizio <= cella.Inizio_collegamento <= $fine
RETURN DISTINCT p.nome AS nome, p.cognome AS cognome, p.Sim AS sim
"""

# Test nuove funzioni
if __name__ == "__main__":
    pass
