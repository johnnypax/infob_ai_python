from pathlib import Path
import pandas as pd

CARTELLA = Path(__file__).parent / "dati"
FILE_EXCEL = CARTELLA / "02_prodotti.xlsx"

# Quanti fogli contiene?
# with pd.ExcelFile(FILE_EXCEL) as excel:
#     print("Fogli presenti: ", excel.sheet_names)

# Leggere un foglio specifico
# prodotti = pd.read_excel(FILE_EXCEL, sheet_name="Prodotti")
# print(prodotti.head())

# Leggere tutti i fogli
# tutti_fogli = pd.read_excel(FILE_EXCEL, sheet_name=None)
# print(tutti_fogli)

# for nome, tabella in tutti_fogli.items():
#     print(f"{nome} -> {tabella.shape}")

# Merge ovvero... JOIN

prodotti = pd.read_excel(FILE_EXCEL, sheet_name="Prodotti")
categorie = pd.read_excel(FILE_EXCEL, sheet_name="Categorie")

listino = prodotti.merge(categorie, on="categoria")
listino["prezzo_iva"] = listino["prezzo_listino"] * (listino["aliquota_iva"] / 100)
listino["prezzo_ivato"] = listino["prezzo_listino"] + listino["prezzo_iva"]
# print(listino.head())

riepilogo = (listino.groupby("categoria").agg(
                                            n_prodotti=("id_prodotto", "count"),
                                            prezzo_medio=("prezzo_listino", "mean"),
                                            prezzo_max=("prezzo_listino", "max")).round(2)
                                        .sort_values("prezzo_medio", ascending=False)
            )

FILE_REPORT = CARTELLA / "02_rapporto.xlsx"

with pd.ExcelWriter(FILE_REPORT) as writer:
    listino.to_excel(writer, sheet_name="Listino", index=False)
    riepilogo.to_excel(writer, sheet_name="Riepilogo")