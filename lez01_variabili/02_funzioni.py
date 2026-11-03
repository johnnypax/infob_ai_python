# richiesta = "Ho un PROBLEMA con la fattura"
# # richiesta = richiesta.lower()         # NO BUONO ;(
# # urgente -> alta, problema -> media,  tutti gli altri -> bassa

# if "urgente" in richiesta.lower():
#     priorita = "alta"
# elif "problema" in richiesta.lower():
#     priorita = "media"
# elif "errore" in richiesta.lower():
#     priorita = "attenzione"
# else:
#     priorita = "bassa"

# print(f"Priorità assegnata: {priorita}")

# ----------------------------- LISTE
# lista_canali = ["email", "telefono", "chat", 3, True, "😍"]
# lista_canali.append("Giovanni")

# # print(lista_canali)
# # print( len(lista_canali) )

# for canale in lista_canali:
#     print(f"Richiesta arrivata da: {canale}")

#########

# for i in range(7):
#     print("numero", i)

# -------------------------------
# Dato l'elenco delle ore di lezione [3,3,4,3,3] stampare in maniera
# automatica (con un ciclo) il totale delle ore

# ore = [3,3,4,3,3]
# somma = 0

# for o in ore:
#     somma += o

# print(somma)

# -------------------------- FUNZIONI

def calcola_priorita(testo):
    if "urgente" in testo.lower():
        return "alta"
    elif "problema" in testo.lower():
        return "media"
    elif "errore" in testo.lower():
        return "attenzione"
    else:
        return "bassa"

# print( calcola_priorita("URGENTE: server down") )
# print( calcola_priorita("Vorrei informazioni sul corso") )

assert calcola_priorita("Urgente!") == "alta"
assert calcola_priorita("ciao") == "bassa"
assert calcola_priorita("Giovanni") == "bassa"