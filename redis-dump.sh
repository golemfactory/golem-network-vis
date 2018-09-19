#!/bin/bash
echo ---CUT---
redis-cli --scan --pattern 'p2p*' | while read key; do
        echo $key
        redis-cli get $key
done
echo ---CUT---
redis-cli smembers active_nodes 
