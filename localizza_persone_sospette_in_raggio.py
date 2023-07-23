def localizza_persone_sospette_in_raggio(driver):
    data = input("Inserisci la data (YYYY-MM-DD): ")
    orario = input("Inserisci l'orario (HH:MM:SS): ")
    latitudine_data = float(input("Inserisci la latitudine delle coordinate geografiche: "))
    longitudine_data = float(input("Inserisci la longitudine delle coordinate geografiche: "))
    raggio = float(input("Inserisci il raggio in metri: "))
    
    with driver.session() as session:
        result = session.run(
            """
            // Query per localizzare persone sospette in un raggio dalle coordinate geografiche
            // ... (inserisci qui la query che hai definito in precedenza) ...
            """
        )
        
        # Lista per salvare le persone sospette nel raggio dalle coordinate geografiche
        persone_sospette = []
        
        # Itera sui record restituiti dalla query
        for record in result:
            # Accedi al nodo "Persona" dal record
            persona_node = record["persona"]
            # Accedi agli attributi "nome" e "cognome" del nodo "Persona"
            nome_persona = persona_node["nome"]
            cognome_persona = persona_node["cognome"]
            # Aggiungi il nome e cognome della persona alla lista delle persone sospette
            persone_sospette.append((nome_persona, cognome_persona))
        
        # Stampa le persone sospette nel raggio dalle coordinate geografiche
        print(f"Persone sospette entro {raggio} metri dalle coordinate ({latitudine_data}, {longitudine_data}): {persone_sospette}")
