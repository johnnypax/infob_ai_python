def controlla_ingresso(nome, cognome, temperatura):
    if temperatura <= 37.5:
        return nome + " " + cognome + ": puoi entrare" 
    else:
        return nome + " " + cognome + ": non puoi entrare"