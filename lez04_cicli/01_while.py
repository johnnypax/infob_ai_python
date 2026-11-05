# Mandate in output un menu che mi permette di scegliere tra 1 = saluta, 0 = esci.

# while True:
#     scelta = input("1 = saluta, 0 = esci").strip()
#     if scelta == "1":
#         nome = input("Dimmi qual'è il tuo nome")
#         print(f"Ciao: {nome}")
#     elif scelta == "0":
#         print("Arrivederci")
#         break
#     else:
#         print("Comando non riconosciuto")

while True:
    scelta = int(input("1 = saluta, 0 = esci").strip())
    if scelta == 1:
        nome = input("Dimmi qual'è il tuo nome")
        print(f"Ciao: {nome}")
    elif scelta == 0:
        print("Arrivederci")
        break
    else:
        print("Comando non riconosciuto")