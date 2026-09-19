#!/bin/bash
set -e

RG="cloud-demo-rg"
VM="cloud-demo-vm"
LOCATION="eastus"

az group create --name $RG --location $LOCATION

az vm create \
  --resource-group $RG \
  --name $VM \
  --image Ubuntu2204 \
  --size Standard_B1s \
  --admin-username azureuser \
  --generate-ssh-keys \
  --output none

az vm run-command invoke \
  --resource-group $RG \
  --name $VM \
  --command-id RunShellScript \
  --scripts "sudo apt-get update -y && sudo apt-get install -y nginx && sudo systemctl enable --now nginx && echo 'Automation successful' && hostname && uptime"

echo "VM created and configured successfully."