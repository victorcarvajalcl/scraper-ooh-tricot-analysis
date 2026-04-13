import pandas as pd
from geopy.geocoders import Nominatim
from time import sleep
import re

# Cargar archivo
df = pd.read_excel("tricot_tiendas.xlsx")

# Limpiar filas vacías
df = df.dropna(subset=["Dirección", "Ciudad / Comuna"])

# Crear geolocalizador
geolocator = Nominatim(user_agent="geo_tricot_v2")

latitudes = []
longitudes = []

for index, row in df.iterrows():
    try:
        # 🔹 LIMPIEZA DE DIRECCIÓN (CLAVE)
        direccion_raw = str(row["Dirección"])

        # Eliminar textos como "Local", "Lc", etc.
        direccion_limpia = re.sub(r'Local.*|Lc.*|LOCAL.*', '', direccion_raw)
        direccion_limpia = direccion_limpia.strip()

        # Construir dirección final
        direccion = f"{direccion_limpia}, {row['Ciudad / Comuna']}, Chile"

        # Geocodificar
        location = geolocator.geocode(direccion)

        if location:
            latitudes.append(location.latitude)
            longitudes.append(location.longitude)
            print(f"OK: {direccion}")
        else:
            latitudes.append(None)
            longitudes.append(None)
            print(f"NO ENCONTRADO: {direccion}")

    except Exception as e:
        latitudes.append(None)
        longitudes.append(None)
        print(f"ERROR: {direccion} -> {e}")

    sleep(1.5)  # evitar bloqueo

# Agregar columnas
df["Latitud"] = latitudes
df["Longitud"] = longitudes

# Guardar resultado
df.to_excel("tricot_geocodificado.xlsx", index=False)

print("\nProceso terminado 🚀")