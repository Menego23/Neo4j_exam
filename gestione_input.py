# File gestione_input.py

# Le funzioni di gestione degli input devono ritornare queste stringhe di esempio:
def find_suspect_by_name_datetime(nome, datetime):
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
