# Funzioni per printare in console la gui

def print_scelta():
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

    data = input("Inserisci data (YY-MM-GG): ")
    orario = input("Inserisci orario (HH:MM:SS): ")

    if data == "":
        data = "2021-01-01 2021-01-02"
    if orario == "":
        orario = "00:00:00 00:00:00"

    data = data.split(" ")
    orario = orario.split(" ")
    date_time_inizio = data[0] + "T" + orario[0]
    date_time_fine = data[1] + "T" + orario[1]
    date_time = [date_time_inizio, date_time_fine]

    match scelta:
        case '1':
            nome = input("Inserisci nome persona: ")
            return nome, date_time

        case '2':
            cell = input("Inserisci cella: ")
            return cell, date_time

        case '3':
            latitudine = input("Inserisci latitudine: ")
            longitudine = input("Inserisci longitudine: ")
            raggio = input("Inserisci raggio: ")
            coord = [latitudine, longitudine, raggio]
            return coord, date_time

        case _:
            print("Scelta non valida")


# Test nuove funzioni
if __name__ == "__main__":
    print(print_scelta())
