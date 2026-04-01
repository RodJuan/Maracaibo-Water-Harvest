import numpy as np
import matplotlib.pyplot as plt

def dew_point(T, RH):
    """Fórmula Magnus"""
    es = 6.112 * np.exp((17.67 * T) / (T + 243.5))
    e = es * (RH / 100)
    return (243.5 * np.log(e / 6.112)) / (17.67 - np.log(e / 6.112))

# Parámetros Maracaibo
T_air = 27.0          # °C
RH = 80.0             # %
Q_rad = 45.0          # W/m² enfriamiento radiativo con pintura IR
hours_night = 12
Lv = 2.45e6           # J/kg

Td = dew_point(T_air, RH)
T_surf = T_air - 5.6  # delta realista con pintura IR

print(f"Punto de rocío: {Td:.2f} °C")
print(f"Temperatura superficie: {T_surf:.2f} °C")

if T_surf < Td:
    m_hour = (Q_rad * 0.7) / Lv * 3600 / 1000   # kg/m²/h → L/m²/h
    total_L_m2 = m_hour * hours_night
    print(f"Rendimiento simulado: {total_L_m2:.2f} L/m²/noche")
    print(f"Para 100 m²: {total_L_m2 * 100:.1f} L/día")
else:
    print("Condiciones insuficientes para condensación")
