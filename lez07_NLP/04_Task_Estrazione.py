# Prevedere un sistema che, data una pagina web (indirizzo), estrae il suo contenuto con una lista di soggetti e complementi oggetto.

# Tip: Beautiful Soup

# from bs4 import BeautifulSoup
import requests
import spacy
from bs4 import BeautifulSoup


nlp = spacy.load("it_core_news_sm")
indirizzo = "https://www.tiraccontounviaggio.it/cosa-vedere-a-pescara-in-mezza-giornata/"

response = requests.get(indirizzo)
pagina = BeautifulSoup(response.text, "html.parser")
testo = pagina.get_text()
# print(testo)

estrazione = nlp(testo)
soggetti = []

for token in estrazione:
    if token.dep_ == "nsubj" and token.head.dep_ == "ROOT":
        soggetti.append(token.text)

print(soggetti)
