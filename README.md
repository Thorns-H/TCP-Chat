# TCP - Chat

This script emulates a chat room using the TCP protocol and the [socket](https://docs.python.org/3/library/socket.html) 
module with his low-level networking interface and the [thread](https://docs.python.org/3/library/threading.html) 
module to create multiple clients.

## To Run
First set up the server : 
```
python3 helpers/server.py
```
And run the client script on another terminal :
```
python3 client.py
```
**ⓘ Important:** <br />
* You can change the server address and the port editing the ```settings/config.json``` file.
* To run this properly remember to start the server first.
* Do not change the unicode setting if you're using the AF_INET socket type.