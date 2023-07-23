# file lv_1_localizza_persona_sospetta.py

def localizza_persona_sospetta(driver):
    data = input("Inserisci la data (YYYY-MM-DD): ")
    orario = input("Inserisci l'orario (HH:MM:SS): ")
    nome_persona = input("Inserisci il nome della persona sospetta: ")
    
    # Query Cypher per localizzare una persona sospetta
    query = f"""
        MATCH (p:Persona {{nome: '{nome_persona}'}})-[:Possiede]->(s:Sim)-[collegata:Collegata]->(c:Cella)
        WHERE datetime('{data}T{orario}') >= collegata.data_inizio_collegamento AND
              datetime('{data}T{orario}') <= collegata.data_fine_collegamento
        RETURN c
    """
    
    with driver.session() as session:
        result = session.run(query)
        
        # Lista per salvare le celle telefoniche collegate alla persona sospetta
        celle_collegate = []
        
        # Itera sui record restituiti dalla query
        for record in result:
            # Accedi al nodo "Cella" dal record
            cella_node = record["c"]
            # Accedi all'attributo "nome" del nodo "Cella"
            nome_cella = cella_node["nome"]
            # Aggiungi il nome della cella alla lista delle celle collegate
            celle_collegate.append(nome_cella)
        
        # Stampa le celle telefoniche collegate alla persona sospetta
        print(f"Celle telefoniche collegate a {nome_persona} il {data} alle {orario}: {celle_collegate}")
