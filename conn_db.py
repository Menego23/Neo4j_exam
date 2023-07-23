# conn_db.py
from neo4j import GraphDatabase, basic_auth
# Configurazione del database Neo4j

USERNAME = "neo4j"
PASSWORD = "F30NRAbmU7MFUz8uxJqtgo0anUkku0eygfHUbMR8rDo"
DATABASE_URL = "neo4j+s://548ca5cd.databases.neo4j.io"

class DatabaseConnector:
    def __init__(self, USERNAME, PASSWORD, DATABASE_URL):
        self.driver = GraphDatabase.driver(DATABASE_URL, auth=basic_auth(USERNAME, PASSWORD))

    def close(self):
        self.driver.close()
