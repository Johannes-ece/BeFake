import subprocess
import time
import threading
#subprocess.call(["python3", "./befake.py", "login", "+61493447823"])

def heartbeat():
    while True:
        print("Heartbeat")
        time.sleep(60)  # wait for 60 seconds

def run_script():
    while True:
        subprocess.call(["python3", "./befake.py", "feed", "friends-v1"])
        time.sleep(1800)  # wait for 3600 seconds (1 hour)

# create a thread for the heartbeat function that runs alongside the main program
threading.Thread(target=heartbeat).start()

# run the script
run_script()
