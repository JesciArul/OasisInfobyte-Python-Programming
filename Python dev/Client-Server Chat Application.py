import socket

HOST = 'localhost'  
PORT = 12345       


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Server listening on {HOST}:{PORT} ...")

    conn, addr = server.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            print("Client disconnected.")
            break
        if data.lower() == 'exit':
            print("Client requested to exit.")
            break

        print(f"Client: {data}")
        reply = input("Server: ")
        conn.send(reply.encode())

except Exception as e:
    print("Error:", e)
finally:
    conn.close()
    server.close()
    print("Server closed.")