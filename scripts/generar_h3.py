import json
import h3

# Bounding box Santiago
min_lat, max_lat = -33.75, -33.15
min_lng, max_lng = -71.05, -70.2

resolution = 5

# GeoJSON formato correcto
polygon = {
    "type": "Polygon",
    "coordinates": [[
        [min_lng, min_lat],
        [max_lng, min_lat],
        [max_lng, max_lat],
        [min_lng, max_lat],
        [min_lng, min_lat]
    ]]
}

# ✅ NUEVA FUNCIÓN (H3 v4)
h3_indexes = h3.geo_to_cells(polygon, resolution)

features = []

for h in h3_indexes:
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

with open("data/h3.geojson", "w") as f:
    json.dump(geojson, f)

print(f"✅ Generados {len(features)} hex H3")