// Crea i nodi "Sim"
CREATE (Sabrina_Sim:Sim {numero: '+39 574 159 8525'})
CREATE (Mario_Sim:Sim {numero: '+39 123 456 7890'})
CREATE (Laura_Sim:Sim {numero: '+39 987 654 3210'})
CREATE (Alfonso_Sim:Sim {numero: '+39 123 456 7890'})

// Crea i nodi "Cella"
CREATE (cella_1:Cella {nome: 'cella_1', id: 653487})
CREATE (cella_2:Cella {nome: 'cella_2', id: 123456})
CREATE (cella_3:Cella {nome: 'cella_3', id: 987654})
CREATE (cella_4:Cella {nome: 'cella_4', id: 123456})

// Crea i nodi "Persona"
CREATE (Sabrina:Persona {nome: 'Sabrina', cognome: 'Rossi'})
CREATE (Mario:Persona {nome: 'Mario', cognome: 'Bianchi'})
CREATE (Laura:Persona {nome: 'Laura', cognome: 'Verdi'})
CREATE (Alfonso:Persona {nome: 'Alfonso', cognome: 'Gialli'})

// Crea i nodi "Luogo" con coordinate fino a 4 cifre dopo il punto
CREATE (Banca_Mediolanum:Luogo {nome: 'Banca Mediolanum', latitudine: 45.4581, longitudine: 9.1775})
CREATE (Museo_del_Novecento:Luogo {nome: 'Museo del Novecento', latitudine: 45.4655, longitudine: 9.1897})
CREATE (Duomo_di_Milano:Luogo {nome: 'Duomo di Milano', latitudine: 45.4641, longitudine: 9.1919})
CREATE (Biassono:Luogo {nome: 'Biassono', latitudine: 45.6594, longitudine: 9.2883})

///////////////////////////////////////////////////////////////
// Crea le relazioni "Collegata" tra le Sim e le celle con attributi di inizio e fine collegamento (usando datetime)
CREATE (Sabrina_Sim)-[:Collegata {data_inizio_collegamento: datetime('2023-07-12T01:00:00'), data_fine_collegamento: datetime('2023-07-12T03:00:00')}]->(cella_1)
CREATE (Mario_Sim)-[:Collegata {data_inizio_collegamento: datetime('2023-07-13T16:00:00'), data_fine_collegamento: datetime('2023-07-17T08:00:00')}]->(cella_2)
CREATE (Laura_Sim)-[:Collegata {data_inizio_collegamento: datetime('2023-07-14T09:00:00'), data_fine_collegamento: datetime('2023-07-15T15:00:00')}]->(cella_3)
CREATE (Alfonso_Sim)-[:Collegata {data_inizio_collegamento: datetime('2023-07-08T00:00:00'), data_fine_collegamento: datetime('2023-07-08T23:00:00')}]->(cella_4)
CREATE (Sabrina_Sim)-[:Collegata {data_inizio_collegamento: datetime('2023-07-12T05:00:00'), data_fine_collegamento: datetime('2023-07-13T08:00:00')}]->(cella_4)
CREATE (Mario_Sim)-[:Collegata {data_inizio_collegamento: datetime('2023-07-17T08:00:00'), data_fine_collegamento: datetime('2023-07-20T16:00:00')}]->(cella_4)

///////////////////////////////////////////////////////////////
// Crea le relazioni "Appartenente" tra le persone e le Sim
CREATE (Sabrina)-[:Possiede]->(Sabrina_Sim)
CREATE (Mario)-[:Possiede]->(Mario_Sim)
CREATE (Laura)-[:Possiede]->(Laura_Sim)
CREATE (Alfonso)-[:Possiede]->(Alfonso_Sim)

///////////////////////////////////////////////////////////////
// Crea le relazioni "Situata" tra le celle e i luoghi
CREATE (cella_1)-[:Situata]->(Banca_Mediolanum)
CREATE (cella_2)-[:Situata]->(Museo_del_Novecento)
CREATE (cella_3)-[:Situata]->(Duomo_di_Milano)
CREATE (cella_4)-[:Situata]->(Biassono)
