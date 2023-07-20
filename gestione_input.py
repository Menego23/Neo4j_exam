import conn_db

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
            PASSWORD = "oAcFTwdlvOYd4LOHfzSAx6_jv8umS-S_1E5g1HbYKn4"
            DATABASE_URL = "neo4j+s://3d212299.databases.neo4j.io"
            #definisco la connessione al database neo4j
            conn = conn_db.connessione_db(USERNAME, PASSWORD, DATABASE_URL)
        except Exception as e:
            print("Errore nella connessione al database")
            print(e)
            exit()
        finally:
            print("Connessione al database avvenuta con successo")
            print("Testing query 1")
            print(find_suspect_by_name_datetime("Mario", "2023-01-01 00:00:00"))
            print("Testing query 2")
            print(find_suspect_by_cell(1, "2021-01-01 00:00:00"))
            print("Testing query 3")
            print(find_suspect_by_location(45.0, 9.0, 1000, "2021-01-01 00:00:00"))

            print("bye bye :)")
            conn.close()
            exit()

    else:
        print("Orrore: file non eseguibile  >:(")

        


