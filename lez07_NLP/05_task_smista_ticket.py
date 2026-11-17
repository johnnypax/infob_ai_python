# Costruisci lo Smista-Ticket: un programma che legge i messaggi arrivati all'help desk della scuola e li assegna a una categoria (Tecnico, Amministrativo, Didattica o Altro) cercando parole chiave come "errore" o "computer"

# Cosa devi fare
# 1.  Crea un dizionario categorie con almeno 5 parole chiave per categoria, ad esempio # "Tecnico": ["computer", "errore", "stampante", "password", "wifi"].
# 2.  Analizza ogni messaggio con spaCy e prendi i lemmi (token.lemma_.lower()): così # "errori" diventa "errore" e "voti" diventa "voto".
# 3.  Conta quante parole chiave di ogni categoria compaiono nel messaggio: vince la # categoria con più punti. Se non trovi nessuna parola, la categoria è "Altro".
# 4.  Per ogni messaggio stampa la categoria e le parole chiave trovate.