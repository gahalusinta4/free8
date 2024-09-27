import subprocess
import time

# Prompt the user for the worker name
worker_name = input("Enter RIG name: ")

# Define the log file
log_file = "mining.log"

# Command to run SRBMiner-MULTI
command = [
    "./SRBMiner-MULTI",
    "--disable-gpu",
    "--algorithm", "xelishashv2",
    "--pool", "cn.vipor.net:5077",
    "--wallet", "xel:qcd39a5u8cscztamjuyr7hdj6hh2wh9nrmhp86ljx2sz6t99ndjqzqq9qqqqqyq5vl3zc3tvl60",
    "--worker", worker_name,
    "--password", "solo",
    "--cpu-threads", "30"
]

# Open the log file in append mode and run the command in the background
with open(log_file, "a") as log:
    process = subprocess.Popen(command, stdout=log, stderr=log)

# Continue running a while loop or other tasks
try:
    while True:
        # Perform other tasks or simply keep the loop running
        print("Mining process is running in the background...")
        time.sleep(10)  # Sleep for 10 seconds before printing again

except KeyboardInterrupt:
    print("Exiting...")

    # Optionally, terminate the background process if needed
    process.terminate()
    process.wait()
    print("Mining process terminated.")
