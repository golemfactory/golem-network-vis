#!/bin/bash


ssh $1@$2 > data.txt

wget -O monitor.csv https://stats.golem.network/dump
python generate1.py
python generate2.py

python -m http.server
