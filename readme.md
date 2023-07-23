# Descrizione del Progetto
Il progetto della Polizia Postale mira a localizzare persone sospette utilizzando le informazioni di collegamento delle celle telefoniche. Il sistema utilizza un database Neo4j per gestire i dati riguardanti telefoni, persone, celle e luoghi.

## Collaboratori
- Gianluca Meneghetti
- Stefano Bonfanti
- Giulio Nocco
- Gabriele Laguna

## Obiettivo
L'obiettivo principale del progetto è identificare se una persona sospetta era presente in un determinato luogo in un intervallo di date. Ciò viene fatto controllando se uno dei telefoni di proprietà di quella persona si è collegato a una cella telefonica in quella zona durante il periodo specificato.

## Requisiti Funzionali
Il progetto si articola in tre livelli di funzionalità:

### Livello 1 - Localizzare una persona sospetta
In questo livello, l'utente può fornire una data, un orario e il nome di una persona sospetta. Il sistema effettuerà una ricerca nel database per verificare a quali celle telefoniche le SIM intestate a quella persona erano collegate in quel momento specifico. Le celle telefoniche risultanti verranno visualizzate all'utente.

### Livello 2 - Trovare sospetti in una zona di reato
In questo livello, l'utente può fornire una data, un orario e il nome di una cella telefonica specifica. Il sistema cercherà nel database le persone intestatarie delle SIM collegate a quella cella nel momento specificato. I dettagli delle persone trovate, come il nome e il numero di telefono, verranno restituiti all'utente.

### Livello 3 - Localizzare persone sospette in un raggio
In questo livello, l'utente dovrà fornire le coordinate geografiche di un luogo, una data e un orario. Il sistema verificherà le celle telefoniche collegate alle persone nei dintorni di quel luogo (raggio di 1000 metri). Le informazioni sulle persone trovate, come il nome e il numero di telefono, verranno mostrate all'utente.

## Configurazione e Utilizzo
Prima di eseguire il progetto, è necessario configurare le credenziali per il database Neo4j nel file `db_connector.py`.

Una volta configurato correttamente, l'utente può eseguire il file `main.py` per avviare l'applicazione. Verrà visualizzato un menu principale con le opzioni disponibili. L'utente può selezionare l'opzione desiderata e seguire le istruzioni per fornire i dati richiesti.

In alternativa si può configurare il proprio db e fare la query direttamente da Neo4j usando il file creation_db.cypher

## Esempi di Utilizzo
- **Localizzazione Persona Sospetta**
  L'utente può inserire la data "2023-07-12", l'orario "08:30:00" e il nome "Mario". Il sistema restituirà le celle telefoniche a cui la SIM intestata a Mario era collegata a quell'orario specifico.

- **Trova Sospetti in Zona di Reato**
  L'utente può inserire la data "2023-07-14", l'orario "15:30:00" e il nome della cella "cella_3". Il sistema restituirà le persone intestatarie delle SIM collegate a quella cella all'orario specificato.

- **Localizza Persone Sospette in un Raggio**
  L'utente può inserire le coordinate geografiche "45.4700" e "9.1800", la data "2023-07-15" e l'orario "10:00:00". Il sistema restituirà le persone che avevano le SIM collegate a celle telefoniche entro un raggio di 1000 metri da quelle coordinate.
