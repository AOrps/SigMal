import socket # for connecting via sockets 
# pip install socket


def port_open(host, port):
    """
    port_open: determines if the port is open
        host: the addr of machine you wish to figure out
        port: the port number you want to try to connect to
    return: (bool)
    """
    s = socket.socket() #creating a socket object 

    # Does error handling to figure out the port is open or closed.
    try:
        s.connect((host, port))
    except:
        return False
    else:
        return True


def portscan(host, max_range):
    for port in range(1, max_range):
        if port_open(host, port):
            print(f"Port {port} is open")



def main():
    portscan("127.0.0.1", 2800)  #localhost


if __name__ == "__main__":
    main()