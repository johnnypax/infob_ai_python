import spacy

# Natural Language Processor
nlp = spacy.load("it_core_news_lg")

frase_uno = "Giovanni legge per ore"
frase_due = "Tu leggi per diventare sapiente"

estrazione_uno = nlp(frase_uno)
estrazione_due = nlp(frase_due)

for token in estrazione_uno:
    print(f"{token.text} -> Lemma: {token.lemma_}")

for token in estrazione_due:
    print(f"{token.text} -> Lemma: {token.lemma_}")