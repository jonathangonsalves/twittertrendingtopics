
#!/bin/bash

exists=$(grep -c "kafka" /etc/passwd)

if [ $exists -eq 0 ]; then
    echo "Creating Kafka user..."
    sudo useradd -m -p $(openssl passwd -1 "kafka") kafka;
    echo "Adding kafka user in sudo group..."
    sudo adduser kafka sudo;
else
    echo "Kafka user already exists..."
    return
fi
