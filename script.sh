#!/bin/bash

echo "Starting to dump redis"
ssh $1@$2 "bash -s" < redis-dump.sh > data.txt
echo "Dumping redis done"

wget -O monitor.csv https://stats.golem.network/dump
python generate1.py
python generate2.py

python -m http.server
