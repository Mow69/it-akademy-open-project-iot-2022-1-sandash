#!/usr/bin/env python3

import time

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sqlite3

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
REDL = 20
GREENL = 21

GPIO.setup(REDL, GPIO.OUT)
GPIO.setup(GREENL, GPIO.OUT)

reader = SimpleMFRC522()
connexion = sqlite3.connect("bdd.db")
cursor = connexion.cursor()


def read_rfid():
    try:
        id, text = reader.read()
        print(id)
        print(text)

    finally:
        return id


def control_sqlite(rfId):
    cursor.execute("SELECT validate FROM rfids WHERE rfid = ?", [str(rfId)])
    return bool(cursor.fetchone()[0])


def register_sqlite(rfId):
    # is_present = bool(cursor.execute("SELECT present FROM rfids WHERE rfid = ?", [str(rfId)]))
    cursor.execute("SELECT present FROM rfids WHERE rfid = ?", [str(rfId)])
    is_present = bool(cursor.fetchone()[0])
    if is_present:
        cursor.execute("UPDATE rfids SET present = 0 WHERE rfid = ?", [str(rfId)])
        connexion.commit()
        return print('Going OUT')
    cursor.execute("UPDATE rfids SET present = 1 WHERE rfid = ?", [str(rfId)])
    connexion.commit()
    return print('Going IN')


def green_led():
    print('Can go')
    GPIO.output(GREENL, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(GREENL, GPIO.LOW)
    # done the red led
    return True


def red_led():
    print('warning')
    GPIO.output(REDL, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(REDL, GPIO.LOW)
    # done the green led
    return False


def run():
    while True:
        time.sleep(3)
        rfid = read_rfid()
        if control_sqlite(rfid):
            register_sqlite(rfid)
            green_led()
        else:
            red_led()


if __name__ == '__main__':
    run()
    connexion.close()
    GPIO.cleanup
