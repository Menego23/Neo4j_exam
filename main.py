# main.py
import db_functions as db
import GUI

# Configurazione del database Neo4j
USERNAME = "neo4j"
PASSWORD = "44MhzQ4SUShStF5KDmY6VJXg87MmPPT087FCF_6lkGc"
DATABASE_URL = "neo4j+s://7a8887c9.databases.neo4j.io"
def main():
    db_conn = db.connect_to_database(USERNAME, PASSWORD, DATABASE_URL)

    while True:
        input_data = GUI.menu()
        scelta = input_data[0]
        date_time = input_data[1]

        if scelta == '1':
            nome = input_data[2]
            result = db.find_suspect_by_name_datetime(db_conn, nome, date_time)
            print("Celle telefoniche collegate a una persona tramite SIM e data:")
            print(result)

        elif scelta == '2':
            cella = input_data[2]
            result = db.find_suspect_by_cell(db_conn, cella, date_time)
            print("Persone intestatarie delle SIM collegate a una cella e data:")
            print(result)

        elif scelta == '3':
            latitudine, longitudine, raggio = input_data[2]
            result = db.find_suspect_by_location(db_conn, latitudine, longitudine, raggio, date_time[0], date_time[1])
            print("Persone intestatarie delle SIM collegate a celle in un raggio da coordinate e data:")
            print(result)

        else:
            print("Opzione non valida")

        again = input("Vuoi effettuare un'altra ricerca? (S/N): ")
        if again.lower() != 's':
            break

    db.close_connection(db_conn)

if __name__ == "__main__":
    main()
