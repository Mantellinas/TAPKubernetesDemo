#! /usr/bin/env bash
docker login
minikube delete --all
minikube start

echo "Entro dentro la cartella NameSpace e creo il namespace su minikube"
cd NameSpace
kubectl apply -f namespace.yaml
cd ..
echo "Entro dentro la cartella BeansTalk e creo la coda su minikube"
cd BeansTalk
kubectl apply -f beanstalk_deployment.yaml 
sleep 10
cd ..
echo "Entro dentro la cartella Actor e creo i due file di configurazione"
cd Actors
kubectl apply -f beanstalk_config_map.yaml 
sleep 10
echo "Eseguo il producer"
kubectl apply -f job_producer.yaml 
echo "Eseguo il consumer"
kubectl apply -f job_consumer.yaml 