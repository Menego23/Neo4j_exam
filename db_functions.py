# db_functions.py
from neo4j import GraphDatabase, basic_auth

USERNAME = "neo4j"
PASSWORD = "F30NRAbmU7MFUz8uxJqtgo0anUkku0eygfHUbMR8rDo"
DATABASE_URL = "neo4j+s://548ca5cd.databases.neo4j.io"

def connect_to_database(USERNAME, PASSWORD, DATABASE_URL):
    return GraphDatabase.driver(DATABASE_URL, auth=basic_auth(USERNAME, PASSWORD))

def close_connection(driver):
    driver.close()

def find_suspect(driver, name):
    # Implement the logic to find suspects by name using the driver session
    with driver.session() as session:
        result = session.run(
            """
            MATCH (p:Persona {nome: $nome})
            MATCH (p)-[:Collegata]->(cella:Cella)
            RETURN cella.id AS cella_id
            """,
            nome=name
        )
        return [record["cella_id"] for record in result]

def find_suspect_by_location(driver, latitude, longitude, radius, start_date, end_date):
    # Implement the logic to find suspects by location and datetime using the driver session
    with driver.session() as session:
        result = session.run(
            """
            MATCH (p:Persona)-[:Collegata]->(cella:Cella)
            WHERE distance(point({latitude: $latitudine, longitude: $longitudine}), point({latitude: cella.latitudine, longitude: cella.longitudine})) <= $raggio
            AND $inizio <= cella.Inizio_collegamento <= $fine
            RETURN DISTINCT p.nome AS nome, p.cognome AS cognome, p.Sim AS sim
            """,
            latitudine=latitude,
            longitudine=longitude,
            raggio=radius,
            inizio=start_date,
            fine=end_date,
        )
        return list(result)

def find_suspect_by_name_datetime(driver, nome, datetime):
    cella_id = find_suspect(driver, nome)
    with driver.session() as session:
        result = session.run(
            """
            MATCH (p:Persona)-[:Collegata]->(cella:Cella {id: $cella_id})
            WHERE $inizio <= cella.Inizio_collegamento <= $fine
            RETURN DISTINCT p.nome AS nome, p.cognome AS cognome, p.Sim AS sim
            """,
            cella_id=cella_id,
            inizio=datetime[0],
            fine=datetime[1],
        )
        return list(result)
