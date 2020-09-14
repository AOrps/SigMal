import socket # for connecting


def port_open(host, port):
    s = socket.socket()
    try:
        s.connect((host, port))
    except:
        return False
    else:
        return True


def portscan(host, max_range):
    for port in range(1, max_range):
        if port_open(host, port):
            print(f"{port} is open")



def main():
    portscan("127.0.0.1", 1024)


if __name__ == "__main__":
    main()