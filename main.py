from db_connector import connect_to_db
from localizza_persona_sospetta import localizza_persona_sospetta
from trova_sospetti_zona_reato import trova_sospetti_zona_reato
from localizza_persone_sospette_in_raggio import localizza_persone_sospette_in_raggio

def main():
    driver = connect_to_db()
    
    while True:
        print("\nMenu:")
        print("1. Localizzare una persona sospetta")
        print("2. Trovare sospetti in una zona di reato")
        print("3. Localizzare persone sospette in un raggio dalle coordinate geografiche")
        print("4. Esci")
        
        scelta = input("Seleziona un'opzione: ")
        
        if scelta == "1":
            localizza_persona_sospetta(driver)
        elif scelta == "2":
            trova_sospetti_zona_reato(driver)
        elif scelta == "3":
            localizza_persone_sospette_in_raggio(driver)
        elif scelta == "4":
            print("Uscendo dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")

    driver.close()

if __name__ == "__main__":
    main()
