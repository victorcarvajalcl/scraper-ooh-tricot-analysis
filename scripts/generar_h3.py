import json
import h3

# Cargar H6 desde tu data real
with open("data/h6.geojson") as f:
    h6_geo = json.load(f)

h3_set = set()

# Obtener H3 padres
for feature in h6_geo["features"]:
    props = feature.get("properties", {})
    
    h6_index = props.get("h6") or props.get("hex")
    
    if not h6_index:
        continue

    parent = h3.cell_to_parent(h6_index, 3)
    h3_set.add(parent)

features = []

for h in h3_set:
    boundary = h3.cell_to_boundary(h)
    
    coords = [[lng, lat] for lat, lng in boundary]
    coords.append(coords[0])

    features.append({
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [coords]
        },
        "properties": {
            "h3": h
        }
    })

geojson = {
    "type": "FeatureCollection",
    "features": features
}

# Guardar donde tu index lo espera
with open("data/h3.geojson", "w") as f:
    json.dump(geojson, f)

print("✅ H3 generado correctamente en data/h3.geojson")