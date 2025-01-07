import socket
import subprocess
import platform
def check_os():
  command = "echo $HOME"
  result = subprocess.run(command, shell=True, capture_output=True, text=True)
  if "/data/data/com.termux/files/home" in result.stdout:

    while True:
      host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      try:
        host.bind(('localhost', 4443))
        host.listen()
        conex, addr = host.accept()
        file_name = conex.recv(1024).decode()
        with open(file_name, 'rb') as file:
          for data in file.readlines():
            conex.send(data)
        print(f"File {file_name} has sent")
        conex.close()
      except:
        print("Something is wrong")
    elif "Linux" in platform.system():

      while True:
        host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
          host.bind(('localhost', 4443))
          host.listen()
          conex, addr = host.accept()
          file_name = conex.recv(1024).decode()
          with open(file_name, 'rb') as file:
            for data in file.readlines():
              conex.send(data)
          print(f"File {file_name} has sent")
          conex.close()
        except:
          print("Something is wrong")
    else:
      print("Unknown Error")
  
  
  
