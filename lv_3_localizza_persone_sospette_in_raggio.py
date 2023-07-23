# file lv_3_localizza_persone_sospette_in_raggio.py

def trova_persone_intestatarie_cella_in_raggio(driver):
    latitudine = float(input("Inserisci la latitudine delle coordinate geografiche: "))
    longitudine = float(input("Inserisci la longitudine delle coordinate geografiche: "))
    data = input("Inserisci la data (YYYY-MM-DD): ")
    orario = input("Inserisci l'orario (HH:MM:SS): ")

    query = f"""
        MATCH (persona:Persona)-[:Possiede]->(sim:Sim)-[collegata:Collegata]->(cella:Cella)-[:Situata]->(luogo:Luogo)
        WHERE datetime('{data}T{orario}') >= collegata.data_inizio_collegamento AND
              datetime('{data}T{orario}') <= collegata.data_fine_collegamento AND
              6371000 * 2 * ASIN(SQRT(
                  SIN(RADIANS(luogo.latitudine - {latitudine}) / 2) * SIN(RADIANS(luogo.latitudine - {latitudine}) / 2) +
                  COS(RADIANS({latitudine})) * COS(RADIANS(luogo.latitudine)) *
                  SIN(RADIANS(luogo.longitudine - {longitudine}) / 2) * SIN(RADIANS(luogo.longitudine - {longitudine}) / 2)
              )) <= 1000
        RETURN DISTINCT persona.nome AS nome_persona, sim.numero AS numero_sim
    """

    with driver.session() as session:
        result = session.run(query)

        persone_in_raggio = []

        for record in result:
            nome_persona = record["nome_persona"]
            numero_sim = record["numero_sim"]
            persone_in_raggio.append((nome_persona, numero_sim))

        print(f"Persone nel raggio di 1000 metri dalle coordinate ({latitudine}, {longitudine}) "
              f"il {data} alle {orario}:")
        for persona, numero_sim in persone_in_raggio:
            print(f"Persona: {persona}, Numero SIM: {numero_sim}")
