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
    while True:
        message = f"{username}: {input('')}"
        client.send(message.encode("utf-8"))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")

            if message == "@username":
                client.send(username.encode("utf-8"))
            else:
                print(message)
        except:
            print("An error ocurred")
            client.close
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()