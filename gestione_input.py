from neo4j import GraphDatabase

debug = True

# Le funzioni di gestione degli input devono ritornare queste strinhe di esempio:
def find_suspect_by_name_datetime(nome, datetime):
    # datetime deve essere una stringa nel formato "YYYY-MM-DD HH:MM:SS"
    # Con una data, un orario e una persona, 
    # elencare le celle telefoniche alle quali le SIM intestate a quella persona erano collegate.
    QUERY_FIND_SUSPECT = f"""
    MATCH (p:Persona {{nome: "{nome}"}})-[:Collegata]->(cella:Cella)
    WHERE '{datetime}' <= cella.Inizio_collegamento <= '{datetime}'
    RETURN DISTINCT cella.id AS id, cella.latitudine AS latitudine, cella.longitudine AS longitudine
    """
    return QUERY_FIND_SUSPECT

def find_suspect_by_cell(cella_id, datetime):
    # Con una data, un orario ed una cella, 
    # elencare le persone intestatarie selle SIM collegate a quella cella in quel momento
    QUERY_FIND_SIM_BY_CELL_AND_TIME = f"""
    MATCH (p:Persona)-[:Collegata]->(cella:Cella {{id: {cella_id}}})
    WHERE '{datetime}' <= cella.Inizio_collegamento <= '{datetime}'
    RETURN DISTINCT p.nome AS nome, p.cognome AS cognome, p.Sim AS sim
    """

    return QUERY_FIND_SIM_BY_CELL_AND_TIME

def find_suspect_by_location(latitudine, longitudine, raggio, datetime):
    #  Date delle coordinate geografiche, una data e un orario ed un raggio,
    #  elencare le persone intestatarie delle SIM collegate alle celle che si trovano
    #  in un certo raggio dalle coordinate date
    QUERY_FIND_SUSPECT_BY_LOCATION = f"""
    MATCH (p:Persona)-[:Collegata]->(cella:Cella)
    WHERE distance(point({{"latitude": "{latitudine}", "longitude": "{longitudine}"}}), point({{"latitude": cella.latitudine, "longitude": cella.longitudine}})) <= {raggio}
    AND '{datetime}' <= cella.Inizio_collegamento <= '{datetime}'
    RETURN DISTINCT p.nome AS nome, p.cognome AS cognome, p.Sim AS sim
    """

    return QUERY_FIND_SUSPECT_BY_LOCATION
# Test nuove funzioni
if __name__ == "__main__":
    if debug:
        print("debug: gestione_input.py")
        try:
            #definisco le credenziali di accesso al database neo4j
            USERNAME = "neo4j"
            PASSWORD = "44MhzQ4SUShStF5KDmY6VJXg87MmPPT087FCF_6lkGc"
            DATABASE_URL = "neo4j+s://7a8887c9.databases.neo4j.io"
            #definisco la connessione al database neo4j
            conn = GraphDatabase.driver(DATABASE_URL, auth=(USERNAME, PASSWORD))
            print("Connessione al database avvenuta con successo")
            #stampo le info del db
            with conn.session() as session:
                print("Testing query 0")
                result = session.run("CALL dbms.components()")
                for record in result:
                    print(record)
                #stampo le tabelle e il numero di record
                result = session.run("CALL db.schema.visualization()")
                for record in result:
                    print(record)
                print("__________________\n__________________\n__________________")
            print("Testing query 1")
            print(find_suspect_by_name_datetime("Mario", "2021-01-01 00:00:00"))
            #eseguo la query
            with conn.session() as session:
                result = session.run(find_suspect_by_name_datetime("Sabrina", "2023-07-11 12:35:15"))
                print(result.values())
                for record in result:
                    print(record)
            print("Testing query 2")
            print(find_suspect_by_cell(1, "2021-01-01 00:00:00"))
            print("Testing query 3")
            print(find_suspect_by_location(45.0, 9.0, 1000, "2021-01-01 00:00:00"))
            conn.close()
            print("bye bye :)")
            exit()

        except Exception as e:
            print("Errore nella connessione al database")
            print(e)
            exit()
            
    else:
        print("Orrore: file non eseguibile  >:(")

        


