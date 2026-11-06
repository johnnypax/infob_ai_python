
from pathlib import Path

cartella = Path("output_infobasic") # C:\Users\ACADEMY\Desktop\Corso_PYTHON\output_infobasic
cartella.mkdir(exist_ok=True)
file_note = cartella / "note.txt"   # path del file
# print(file_note)
# print(file_note.name, file_note.suffix, file_note.stem)
# print("Esiste?", file_note.exists())

# Scrivere
# with open(file_note, "w", encoding="utf-8") as f:
#     f.write("Prima riga\n")
#     f.write("Seconda riga\n")

# with open(file_note, "a", encoding="utf-8") as f:
#     f.write("Terza riga")

with open(file_note, encoding="utf-8") as f:
    for numero, riga in enumerate(f, start=2):
        print(numero, riga)

# Trasformare il gestionale in modo che inserimento e stampa finiscano in CSV sul file.