import socket
import threading
import settings
import pathlib

path = pathlib.Path(__file__).parent.resolve()

HOST, PORT, UNICODE = settings.load_settings(path)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST,PORT))

server.listen()
print(f"Server running on {HOST}:{PORT}")

clients = []
usernames = []

def broadcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message)

def receive_connections():
    while True:
        client, address = server.accept()

        client.send("@username".encode("utf-8"))
        username = client.recv(1024).decode("utf-8")

        clients.append(client)
        usernames.append(username) 

        print(f"{username} is connected with {str(address)}")

        message = f"@SERVER: {username} joined the chat!".encode("utf-8")
        broadcast(message, client)

        client.send("Connected to the server".encode("utf-8"))

        thread = threading.Thread(target = handle_messages, args=(client,))

        thread.start()

def handle_messages(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = clients.index(client)
            username = usernames.index(index)

            broadcast(f"@SERVER: {username} disconnected".encode("utf-8"), client)

            clients.remove(client)
            usernames.remove(username)
            client.close()

            break

receive_connections()