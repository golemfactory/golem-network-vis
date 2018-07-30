import pandas as pd
import json

with open("./data.txt", "r") as f:
    d = f.readlines()
d.pop(0)
d.pop(0)
separator = d.pop(0)

# first part of the list is p2p_info
separator_pos = d.index(separator)

p2p = d[:separator_pos]
# second part is active nodes
active_nodes = d[(separator_pos+1):]
active_nodes = [a.split()[-1][1:-1] for a in active_nodes]

keys = [k.replace("p2pstats.", "")[:-1] for k in p2p[::2]]
vals = [json.loads(json.loads(v.replace("\\x", "_UNICX_"))) for v in p2p[1::2]] # SOOOO UGLY

vals = [[v for v in vv["p2p_snapshot"] if v["key_id"] in active_nodes] for vv in vals if vv]

assert len(keys) == len(vals)

network_all = {k: len(vv) for k, vv in zip(keys, vals) if k in active_nodes}
network = {k: [v["key_id"] for v in vv] for k, vv in zip(keys, vals) if k in active_nodes}
connections_set = set((k1, k2) for k1 in network.keys() for k2 in network[k1])

out = {}

def get_degree(k):
    return network_all[k]

out["nodes"] = [{"id": k, "group": get_degree(k)} for k in network_all.keys()]
out["links"] = [{"source": k1, "target": k2, "value": 1} 
                for k1, k2 in connections_set
                if k1 in keys and k2 in keys]

# import IPython; IPython.embed()


with open("graph.json", "w") as f:
    json.dump(out, f)