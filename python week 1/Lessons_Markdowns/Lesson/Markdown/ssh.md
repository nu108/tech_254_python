What is SSH?- secure shell 

It is a cryptographic network protocol 

What is it used for ?

 used for secure remote communication between two computers over an unsecured network,
 such as the internet. It provides a secure way to access and manage remote systems and devices, allowing users to log in to a remote machine, execute 
 commands, and transfer files securely.
 
How does SSH work?
SSH (Secure Shell) works by establishing a secure encrypted connection between a client
(the computer initiating the connection) and a server(the remote computer or device being connected to). This secure connection allows
for secure remote access, file transfer, and various other network services.


What are private and public keys?

Private Key:

A private key is a secret cryptographic key that is kept confidential by its owner. 
It must never be shared with others.

Public Key:

A public key is derived from the private key and is intended to be shared openly.


Why use SSH? How does it increase security?

Encrypted Communication: SSH encrypts all data transmitted between the client and server. This encryption ensures that even if someone intercepts the network traffic, they won't be able to decipher the contents. This is crucial for protecting sensitive information, including passwords and data, during remote communication.

Secure Remote Access: SSH provides a secure means of remotely accessing and managing servers, network devices, and other systems. System administrators and developers can securely log in to remote machines over untrusted networks, such as the internet, without exposing login credentials to potential attackers.

Authentication Methods: SSH supports various authentication methods, including password-based authentication and public key authentication. Public key authentication, in particular, is highly secure because it requires possession of a private key to gain access. This reduces the risk of brute force attacks and password guessing. 

How to make a ssh key :

enter into terminal: ssh-keygen -t rsa -b 2048 

next enter:  ssh-keygen -t rsa -b 2048 -f /path/to/keyfile

"enter a pass phrase"