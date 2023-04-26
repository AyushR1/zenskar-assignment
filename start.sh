#!/bin/bash


echo "Starting docker containers for kafka and zookeeper"
sudo docker compose up -d

echo "Creating topics"
sudo docker exec broker \
kafka-topics --bootstrap-server broker:9092 \
             --create \
             --topic consumer  


echo "Starting workers"
python workers.py &

echo "Starting django server"
python manage.py runserver
