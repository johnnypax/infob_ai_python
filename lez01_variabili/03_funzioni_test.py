def calcola_priorita(testo):
    if "urgente" in testo.lower():
        return "alta"
    elif "problema" in testo.lower():
        return "media"
    elif "errore" in testo.lower():
        return "attenzione"
    else:
        return "bassa"

def test_calcola_priorita():
    assert calcola_priorita("Urgente!") == "alta"
    assert calcola_priorita("ciao") == "bassa"
    assert calcola_priorita("Giovanni") == "bassa"