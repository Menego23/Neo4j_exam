# file lv_2_trova_sospetti_zona_reato.py

def trova_sospetti_zona_reato(driver):
    data = input("Inserisci la data (YYYY-MM-DD): ")
    orario = input("Inserisci l'orario (HH:MM:SS): ")
    nome_cella = input("Inserisci il nome della cella: ")
    
    # Query Cypher per elencare le persone intestatarie delle SIM collegate alla cella in quel momento
    query = f"""
        MATCH (cella:Cella {{nome: '{nome_cella}'}})
        MATCH (persona:Persona)-[:Possiede]->(sim:Sim)-[collegata:Collegata]->(cella)
        WHERE datetime('{data}T{orario}') >= collegata.data_inizio_collegamento AND
              datetime('{data}T{orario}') <= collegata.data_fine_collegamento
        RETURN DISTINCT persona.nome AS nome_persona, sim.numero AS numero_sim
    """
    
    with driver.session() as session:
        result = session.run(query)
        
        # Lista per salvare le persone intestatarie delle SIM collegate alla cella
        persone_intestatarie = []
        
        # Itera sui record restituiti dalla query
        for record in result:
            # Accedi al nome della persona dal record
            nome_persona = record["nome_persona"]
            # Accedi al numero della SIM dal record
            numero_sim = record["numero_sim"]
            # Aggiungi il nome della persona e il numero della SIM alla lista delle persone intestatarie
            persone_intestatarie.append((nome_persona, numero_sim))
        
        # Stampa le persone intestatarie delle SIM collegate alla cella
        print(f"Persone intestatarie delle SIM collegate alla cella {nome_cella} il {data} alle {orario}:")
        for persona, sim in persone_intestatarie:
            print(f"Nome Persona: {persona}, Numero SIM: {sim}")


