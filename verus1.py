import subprocess
import time
import random
import os
os.system("sudo chmod +x SRBMiner-MULTI")

# Prompt the user for the worker name
name = random.randint(2000,9000)
i = f'worker_{name}'
print(i)
# Define the log file
log_file = "mining.log"

# Command to run SRBMiner-xMULTI

