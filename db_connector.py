from neo4j import GraphDatabase

def connect_to_db():
    DATABASE_URL = "neo4j+s://7a8887c9.databases.neo4j.io"
    USERNAME = "neo4j"
    PASSWORD = "44MhzQ4SUShStF5KDmY6VJXg87MmPPT087FCF_6lkGc"
    return GraphDatabase.driver(DATABASE_URL, auth=(USERNAME, PASSWORD))
