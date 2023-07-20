# import conn_db
# import gestione_input
import GUI

# Configurazione del database Neo4j
USERNAME = "neo4j"
PASSWORD = "oAcFTwdlvOYd4LOHfzSAx6_jv8umS-S_1E5g1HbYKn4"
DATABASE_URL = "neo4j+s://3d212299.databases.neo4j.io"

input = GUI.menu()
date_time = input[1]

match input[0]:
    case '1':
        nome = input[2]
        print(nome)
    case '2':
        cell = input[2]
        print(cell)
    case '3':
        coord = input[2]
        print(coord)

