#!/bin/bash


# How kafka is capable to communicate in a network, we will create a specific user for kafka.
# -m guarantees that it will be create the folder /home/kafka
sudo useradd kafka -m;

# defines a passwd for kafka user
sudo passwd kafka;

# adds kafka user to sudo group
sudo adduser kafka sudo;

#login into kafkauser
su -l kafka;

#create /home/kafka/Downloads
mkdir ~/Downloads;

# install curl
sudo apt-get update && sudo apt-get install curl -y;

# download kafka binaries
curl "https://archive.apache.org/dist/kafka/2.1.1/kafka_2.11-2.1.1.tgz" -o ~/Downloads/kafka.tgz;

# extract binaries with strip 1 to guarantees that it will be extracted in ~/kafka/ and not /kafka/kafka_2.12.../
tar -xvzf ~/Downloads/kafka.tgz --strip 1;







