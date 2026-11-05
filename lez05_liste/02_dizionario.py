studente = {
    "id": 1,
    "matricola": "AB12345",
    "nome": "Giovanni",
    "cognome": "Pace"
}

print(studente)
# print(studente["idcetto"]) # Accesso per chiave
print(studente.get("idcetto"))

for chiave, valore in studente.items():
    print(chiave, valore)