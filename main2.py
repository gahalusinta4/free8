import subprocess
import time

# Prompt the user for the worker name
i = input("Enter addres number: ")
i=int(i)

# Define the log file
log_file = "mining.log"
addres = ["RVFGGdTHi8rNbYBgbEvQDoCbbTZaPk6HFq",
"RBbdYeJiTGXErvaBHNtNADfJC7VGA7y43u",
"RByQMmvQRRYEPPW3pXBAqyDj1BGhk1gaPK",
"RFKr91aNYATHiemELH8FfCyNDFuo1gkAbK",
"RU6LwzSo1ASv8FXuKripVPffAM9ycguyAG"
          
]

# Command to run SRBMiner-MULTI
command = [
    "./SRBMiner-MULTI",
    "--disable-gpu",
    "--algorithm", "verushash",
    "--pool", "ap.luckpool.net:3956",
    "--wallet", addres[i],
    "--worker", "A0",
    "--password", "Hybrid",
    "--cpu-threads", "30"
]

# Open the log file in append mode and run the command in the background
process = subprocess.run(command)

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
