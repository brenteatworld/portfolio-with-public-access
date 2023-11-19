#!/bin/python3

#import necessary modules for server to function correctly for chat program - socket for network connections on LAN and threading for multi client connection
import socket
import threading

#create new socket using IPv4 addressing (AF_INET) and TCP (SOCK_STREAM)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#associate socket with specific network interface/port number.
server.bind(("0.0.0.0, #port number to be added"))
#limit of five connections before refusing connections
server.listen(5)


#clients keeps track of connected clients in a dictionary
clients = {}
#audit log keeps a log of messages about user activity
audit_log = []


