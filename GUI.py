from datetime import datetime

def menu():
    while True:
        scelta = input("1. Con una data, un orario e una persona, elencare le celle telefoniche alle quali le SIM intestate a quella persona erano collegate.\n"
                        "2. Con una data, un orario ed una cella, elencare le persone intestatarie selle SIM collegate a quella cella in quel momento\n"
                        "3. Date delle coordinate geografiche, una data e un orario elencare le persone intestatarie delle SIM collegate alle celle che si trovano in un certo raggio dalle coordinate date\n")
        try:
            if int(scelta) in range(1, 4):
                break
            else:
                raise ValueError
        except ValueError:
            print("Scelta non valida")

    while True:
        data_input = input("Inserisci data (YYYY-MM-DD): ")
        orario_input = input("Inserisci orario (HH:MM:SS): ")

        # Verifica se la data e l'orario inseriti sono nel formato corretto
        try:
            date_time_inizio = datetime.strptime(data_input + " " + orario_input, "%Y-%m-%d %H:%M:%S")
            break
        except ValueError:
            print("Data o orario non validi. Assicurati di inserire una data nel formato corretto (YYYY-MM-DD) e un orario nel formato corretto (HH:MM:SS).")

    # L'utente può inserire una data di fine (data_input2) diversa dalla data di inizio (data_input)
    data_input2 = input("Inserisci data di fine (YYYY-MM-DD) o lascia vuoto per la stessa data di inizio: ")
    if not data_input2:
        data_input2 = data_input

    # Converte le date di inizio e fine in formati di stringa adeguati per l'esecuzione delle query
    date_time_inizio = date_time_inizio.strftime("%Y-%m-%dT%H:%M:%S")
    date_time_fine = datetime.strptime(data_input2 + " " + orario_input, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")

    date_time = [date_time_inizio, date_time_fine]

    match scelta:
        case '1':
            nome = input("Inserisci nome persona: ")
            return scelta, date_time, nome

        case '2':
            cell = input("Inserisci cella: ")
            return scelta, date_time, cell

        case '3':
            latitudine = input("Inserisci latitudine: ")
            longitudine = input("Inserisci longitudine: ")
            raggio = input("Inserisci raggio: ")
            coord = [latitudine, longitudine, raggio]
            return scelta, date_time, coord

        case _:
            print("Scelta non valida")


# Test nuove funzioni
if __name__ == "__main__":
    print(menu())
