#!/bin/bash

#su - kafka -c "echo '[Unit]\nRequires=network.target remote-fs.target\nAfter=network.target remote-fs.target\n\n[Service]\nType=simple\nUser=kafka\nExecStart=/home/kafka/kafka/bin/zookeeper-server-start.sh /home/kafka/kafka/config/zookeeper.properties\nExecStop=/home/kafka/kafka/bin/zookeeper-server-stop.sh\nRestart=on-abnormal\n\n[Install]\nWantedBy=multi-user.target' >> /etc/systemd/system/zookeeper.service";

su - kafka -c "echo $'[Unit]
Requires=zookeeper.service
After=zookeeper.service

[Service]
Type=simple
User=kafka
ExecStart=/bin/sh -c '/home/kafka/kafka/bin/kafka-server-start.sh /home/kafka/kafka/config/server.properties > /home/kafka/kafka/kafka.log 2>&1'
ExecStop=/home/kafka/kafka/bin/kafka-server-stop.sh
Restart=on-abnormal

[Install]
WantedBy=multi-user.target'>> teste.sh";






