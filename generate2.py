import pandas as pd
import json

df = pd.read_csv("./monitor.csv", index_col="node_id")
d = df.to_dict("index")


with open("node_info.json", "w") as f:
    json_text = json.dumps(d, ensure_ascii=True)
    f.write("node_info = ")
    f.write(json_text)
    f.write(";")


with open("data.txt", "r") as f:
    d = f.readlines()

d.pop(0)
d.pop(0)
separator = d.pop(0)
# first part of the list is p2p_info
separator_pos = d.index(separator)
d = d[:separator_pos]


keys = [k.replace("p2pstats.", "")[:-1] for k in d[::2]]
vals = [json.loads(json.loads(v.replace("\\x", "_UNICX_"))) for v in d[1::2]] # SOOOO UGLY
assert len(keys) == len(vals)
network_all = {k: vv["p2p_snapshot"] for k, vv in zip(keys, vals)}


with open("p2p_info.json", "w") as f:
    json_text = json.dumps(network_all, ensure_ascii=True)
    f.write("p2p_info = ")
    f.write(json_text)
    f.write(";")

