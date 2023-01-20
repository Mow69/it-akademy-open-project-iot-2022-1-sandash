<?php

namespace App\EventListener;

use Doctrine\Persistence\Event\LifecycleEventArgs;
use \PhpMqtt\Client\MqttClient;

class UserListener
{
    const SERVER   = 'gazometre.freeboxos.fr';
    const PORT     = 1883;
    const CLIENT_ID = 'symfony-publisher';

    public function mqttPublish($id, $rfid, $topic): Void
    {
        $message = json_encode(['id' => $id, 'rfid' => $rfid]);
        $mqtt = new MqttClient(self::SERVER, self::PORT, self::CLIENT_ID);
        $mqtt->connect();
        $mqtt->publish($topic, $message, 0);
        $mqtt->disconnect();

    }
}