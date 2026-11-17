import spacy

# Natural Language Processor
nlp = spacy.load("it_core_news_sm")

frase = "Giovanni Pace, docente di Informatica, è appassionato di Droni!"

estrazione = nlp(frase)

# print("Tipo di 'frase': ", type(frase))
# print("Tipo di 'estrazione': ", type(estrazione))

for token in estrazione:
    print(token)