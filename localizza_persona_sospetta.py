def trova_persone_intestatarie_cella_in_momento(driver, nome_persona, nome_cella, data, orario):
    with driver.session() as session:
        result = session.run(
            f"""
            MATCH (p:Persona {{nome: '{nome_persona}'}})-[:Possiede]->(s:Sim)-[collegata:Collegata]->(c:Cella {{nome: '{nome_cella}'}})
            WHERE datetime('{data}T{orario}') >= collegata.data_inizio_collegamento AND
                  datetime('{data}T{orario}') <= collegata.data_fine_collegamento
            RETURN p
            """
        )
        
        # Lista per salvare le persone intestatarie delle SIM
        persone_intestatarie = []
        
        # Itera sui record restituiti dalla query
        for record in result:
            # Accedi al nodo "Persona" dal record
            persona_node = record["p"]
            # Accedi all'attributo "nome" del nodo "Persona"
            nome_persona = persona_node["nome"]
            # Aggiungi il nome della persona alla lista delle persone intestatarie
            persone_intestatarie.append(nome_persona)
        
        # Stampa le persone intestatarie delle SIM
        print(f"Persone intestatarie delle SIM collegate alla cella {nome_cella} al {data} alle {orario}: {persone_intestatarie}")
