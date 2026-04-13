import pandas as pd
import json

df = pd.read_excel("../data/tricot/tricot_geocodificado.xlsx")

data = []

for _, row in df.iterrows():
    if pd.notna(row["Latitud"]) and pd.notna(row["Longitud"]):
        data.append({
            "nombre": "Tricot",
            "direccion": row.get("Dirección"),
            "comuna": row.get("Ciudad / Comuna"),
            "lat": row.get("Latitud"),
            "lng": row.get("Longitud"),
            "tipo": "tienda"
        })

with open("../data/tricot.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ tricot.json creado")