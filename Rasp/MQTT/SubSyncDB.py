#!/usr/bin/env python3

import random
import paho.mqtt.client as mqtt
import sqlite3
import json

broker = 'gazometre.freeboxos.fr'
port = 1883
topic = "#"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'sandash'
password = 'sandash'


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)


# The callback for when a PUBLISH message is received from the server.
def create_rfid(id, rfid):
    connexion = sqlite3.connect("bdd.db")
    cursor = connexion.cursor()

    data = [(id, rfid, 0, 1)]

    cursor.executemany("INSERT INTO rfids (distant_id, rfid, present, validate) VALUES (?, ?, ?, ?)", data)

    connexion.commit()
    connexion.close()


def update_rfid(id, rfid):
    connexion = sqlite3.connect("bdd.db")
    cursor = connexion.cursor()

    sql = """Update rfids set rfid = ? where distant_id = ?"""
    data = (rfid, id)
    cursor.execute(sql, data)

    connexion.commit()
    connexion.close()


def delete_rfid(id, rfid):
    connexion = sqlite3.connect("bdd.db")
    cursor = connexion.cursor()

    sql = 'DELETE FROM rfids WHERE distant_id=?'

    cursor.execute(sql, (id,))

    connexion.commit()
    connexion.close()


def on_message(client, userdata, msg):
    mqtt_create = "/rfid/create"
    mqtt_update = "/rfid/update"
    mqtt_delete = "/rfid/delete"

    print(msg.topic + " " + str(msg.payload))

    if msg.topic == mqtt_create:
        m_decode = str(msg.payload.decode("utf-8", "ignore"))
        message = json.loads(m_decode)
        id = str(message['id'])
        rfid = message['rfid']
        print("Create: " + rfid)
        create_rfid(id, rfid)
    elif msg.topic == mqtt_update:
        m_decode = str(msg.payload.decode("utf-8", "ignore"))
        message = json.loads(m_decode)
        id = str(message['id'])
        rfid = message['rfid']
        print("Update: " + rfid)
        update_rfid(id, rfid)
    elif msg.topic == mqtt_delete:
        m_decode = str(msg.payload.decode("utf-8", "ignore"))
        message = json.loads(m_decode)
        id = str(message['id'])
        rfid = message['rfid']
        print("Delete: " + rfid)
        delete_rfid(id, rfid)
    else:
        print("I'm not concerned")


def run():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, 1883, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()


if __name__ == '__main__':
    run()
