import conn_db
import gestione_input
import GUI

# Configurazione del database Neo4j
USERNAME = "neo4j"
PASSWORD = "oAcFTwdlvOYd4LOHfzSAx6_jv8umS-S_1E5g1HbYKn4"
DATABASE_URL = "neo4j+s://3d212299.databases.neo4j.io"

def main():
    db_conn = conn_db.DatabaseConnector(USERNAME, PASSWORD, DATABASE_URL)

    while True:
        input_data = GUI.menu()
        scelta = input_data[0]
        date_time = input_data[1]

        if scelta == '1':
            nome = input_data[2]
            result = db_conn.find_suspect_by_name_datetime(nome, date_time)
            print("Celle telefoniche collegate a una persona tramite SIM e data:")
            print(result)

        elif scelta == '2':
            cella = input_data[2]
            result = db_conn.find_suspect_by_cell(cella, date_time)
            print("Persone intestatarie delle SIM collegate a una cella e data:")
            print(result)

        elif scelta == '3':
            latitudine, longitudine, raggio = input_data[2]
            result = db_conn.find_suspect_by_location(latitudine, longitudine, raggio, date_time)
            print("Persone intestatarie delle SIM collegate a celle in un raggio da coordinate e data:")
            print(result)

        else:
            print("Opzione non valida")

        again = input("Vuoi effettuare un'altra ricerca? (S/N): ")
        if again.lower() != 's':
            break

    db_conn.close()

if __name__ == "__main__":
    main()
