from neo4j import GraphDatabase, basic_auth

# Configurazione del database Neo4j
USERNAME = "neo4j"
PASSWORD = "44MhzQ4SUShStF5KDmY6VJXg87MmPPT087FCF_6lkGc"
DATABASE_URL = "neo4j+s://7a8887c9.databases.neo4j.io"

def test_connection():
    try:
        print("Connecting to Neo4j database...")
        driver = GraphDatabase.driver(DATABASE_URL, auth=basic_auth(USERNAME, PASSWORD))
        print("Connected successfully. Running a test query...")
        with driver.session() as session:
            session.run("RETURN 1")
        print("Test query executed successfully. Connection to Neo4j database is successful.")
        driver.close()
        return True
    except Exception as e:
        print(f"Connection to Neo4j database failed: {e}")
        return False

if __name__ == "__main__":
    test_connection()
