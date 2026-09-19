Steps to run:



1. Start Minikube.
2. Build the Docker image.
3. Load the image into Minikube.
4. Deploy with kubectl.
5. Check Pods and Services.
6. Open the application.



\# Start the Minikube cluster

minikube start



\# Build the Docker image

docker build -t python-12factor-app:latest .



\# Load the image into Minikube

minikube image load python-12factor-app:latest



\# Create the Kubernetes Deployment

kubectl apply -f deployment.yaml



\# Create the Kubernetes Service

kubectl apply -f service.yaml



\# Verify the Deployment

kubectl get pods



\# Verify the Service

kubectl get services



\# Open the application in a browser

minikube service python-12factor-service

