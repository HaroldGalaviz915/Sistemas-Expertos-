# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 22:50:20 2025

@author: PC
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# Simulación de dataset
# =========================
# Datos: consumo de electricidad según número de aparatos y horas de aire acondicionado
np.random.seed(0)
num_samples = 50
num_aparatos = np.random.randint(2, 10, num_samples)
horas_ac = np.random.randint(1, 8, num_samples)

# Consumo en kWh (relación lineal + ruido)
consumo = 30 + (5 * num_aparatos) + (10 * horas_ac) + np.random.normal(0, 5, num_samples)

# Crear DataFrame
data = pd.DataFrame({
    'num_aparatos': num_aparatos,
    'horas_ac': horas_ac,
    'consumo': consumo
})

print("Primeras filas del dataset:\n", data.head())

# =========================
# Preparar variables
# =========================
X = data[['num_aparatos', 'horas_ac']].values
y = data['consumo'].values

# Agregar columna de unos para el sesgo (bias)
X_b = np.c_[np.ones((X.shape[0], 1)), X]

# =========================
# Cálculo de parámetros con fórmula de la regresión lineal (Normal Equation)
# =========================
theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
print("\nParámetros (theta):", theta)

# =========================
# Predicciones
# =========================
y_pred = X_b.dot(theta)

# =========================
# Visualización
# =========================
plt.scatter(range(len(y)), y, label="Valores reales")
plt.plot(range(len(y)), y_pred, color="red", label="Predicción")
plt.xlabel("Muestra")
plt.ylabel("Consumo de electricidad (kWh)")
plt.legend()
plt.title("Regresión Lineal: Consumo eléctrico")
plt.show()
