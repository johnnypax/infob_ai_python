# Creare un piccolo gestionale che permetta di:
# 1. Inserire un nuovo studente in lista
# 2. Stampare tutti gli studenti
# 3. Uscire

# Ogni studente è caratterizzato da 
# - ID: Autoincrementale, 
# - Nome: Stringa, 
# - Cognome: Stringa, 
# - Matricola: Stringa
lista_stud = []

while True:
    scelta = input("Cosa vuoi fare? \n1 - Inserisci Studente \n2 - Stampa Studenti \n3 - Quit\n")
    if scelta == "1":
        nome = input("Dammi il nome: ")
        cognome = input("Dammi il cognome: ")
        matricola = input("Dammi il matricola: ")

        studente = {
            "id": len(lista_stud) + 1,
            "nome": nome,
            "cognome": cognome,
            "matricola": matricola
        }

        lista_stud.append(studente)
        print("Inserimento effettuato con successo!")
    elif scelta == "2":
        for s in lista_stud:
            print(s)
    elif scelta == "3":
        break
    else:
        print("Comando non riconosciuto")
        
# TODO: Trasformare l'esercizio di sopra con funzioni (e testarle)