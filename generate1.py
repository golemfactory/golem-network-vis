import pandas as pd
import json

with open("data.txt", "r") as f:
    d = f.readlines()
d.pop(0)
d.pop(0)

keys = [k.replace("p2pstats.", "")[:-1] for k in d[::2]]
vals = [json.loads(json.loads(v.replace("\\x", "_UNICX_"))) for v in d[1::2]] # SOOOO UGLY

assert len(keys) == len(vals)

network_all = {k: len(vv["p2p_snapshot"]) for k, vv in zip(keys, vals)}

network = {k: [v["key_id"] for v in vv["p2p_snapshot"]] for k, vv in zip(keys, vals)}
connections_set = set((k1, k2) for k1 in keys for k2 in network[k1])

out = {}

def get_degree(k):
    return network_all[k]

out["nodes"] = [{"id": k, "group": get_degree(k)} for k in keys]
out["links"] = [{"source": k1, "target": k2, "value": 1} 
                for k1, k2 in connections_set
                if k1 in keys and k2 in keys]

with open("graph.json", "w") as f:
    json.dump(out, f)