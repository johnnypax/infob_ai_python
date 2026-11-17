import spacy

nlp = spacy.load("it_core_news_lg")
frase = "Mario mangia la mela mentre il gatto lo guarda."
# frase = input("Inserisci la frase")

estrazione = nlp(frase)
stack_sostantivi = []

for token in estrazione:
    if token.pos_ == "NOUN" or token.pos_ == "PROPN":
        stack_sostantivi.append(token.text)

print(stack_sostantivi)
