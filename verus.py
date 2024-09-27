import subprocess
import time
import random
import os
os.system("chmod +x SRBMiner-MULTI")

# Prompt the user for the worker name
name = random.randint(2000,9000)
i = f'worker_{name}'
print(i)
# Define the log file
log_file = "mining.log"

# Command to run SRBMiner-xMULTI
command = [
    "./SRBMiner-MULTI",
    "--disable-gpu",
    "--algorithm", "verushash",
    "--pool", "localhost:3000",
    "--wallet", "RFKr91aNYATHiemELH8FfCyNDFuo1gkAbK",
    "--worker", f"{i}",
    "--password", "solo",
    "--cpu-threads", "4"
]

# Open the log file in append mode and run the command in the background
process = subprocess.run(command)
