# Sono un commento Ctrl + K + C - opposto Ctrl + K + U
# print("Ciao")
# print("Posso stampare anche dei numeri", 42)
# print("Posso stampare anche dei numeri 42")

# nome_corso = "AI Application Developer"
# numero = 5

# a = "Ciao"
# a = 5           # Non Type-Safe
# a = "🤣"

# print(a)

# Tipi di dato primitivo
# nome_corso = "AI Appl..."
# numero_studenti = 5
# ore_modulo = 35.0
# corso_attivo = True

# print(nome_corso, numero_studenti, ore_modulo, corso_attivo)

# print( type(nome_corso) )   # Duplicazione Alt + Maiusc + Freccia Su
# print( type(numero_studenti) )
# print( type(ore_modulo) )
# print( type(corso_attivo) )

# Verifica del tipo
# a = "Ciao"
# a = 5           # Non Type-Safe
# a = "🤣"

# print(type(a))

## ---------------------- OPERAZIONI CON NUMERI

# print(7 / 2)     # 1             # CPU ONLY - NO RAM
# print(7 / 2)    # 1
# print(7 / 2)    # 1
# print(7 / 2)    # 1

# risultato = 7 / 2  # 2              # CPU + RAM
# print(risultato) # 0
# print(risultato) # 0
# print(risultato) # 0
# print(risultato) # 0

# print(7 / 2)    # divisione
# print(7 // 2)   # divisione intera
# print(7 % 4)    # resto                 7 = 4 -> 3
# print(3 ** 3)   # potenza

# print(10 % 2 == 0)

## -------------------- OPERAZIONI SU STRINGHE

# richiesta = "  URGENTE: non riesco ad accedere alla piattaforma   "
# print( richiesta )
# print( richiesta.strip() )
# print( richiesta.lower() )

# print( richiesta.strip().lower() )  # 102 -> OK
# print( richiesta.lower().strip() )  # 108

# print( len(richiesta.strip()) )
# # print( len(5) ) # ERRORE
# print("urgente" in richiesta.lower())

# ------------------------------- Interpolazione
# studente = "Giovanni Pace"
# ore = 35.5

# # print(studente + " ha frequentato " + ore + "ore") # ERRORE, int non compatibile
# print(f"{studente} ha frequentato {ore} ore")
# print(f"La somma di 5 + 2 è: {5 + 2}")

# parola = "Giovanni"
# print( parola[0], parola[-1], parola[0:3] )

# matricola = "AB-2027"
# print( matricola[3:7] )
# print( matricola[-4:] )