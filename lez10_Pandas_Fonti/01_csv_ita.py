import pandas as pd
from pathlib import Path

CARTELLA = Path(__file__).parent / "dati"
FILE_ORDINI = CARTELLA / "01_ordini.csv"

# Estrazione del file
# try:
#     df_sbagliato = pd.read_csv(FILE_ORDINI, encoding="UTF-8", encoding_errors="strict")
#     print(df_sbagliato)
# except Exception as errore:
#     print("Errore: ", errore)

# Estrazione colonne
try:
    df_sbagliato = pd.read_csv(
                            FILE_ORDINI, 
                            encoding="UTF-8", 
                            encoding_errors="strict",
                            sep=";",
                            decimal=",")
    print(df_sbagliato.head(10))
    print(df_sbagliato.shape)           # Righe, Colonne
except Exception as errore:
    print("Errore: ", errore)

print("Programma terminato")