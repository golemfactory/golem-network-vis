## Rudimentary visualization tool for golem network.

Used just to get a gist of what the network looks like, not production ready, done using duck tape, mostly.

Shows nodes graph and nodes info:

[[./screenshot.png]]

### Running

To run on new data, you have to have access to the internal golem network (bebum is where the monitor runs):
```
./script.sh $USER bebum
```

Otherwise, you can run on old (19.09.18) data by just:

```
python -m http.server
```