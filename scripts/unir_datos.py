import json
import math

def distancia(a,b,c,d):
    return math.sqrt((a-c)**2 + (b-d)**2)

with open("../data/soportes_h3.json") as f:
    soportes = json.load(f)

with open("../data/tricot.json") as f:
    tricot = json.load(f)

for s in soportes:
    cercanos = 0

    for t in tricot:
        if t["lat"] and t["lng"]:
            if distancia(s["lat"], s["lng"], t["lat"], t["lng"]) < 0.01:
                cercanos += 1

    s["tricot_cercanos"] = cercanos

with open("../data/soportes_enriquecidos.json", "w") as f:
    json.dump(soportes, f, indent=2)

print("🔥 Cruce listo")