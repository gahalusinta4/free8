#!/bin/sh

# Prompt the user for the worker name
read -p "Enter RIG name: " WORKER_NAME

# Run the mining command with the user-provided worker name
./SRBMiner-MULTI --disable-gpu --algorithm verushash --pool de.vipor.net:5040 --wallet RFKr91aNYATHiemELH8FfCyNDFuo1gkAbK --Worker "$WORKER_NAME" --cpu-threads 30
