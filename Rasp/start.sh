#!/bin/bash

python ./MQTT/SubSyncDB.py &
python ./MQTT/PubSyncDB.py &
python ./RFID/Read.py