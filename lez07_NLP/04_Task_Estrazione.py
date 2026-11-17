# Prevedere un sistema che, data una pagina web (indirizzo), estrae il suo contenuto con una lista di soggetti e complementi oggetto.

# Tip: Beautiful Soup

# from bs4 import BeautifulSoup
import requests
import spacy
import json
from bs4 import BeautifulSoup


nlp = spacy.load("it_core_news_sm")
indirizzo = "https://www.tiraccontounviaggio.it/cosa-vedere-a-pescara-in-mezza-giornata/"

response = requests.get(indirizzo)
pagina = BeautifulSoup(response.text, "html.parser")
testo = pagina.get_text()
# print(testo)

estrazione = nlp(testo)
soggetti = []

# Estrazione semplice
# for token in estrazione:
#     if token.dep_ == "nsubj" and token.head.dep_ == "ROOT":
#         soggetti.append(token.text)

for token in estrazione:
    if token.dep_ == "nsubj" and token.head.dep_ == "ROOT":
        soggetti.append(
            {
                "text": token.text,
                "pos": token.pos_,
                "dep": token.dep_,
                "lemma": token.lemma_,
                "root": token.head.dep_
            }
        )

# print(soggetti)
print( json.dumps(soggetti, indent=2) )
