# Costruisci lo Smista-Ticket: un programma che legge i messaggi arrivati all'help desk della scuola e li assegna a una categoria (Tecnico, Amministrativo, Didattica o Altro) cercando parole chiave come "errore" o "computer"

# Cosa devi fare
# 1.  Crea un dizionario categorie con almeno 5 parole chiave per categoria, ad esempio # "Tecnico": ["computer", "errore", "stampante", "password", "wifi"].
# 2.  Analizza ogni messaggio con spaCy e prendi i lemmi (token.lemma_.lower()): così # "errori" diventa "errore" e "voti" diventa "voto".
# 3.  Conta quante parole chiave di ogni categoria compaiono nel messaggio: vince la # categoria con più punti. Se non trovi nessuna parola, la categoria è "Altro".
# 4.  Per ogni messaggio stampa la categoria e le parole chiave trovate.

import spacy

# Punto 1
dic_categorie = {
    "Tecnico": ["computer", "errore", "stampante", "password", "wifi"],
    "Amministrativo": ["iscrizione", "pagamento", "certificato", "segreteria", "documento"],
    "Didattica": ["voto", "esame", "lezione", "compito", "professore"]
}

lista_messaggi = [
    "Il computer del laboratorio dà sempre errori e la stampante non funziona per seguire la lezione",
    "Ho dimenticato la password del wifi",
    "Quando devo fare il pagamento per l'iscrizione?",
    "Non vedo i voti della verifica di matematica",
    "Il professore ha caricato i compiti per domani?",
    "Mi serve un certificato dalla segreteria",
    "Buongiorno, a che ora apre la mensa?",
]

nlp = spacy.load('it_core_news_lg')

for messaggio in lista_messaggi:
    # punto 2
    estrazione = nlp(messaggio)

    lemmi = []
    for token in estrazione:
        lemmi.append(token.lemma_.lower())

    # print(messaggio)
    # print(lemmi)
    categoria_vinc = "Altro"
    punteggio_max = 0
    parole_vincenti = []

    for categoria in dic_categorie:
        parole_chiave = dic_categorie[categoria]
        parole_trovate = []

        for parola in parole_chiave:
            if parola in lemmi:
                parole_trovate.append(parola)

        # print(parole_trovate)
        punti = len(parole_trovate)
        if punti > punteggio_max:
            punteggio_max = punti
            categoria_vinc = categoria
            parole_vincenti = parole_trovate

    print(f"Messaggio: {messaggio}")
    print(f"Categoria: {categoria_vinc}")
    print(parole_vincenti)


