def trova_persone_intestatarie_cella_in_raggio(driver, latitude, longitude, raggio, data, orario):
    with driver.session() as session:
        result = session.run(
            f"""
            MATCH (p:Persona)-[:Possiede]->(s:Sim)-[collegata:Collegata]->(c:Cella)-[:Situata]->(luogo:Luogo)
            WHERE point({{latitude: {latitude}, longitude: {longitude}}}).distance(point({{latitude: luogo.latitudine, longitude: luogo.longitudine}})) <= {raggio} * 1000 AND
                  datetime('{data}T{orario}') >= collegata.data_inizio_collegamento AND
                  datetime('{data}T{orario}') <= collegata.data_fine_collegamento
            RETURN DISTINCT p.nome
            """
        )
        
        # Lista per salvare i nomi delle persone intestatarie delle SIM
        persone_intestatarie = []
        
        # Itera sui record restituiti dalla query
        for record in result:
            # Accedi al valore "nome" dal record
            nome_persona = record["p.nome"]
            # Aggiungi il nome della persona alla lista delle persone intestatarie
            persone_intestatarie.append(nome_persona)
        
        # Stampa i nomi delle persone intestatarie delle SIM
        print(f"Persone intestatarie delle SIM collegate alla cella in raggio di {raggio} km dalle coordinate ({latitude}, {longitude}) al {data} alle {orario}: {persone_intestatarie}")
