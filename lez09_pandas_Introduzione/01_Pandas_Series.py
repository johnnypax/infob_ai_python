import pandas as pd

# Serie con indice automatico
# persone = ["Giovanni", "Valeria", "Maria", 85]
# invitati = pd.Series(persone)

# print(type(persone))
# print(persone)

# print(type(invitati))
# print(invitati)

# # Serie con indice personalizzato
# numeri = pd.Series([2,89,56,90,890], index=['a', 'b', 'c', 'e', 'd'])
# # print(numeri)
# # print(numeri['a'])

# print(numeri.min())
# print(numeri.mean())
# print(numeri.max())

# print("-"*30)

# # print(numeri + 800)
# print(numeri / 100)

# ----------------------------

persone = ["Giovanni", "Valeria", "Maria"]
invitati = pd.Series(persone)

print(invitati.str.upper())
print(invitati + "-TEST")
