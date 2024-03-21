import subprocess
import time

while True:
    # Replace 'python3 seeder.py' with the actual command to execute 'seeder.py'
    command = "python3 /app/traffic_generator/torrent/seeder.py"
    
    # Use subprocess to run the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Wait for the process to finish
    process.wait()

    # Get the return code
    return_code = process.returncode
    print("Return Code:", return_code)

    # Optionally, add a delay before starting the command again
    time.sleep(10)  # Sleep for 60 seconds before restarting
