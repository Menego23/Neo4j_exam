# conn_db.py
from neo4j import GraphDatabase, basic_auth
# Configurazione del database Neo4j

USERNAME = "neo4j"
PASSWORD = "44MhzQ4SUShStF5KDmY6VJXg87MmPPT087FCF_6lkGc"
DATABASE_URL = "neo4j+s://7a8887c9.databases.neo4j.io"

class DatabaseConnector:
    def __init__(self, USERNAME, PASSWORD, DATABASE_URL):
        self.driver = GraphDatabase.driver(DATABASE_URL, auth=basic_auth(USERNAME, PASSWORD))

    def close(self):
        self.driver.close()
