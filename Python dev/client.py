import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))  # Connect to your server

while True:
    msg = input("You: ")
    client.send(msg.encode())
    if msg.lower() == 'exit':
        break
    data = client.recv(1024).decode()
    print(f"Server: {data}")

client.close()