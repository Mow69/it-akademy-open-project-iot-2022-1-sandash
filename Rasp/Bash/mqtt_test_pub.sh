#!/bin/bash

mosquitto_pub -h gazometre.freeboxos.fr -t "test" -u sandash -P sandash -m "Test message from pi"
