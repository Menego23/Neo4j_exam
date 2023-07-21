# main.py

import GUI
import conn_db
import gestione_input

# Configurazione del database Neo4j
USERNAME = "neo4j"
PASSWORD = "oAcFTwdlvOYd4LOHfzSAx6_jv8umS-S_1E5g1HbYKn4"
DATABASE_URL = "neo4j+s://3d212299.databases.neo4j.io"

def main():
    # Connessione al database Neo4j
    try:
        conn = conn_db.connessione_db(USERNAME, PASSWORD, DATABASE_URL)
        print("Connessione al database avvenuta con successo")
    except Exception as e:
        print("Errore nella connessione al database")
        print(e)
        return

    # Mostra il menu e ottieni l'input dell'utente
    input = GUI.menu()
    date_time = input[1]

    # Esegui la logica in base alla scelta dell'utente
    match input[0]:
        case '1':
            nome = input[2]
            # Esegui la query corrispondente
            result = gestione_input.find_suspect_by_name_datetime(nome, date_time)
            print(result)
        case '2':
            cell = input[2]
            # Esegui la query corrispondente
            result = gestione_input.find_suspect_by_cell(cell, date_time)
            print(result)
        case '3':
            coord = input[2]
            # Esegui la query corrispondente
            result = gestione_input.find_suspect_by_location(coord[0], coord[1], coord[2], date_time)
            print(result)
        case _:
            print("Scelta non valida")

    # Chiudi la connessione al database
    conn.close()

if __name__ == "__main__":
    main()
