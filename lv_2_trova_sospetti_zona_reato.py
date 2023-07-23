def trova_sospetti_zona_reato(driver):
    data = input("Inserisci la data (YYYY-MM-DD): ")
    orario = input("Inserisci l'orario (HH:MM:SS): ")
    nome_cella = input("Inserisci il nome della cella di reato: ")
    
    with driver.session() as session:
        result = session.run(
        """
        MATCH (zona:Cella {{nome: '{nome_zona}'}})
        MATCH (zona)<-[:Situata]-(cella:Cella)<-[:Collegata]-(sim:Sim)<-[:Possiede]-(persona:Persona)
        WHERE datetime('{data}T{orario}') >= cella.data_inizio_collegamento AND
              datetime('{data}T{orario}') <= cella.data_fine_collegamento
        RETURN DISTINCT persona
            """
        )
        
        # Lista per salvare le persone sospette nella zona di reato
        sospetti_zona_reato = []
        
        # Itera sui record restituiti dalla query
        for record in result:
            # Accedi al nodo "Persona" dal record
            persona_node = record["persona"]
            # Accedi agli attributi "nome" e "cognome" del nodo "Persona"
            nome_persona = persona_node["nome"]
            cognome_persona = persona_node["cognome"]
            # Aggiungi il nome e cognome della persona alla lista dei sospetti
            sospetti_zona_reato.append((nome_persona, cognome_persona))
        
        # Stampa i sospetti nella zona di reato
        print(f"Sospetti nella cella {nome_cella} il {data} alle {orario}: {sospetti_zona_reato}")
