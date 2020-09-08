import socket

# Code yanked from: https://www.thepythoncode.com/article/create-reverse-shell-python 

SERVER_HOST = "0.0.0.0"   #0.0.0.0 is used so it may connect to all IPv4 addresses on local machine
SERVER_PORT = 3456      #Value can change to whatever port you want as long as it is over 1024

BUFFER_SIZE = 1024      #Send 1024bytes --> 1kb a time


s = socket.socket() # simply create a socket object 
# Initialized as a tcp socket
# --> Most malicious reverse shell use either port 80 (http) or 443 (https)
    # which will allow it to bypass firewall restrictions of the target client



