# Funzioni di gestione degli input

# Le funzioni di gestione degli input devono ritornare queste strinhe di esempio:
def find_suspect_by_name(nome):
    QUERY_FIND_SUSPECT = f"""
    MATCH (p:Persona {{nome: {nome}}})
    MATCH (p)-[:Collegata]->(cella:Cella)
    RETURN cella.id AS cella_id
    """
    return QUERY_FIND_SUSPECT

def find_suspect_by_location(latitudine, longitudine, raggio, inizio, fine):
    QUERY_FIND_SUSPECT_BY_LOCATION = f"""
    MATCH (p:Persona)-[:Collegata]->(cella:Cella)
    WHERE distance(point({{"latitude: "{latitudine}", longitude: "{longitudine}}}), point({{latitude: cella.latitudine, longitude: cella.longitudine}})) <= {raggio}
    AND {inizio} <= cella.Inizio_collegamento <= {fine}
    RETURN DISTINCT p.nome AS nome, p.cognome AS cognome, p.Sim AS sim
    """
    return QUERY_FIND_SUSPECT_BY_LOCATION

def find_suspect_by_cell(cella_id, inizio, fine):
    QUERY_FIND_SIM_BY_CELL_AND_TIME = f"""
    MATCH (p:Persona)-[:Collegata]->(cella:Cella {{id: {cella_id}}})
    WHERE {inizio} <= cella.Inizio_collegamento <= {fine}
    RETURN DISTINCT p.nome AS nome, p.cognome AS cognome, p.Sim AS sim
    """
    return QUERY_FIND_SIM_BY_CELL_AND_TIME

# Test nuove funzioni
if __name__ == "__main__":
    pass
