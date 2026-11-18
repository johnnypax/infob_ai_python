
# Traccia dell'esercizio
Utilizzando NumPy, sviluppare un programma che esegua le seguenti operazioni sul dataset

```python
reparti = [
    "Produzione", "Magazzino", "Uffici",
    "Laboratorio", "Server", "Logistica",
    "Manutenzione", "Confezionamento"
]

consumi = np.array([
    [4200, 4100, 4500, 4700, 4900, 5200, 5500, 5400, 5100, 4800, 4600, 4400],
    [2100, 2200, 2300, 2400, 2500, 2700, 2800, 2600, 2500, 2400, 2300, 2200],
    [1200, 1150, 1300, 1250, 1400, 1600, 1800, 1750, 1500, 1350, 1250, 1400],
    [3200, 3300, 3400, 3600, 3800, 3900, 4100, 4000, 3700, 3500, 3400, 3300],
    [6500, 6400, 6600, 6700, 6900, 7100, 7300, 7200, 7000, 6800, 6600, 6500],
    [1800, 1900, 2000, 2100, 2300, 2500, 2600, 2400, 2200, 2100, 2000, 1900],
    [2800, 2700, 2900, 3100, 3200, 3400, 3500, 3300, 3100, 3000, 2900, 2800],
    [3500, 3600, 3800, 4000, 4200, 4500, 4700, 4600, 4300, 4100, 3900, 3700]
])
```

### Parte 1 – Statistiche generali
1. Individuare il consumo massimo registrato.
2. Individuare il consumo minimo registrato.
3. Calcolare il consumo medio complessivo.
4. Calcolare la deviazione standard dei consumi.
### Parte 2 – Analisi per reparto (axis=1)
5. Calcolare il consumo totale annuale di ciascun reparto.
6. Calcolare il consumo medio mensile di ciascun reparto.
7. Individuare il consumo massimo registrato da ogni reparto.
8. Determinare quale reparto ha consumato più energia durante l'anno.
### Parte 3 – Analisi per mese (axis=0)
9. Calcolare il consumo totale aziendale per ciascun mese.
10. Calcolare il consumo medio per reparto in ogni mese.
11. Individuare il mese con il consumo totale più alto.
12. Individuare il mese con il consumo totale più basso.
### Parte 4 – Operazioni avanzate
13. Contare quanti consumi mensili superano 5.000 kWh.
14. Individuare tutti i consumi superiori alla media generale.
15. Simulare una riduzione dei consumi del 10% e creare una nuova matrice.
16. Calcolare il risparmio energetico totale ottenuto.