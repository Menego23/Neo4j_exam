# file GUI.py
from datetime import datetime
USERNAME = "neo4j"
PASSWORD = "44MhzQ4SUShStF5KDmY6VJXg87MmPPT087FCF_6lkGc"
DATABASE_URL = "neo4j+s://7a8887c9.databases.neo4j.io"

def menu():
    print("╔══════════════════════════════╗")
    print("║   Benvenuto nel Menu         ║")
    print("╠═══════════════════════════════════════════════════════════════════════════════════════╗")
    print("║ 1. Celle telefoniche collegate a una persona tramite SIM e data                         ║")
    print("║ 2. Persone intestatarie delle SIM collegate a una cella e data                          ║")
    print("║ 3. Persone intestatarie delle SIM collegate a celle in un raggio da coordinate e data   ║")
    print("╚═══════════════════════════════════════════════════════════════════════════════════════╝")

    scelta = input("Inserisci il numero corrispondente all'opzione desiderata: ")
    while scelta not in ['1', '2', '3']:
        print("╔══════════════════════════════╗")
        print("║ Scelta non valida. Riprova.  ║")
        print("╚══════════════════════════════╝")
        scelta = input("Inserisci il numero corrispondente all'opzione desiderata: ")

    while True:
        data_input = input("Inserisci data (YYYY-MM-DD): ")
        orario_input = input("Inserisci orario (HH:MM:SS): ")

        # Verifica se la data e l'orario inseriti sono nel formato corretto
        try:
            date_time_inizio = datetime.strptime(data_input + " " + orario_input, "%Y-%m-%d %H:%M:%S")
            break
        except ValueError:
            print("╔══════════════════════════════╗")
            print("║ Data o orario non validi.    ║")
            print("║ Assicurati di inserire una   ║")
            print("║ data nel formato corretto    ║")
            print("║ (YYYY-MM-DD) e un orario     ║")
            print("║ nel formato corretto         ║")
            print("║ (HH:MM:SS).                  ║")
            print("╚══════════════════════════════╝")

    # L'utente può inserire una data di fine (data_input2) diversa dalla data di inizio (data_input)
    data_input2 = input("Inserisci data di fine (YYYY-MM-DD) o lascia vuoto per la stessa data di inizio: ")
    if not data_input2:
        data_input2 = data_input

    # Converte le date di inizio e fine in formati di stringa adeguati per l'esecuzione delle query
    date_time_inizio = date_time_inizio.strftime("%Y-%m-%dT%H:%M:%S")
    date_time_fine = datetime.strptime(data_input2 + " " + orario_input, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")

    date_time = [date_time_inizio, date_time_fine]

    if scelta == '1':
        nome = input("Inserisci nome persona: ")
        return scelta, date_time, nome

    elif scelta == '2':
        cell = input("Inserisci cella: ")
        return scelta, date_time, cell

    elif scelta == '3':
        latitudine = input("Inserisci latitudine: ")
        longitudine = input("Inserisci longitudine: ")
        raggio = input("Inserisci raggio: ")
        coord = [latitudine, longitudine, raggio]
        return scelta, date_time, coord

    else:
        print("╔══════════════════════════════╗")
        print("║ Scelta non valida.           ║")
        print("╚══════════════════════════════╝")
