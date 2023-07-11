# Controllo Presenza - Applicazione per la Polizia Postale

Questa è un'applicazione sviluppata in Python per la Polizia Postale che consente di determinare se una persona era presente in un determinato luogo in un intervallo di date. L'applicazione controlla se uno dei telefoni di proprietà di quella persona si è collegato ad una cella telefonica.

## Obiettivo

L'obiettivo principale dell'applicazione è quello di fornire alla Polizia Postale gli strumenti necessari per localizzare una persona sospetta. L'applicazione offre i seguenti livelli di funzionalità:

### Livello 1 - Localizzare una persona sospetta

Con una data, un orario e il nome di una persona, l'applicazione elenca le celle telefoniche alle quali le SIM intestate a quella persona erano collegate.

### Livello 2 - Trovare sospetti in una zona di reato

Con una data, un orario e il codice identificativo di una cella telefonica, l'applicazione elenca le persone intestatarie delle SIM collegate a quella cella in quel momento.

### Livello 3 - Trovare sospetti in un raggio geografico

Con le coordinate geografiche, una data, un orario e un raggio specificato, l'applicazione elenca le persone intestatarie delle SIM collegate alle celle telefoniche che si trovano entro quel raggio dalle coordinate fornite.

## Requisiti

- Python 3.10 installato sul sistema.
- Librerie presenti nei file python
- Accesso a un database neo4j con lo stesso formato dei dati d'esempio
