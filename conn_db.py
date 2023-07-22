from neo4j import GraphDatabase, basic_auth

# Definizione delle query Cypher
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

QUERY_FIND_SIM_BY_CELL_AND_TIME = """
MATCH (p:Persona)-[:Collegata]->(cella:Cella {id: $cella_id})
WHERE $inizio <= cella.Inizio_collegamento <= $fine
RETURN DISTINCT p.nome AS nome, p.cognome AS cognome, p.Sim AS sim
"""


class DatabaseConnector:
    def __init__(self, username, password, url):
        self.driver = GraphDatabase.driver(url, auth=basic_auth(username, password))

    def close(self):
        self.driver.close()

    def find_suspect(self, name):
        with self.driver.session() as session:
            result = session.run(QUERY_FIND_SUSPECT, nome=name)
            return [record["cella_id"] for record in result]

    def find_suspect_by_location(self, latitude, longitude, radius, start_date, end_date):
        with self.driver.session() as session:
            result = session.run(
                QUERY_FIND_SUSPECT_BY_LOCATION,
                latitudine=latitude,
                longitudine=longitude,
                raggio=radius,
                inizio=start_date,
                fine=end_date,
            )
            return list(result)

    def find_suspect_by_name_datetime(self, nome, datetime):
        with self.driver.session() as session:
            result = session.run(
                QUERY_FIND_SIM_BY_CELL_AND_TIME,
                cella_id=self.find_suspect(nome),
                inizio=datetime[0],
                fine=datetime[1],
            )
            return list(result)
