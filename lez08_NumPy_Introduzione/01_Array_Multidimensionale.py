import numpy as np

# stipendi 
salario_gio = [1500,1700,2000,1300]
salario_mar = [1690,1200,3000,91350]
salario_val = [1700,1800,2100,1400]

riep_salari = np.array([salario_gio, salario_mar, salario_val])

# bonus
bonus_gio = [100, 100, 120, 130]
bonus_mar = [110, 130, 120, 130]
bonus_val = [120, 120, 150, 180]

riep_bonus = np.array([bonus_gio, bonus_mar, bonus_val])

riepilogo = riep_salari +  riep_bonus
print(riepilogo)

# Funzioni statistiche
print("Massimo valore", np.max(riepilogo))
print("Media", np.mean(riepilogo))
print("Minimo valore", np.min(riepilogo))

print(np.amax(riepilogo, axis=0))
print(np.amax(riepilogo, axis=1))
