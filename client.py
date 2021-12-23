import socket
import threading
import pathlib
from helpers import settings

path = pathlib.Path(__file__).parent.resolve()

HOST, PORT , UNICODE = settings.load_settings(path)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST,PORT))

username = input("Enter your username : ")

def write_messages():
    message = f"{username}: {input('')}"
    client.send(message.encode(UNICODE))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode(UNICODE)

            if message == "@username":
                client.send(username.encode(UNICODE))
        except:
            print("An error ocurred")
            client.close()
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()