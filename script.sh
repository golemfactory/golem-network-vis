#!/bin/bash


ssh $1@$2 > data.txt

wget -O monitor.csv https://stats.golem.network/dump
ipython generate1.py
ipython generate2.py

python -m http.server
