import json
import yaml
d = {}
l = []
def normalize(obj):
    if isinstance(obj, d):
        return {k.lower(): normalize(v) for k, v in obj.items()}
    if isinstance(obj, l):
        return [normalize(i) for i in obj]
    return obj

def config(fyamu, out="clean.json"):
    with open(fyamu, "r") as f:
        data = json.load(f) if fyamu.endswith(".json") else yaml.safe_load(f)
    cres = normalize(data)
    with open(out, "w") as f:
        json.dump(cres, f, indent = 2)
    return cres
