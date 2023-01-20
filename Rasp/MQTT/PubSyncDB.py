#!/usr/bin/env python3

import json
import sqlite3
import random
import time
import board
import adafruit_dht
import psutil
from paho.mqtt import client as mqtt_client

broker = 'gazometre.freeboxos.fr'
port = 1883
topic = "/rfid/present"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'sandash'
password = 'sandash'
dh11_gpio = board.D23


def read_all():  # for debug
    connexion = sqlite3.connect("bdd.db")
    cursor = connexion.cursor()

    cursor.execute("SELECT * FROM rfids")
    for result in cursor:
        print(result)
    connexion.close()


def init_dh11():
    for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
            proc.kill()

    return adafruit_dht.DHT11(dh11_gpio)


def read_local_weather(sensor):
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
        return {'temp': temp, 'humidity': humidity}
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
    except Exception as error:
        sensor.exit()
        raise error


def read_present():
    data = []
    connexion = sqlite3.connect("bdd.db")

    cursor = connexion.cursor()

    cursor.execute("SELECT rfid FROM rfids WHERE present = 1")
    for result in cursor:
        data.append(result[0])
    connexion.close()
    return data


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    sensor = init_dh11()

    while True:
        msg = json.dumps({'locals': read_local_weather(sensor), 'presents': read_present()})
        result = client.publish(topic, msg)

        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

        time.sleep(3)


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
