def calcola_priorita(testo):
    if "urgente" in testo.lower():
        return "alta"
    elif "problema" in testo.lower():
        return "media"
    elif "errore" in testo.lower():
        return "attenzione"
    else:
        return "bassa"

# def test_calcola_priorita():
#     assert calcola_priorita("Urgente!") == "alta"
#     assert calcola_priorita("ciao") == "bassa"
#     assert calcola_priorita("Giovanni") == "bassa"

def test_dovrebbe_ritornare_alta():
    assert calcola_priorita("Urgente!") == "alta"

def test_dovrebbe_ritornare_bassa():
    assert calcola_priorita("ciao") == "bassa"

def test_dovrebbe_ritornare_bassa():
    assert calcola_priorita("Giovanni") == "bassa"


# Crea una funzione che calcola la somma e testate