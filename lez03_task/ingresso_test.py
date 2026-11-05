from ingresso import controlla_ingresso

def test_puo_entrare():
    assert controlla_ingresso("Mario", "Rossi", 37) == "Mario Rossi: puoi entrare"

def test_non_puo_entrare():
    assert controlla_ingresso("Mario", "Rossi", 39) == "Mario Rossi: non puoi entrare"

def test_edge_case():
    assert controlla_ingresso("Mario", "Rossi", 37.5) == "Mario Rossi: puoi entrare"