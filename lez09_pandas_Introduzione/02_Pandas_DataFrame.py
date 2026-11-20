import pandas as pd
import numpy as np

dictionary = {
    'Nome': ['Giovanni', 'Valeria', 'Marika', 'Ester'],
    'Eta': [38, 19, 39, np.nan],
    'Citta': ['L\'Aquila', pd.NA, 'Chieti', 'Pescara']
}

df_tabella = pd.DataFrame(dictionary)
# print(df_tabella)

# Operazioni semplici
# print( df_tabella["Nome"] )
# print( df_tabella["Nome"][0] )
# print( df_tabella.iloc[0] )
# print( df_tabella.loc[1, "Eta"] )

# Operazioni statistiche
# print( df_tabella.describe() )
# print( df_tabella.info() )

# print( df_tabella["Eta"].mean() )
# print( df_tabella.head(2) )
# print( df_tabella.tail(1) )

# Filtri
# print( df_tabella[ df_tabella["Eta"] > 30 ] )
# print( df_tabella[ df_tabella["Citta"] == "Chieti" ] )

# Esportazione
# df_tabella.to_csv("esportazione.csv", index=False)

# df_over_trenta = df_tabella[ df_tabella["Eta"] > 30 ]
# df_over_trenta.to_csv("esportazione_over_trenta.csv", index=False)

# Importazione
df_importato = pd.read_csv("esportazione_over_trenta.csv")
print(df_importato)
print(type(df_importato))

print(type(df_importato["Eta"]))

print(df_importato["Eta"].dtype)