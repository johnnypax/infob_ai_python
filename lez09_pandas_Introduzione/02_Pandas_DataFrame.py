import pandas as pd

dictionary = {
    'Nome': ['Giovanni', 'Valeria', 'Marika'],
    'Eta': [38, 19, 39],
    'Citta': ['L\'Aquila', 0, 'Chieti']
}

df_tabella = pd.DataFrame(dictionary)
print(df_tabella)