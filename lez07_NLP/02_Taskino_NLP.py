# Creare un sistema interattivo che, data una frase in input dall'utente, estrae Soggetto Verbo principale e complemento oggetto!
# Es. Mario mangia la mela mentre il gatto lo guarda.

import spacy

nlp = spacy.load("it_core_news_lg")

frase = "Mario mangia la mela mentre il gatto lo guarda."
# frase = input("Inserisci la frase")

estrazione = nlp(frase)

for parola in estrazione:
    # print(parola.text, parola.head, parola.head.dep_)
    if parola.dep_ == "nsubj" and parola.head.dep_ == "ROOT":
        print(f"Soggetto: {parola.text} - {parola.lemma_}")
    if parola.dep_ == "ROOT":
        print(f"Verbo: {parola.text} - {parola.lemma_}")
    if parola.dep_ == "obj" and parola.head.dep_ == "ROOT":
        print(f"Complemento Oggetto: {parola.text} - {parola.lemma_}")
