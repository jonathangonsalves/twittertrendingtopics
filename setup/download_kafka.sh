#!/bin/bash


if [ ! -d "/home/kafka/Downloads" ]; then
    su - kafka -c "mkdir ~/Downloads";
fi

echo "Write your kafka user passwd..."
sudo -s -u kafka bash -c "sudo apt-get update && sudo apt-get install curl -y";

su - kafka -c 'curl "https://archive.apache.org/dist/kafka/2.1.1/kafka_2.11-2.1.1.tgz" -o ~/Downloads/kafka.tgz';

su - kafka -c "mkdir ~/kafka";

su - kafka -c "tar -xvzf ~/Downloads/kafka.tgz --strip 1 -C ~/kafka";

su - kafka -c 'echo "\ndelete.topic.enable = true" >> ~/kafka/config/server.properties';
