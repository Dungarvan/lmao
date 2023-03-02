import socket

HOST = '178.79.145.158'  
PORT = 451        


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))

    server_socket.listen()

    print(f"Waiting for a connection on {HOST}:{PORT}")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        cmd = input("Enter a command to send to the client: ")
        conn.sendall(cmd.encode())
        data = conn.recv(1024)
        print(f"Received data from {addr}: {data.decode()}")

