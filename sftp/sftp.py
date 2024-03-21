import pysftp as sftp
import os
import time

host = 'test.rebex.net'
port = 22
username = 'demo'
password= 'password'

cnopts = sftp.CnOpts()
cnopts.hostkeys = None

while(True):
  try:
    conn = sftp.Connection(host=host,port=port,username=username, password=password, cnopts=cnopts)
    print("Connection established successfully!")
    conn.get('/pub/example/ResumableTransfer.png')
  except:
    print('Failed to establish connection to targeted server')

  # Wait for 5 seconds.
  time.sleep(5)

  # Specify the file name you want to delete
  file_to_delete = "ResumableTransfer.png"

  # Get the current working directory
  current_directory = os.getcwd()

  # Create the full path to the file
  file_path = os.path.join(current_directory, file_to_delete)

  # Check if the file exists before attempting to delete
  if os.path.exists(file_path):
      # Delete the file
      os.remove(file_path)
      print(f"{file_to_delete} has been deleted.")
  else:
      print(f"{file_to_delete} does not exist in the current working directory.")
