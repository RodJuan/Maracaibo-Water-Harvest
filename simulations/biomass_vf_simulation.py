# Simulación Biomasa con 55 L/día + N Catatumbo
agua_neta = 55.0  # L/día
WUE = 0.095       # kg FW / L (con +12% por nitrógeno ionizado)
biomasa = agua_neta * WUE

print(f"Biomasa sostenible: {biomasa:.2f} kg/día")
print(f"Equivalente aproximado: {int(biomasa * 20)} raciones diarias de microgreens")
