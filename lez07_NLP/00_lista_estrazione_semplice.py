import spacy

# Natural Language Processor
nlp = spacy.load("it_core_news_sm")

frase = "Giovanni Pace, docente di Informatica, è appassionato di Droni e dell'intero cosmo! Ha due gatti, uno si chiama 'Pippi' e l'altra 'Bu' 😊😍🤣"

estrazione = nlp(frase)

# print("Tipo di 'frase': ", type(frase))
# print("Tipo di 'estrazione': ", type(estrazione))

# for token in estrazione:
#     print(token)

for token in estrazione:
    print(f"{token.text} -> Lemma: {token.lemma_} -> {token.pos_} -> {token.dep_}")

