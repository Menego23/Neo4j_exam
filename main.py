from db_connector import connect_to_db
from lv_1_localizza_persona_sospetta import localizza_persona_sospetta
from lv_2_trova_sospetti_zona_reato import trova_sospetti_zona_reato
from lv_3_localizza_persone_sospette_in_raggio import trova_persone_intestatarie_cella_in_raggio

def print_menu():
    print("\n")
    print("╔══════════════════════════════════════════════╗")
    print("║                 Menu Principale              ║")
    print("╟──────────────────────────────────────────────╢")
    print("║ 1. Localizzare una persona sospetta          ║")
    print("║ 2. Trovare sospetti in una zona di reato     ║")
    print("║ 3. Localizzare persone sospette in un raggio ║")
    print("║ 4. Esci                                      ║")
    print("╚══════════════════════════════════════════════╝")

def main():
    driver = connect_to_db()
    
    while True:
        print_menu()
        
        scelta = input("\nSeleziona un'opzione: ")
        
        if scelta == "1":
            print("\nLocalizzazione Persona Sospetta")
            localizza_persona_sospetta(driver)
        elif scelta == "2":
            print("\nTrova Sospetti in Zona di Reato")
            trova_sospetti_zona_reato(driver)
        elif scelta == "3":
            print("\nLocalizza Persone Sospette in Raggio")
            trova_persone_intestatarie_cella_in_raggio(driver)
        elif scelta == "4":
            print("Uscendo dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")

    driver.close()

if __name__ == "__main__":
    main()
