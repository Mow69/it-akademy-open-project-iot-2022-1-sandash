#!/usr/bin/env python3

import json
import random
import paho.mqtt.client as mqtt
import mysql.connector

broker = 'gazometre.freeboxos.fr'
port = 1883
topic = "/rfid/present"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'sandash'
password = 'sandash'

db_params = {
    'host': "localhost",
    'user': "sanduser",
    'password': "sandpassword",
    'database': "sandash",
}


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    m_decode = str(msg.payload.decode("utf-8", "ignore"))
    message = json.loads(m_decode)
    presents = message['presents']
    locals = message['locals']

    with mysql.connector.connect(**db_params) as db:
        with db.cursor() as c:
            for rfid in presents:
                sql = "UPDATE user SET is_present = 0 WHERE rfid_tag <> " + str(rfid)
                c.execute(sql)
            for rfid in presents:
                sql = "UPDATE user SET is_present = 1 WHERE rfid_tag = " + str(rfid)
                c.execute(sql)

            if locals is not None:
                c.execute("UPDATE weather SET temperature = " + str(locals['temp']) + " WHERE id = 1")
                c.execute("UPDATE weather SET humidity = " + str(locals['humidity']) + " WHERE id = 1")
            db.commit()


def init_bdd():
    with mysql.connector.connect(**db_params) as db:
        with db.cursor() as c:
            c.execute("DELETE FROM weather")
            db.commit()

            sql = "INSERT INTO weather(id, temperature, humidity) VALUES (1, 0, 0)"
            c.execute(sql)
            db.commit()


def run():
    init_bdd()
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
