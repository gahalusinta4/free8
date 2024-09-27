import subprocess
import time
import random
import os
os.system("tmux kill-session")
os.system("tmux new-session -d -s ses python3 verus.py && tmux ls")
#os.system("python3 verus.py")

import time
import sys

def display_time(elapsed_time):
    mins, secs = divmod(elapsed_time, 60)
    hours, mins = divmod(mins, 60)
    timer = f"{int(hours):02}:{int(mins):02}:{int(secs):02}"
    sys.stdout.write("\r" + timer)
    sys.stdout.flush()

def stopwatch():
    start_time = time.time()
    print("Stopwatch started. Press Enter again to stop.")

    while True:
        elapsed_time = time.time() - start_time
        display_time(elapsed_time)
        time.sleep(300)
    
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    display_time(elapsed_time)
    print("\nStopwatch stopped.")

if __name__ == "__main__":
    import select
    stopwatch()

