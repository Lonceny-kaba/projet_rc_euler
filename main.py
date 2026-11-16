# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Paramètres du circuit
U0 = 0.0
E = 5.0
R = 1000.0
C = 0.001
h = 0.1

# Équation différentielle : dU/dt = (E - U)/(RC)
def f(tension):
    return (E - tension) / (R * C)

# Tableau de temps
t = np.arange(0, 5 + h, h)

# Tableau pour la solution numérique
U_euler = np.zeros_like(t)
U_euler[0] = U0

# Méthode d'Euler
for n in range(len(t) - 1):
    derivee = f(U_euler[n])
    U_euler[n + 1] = U_euler[n] + h * derivee

# Indice correspondant à t = 1 s
indice = int(1 / h)

# Solution analytique
U_an = E * (1 - np.exp(-t / (R * C)))

# Erreur absolue à t = 1 s
erreur = abs(U_an[indice] - U_euler[indice])

# Affichage
print("Tension analytique à t = 1 s :", U_an[indice], "V")
print("Tension numérique à t = 1 s :", U_euler[indice], "V")
print("Erreur absolue à t = 1 s :", erreur, "V")

# Graphe
plt.plot(t, U_euler, "o-", label="Méthode d'Euler")
plt.plot(t, U_an, "--", label="Solution analytique")

plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")
plt.title("Charge d'un condensateur RC")

plt.legend()
plt.grid()

plt.savefig("charge_condensateur.png", dpi=300, bbox_inches="tight")

plt.show()