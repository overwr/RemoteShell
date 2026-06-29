import socket 

ip = "127.0.0.1"
port = 9776
timeout = 1
cc = "---" # command to stop the program


def Start():

    msg = None

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    try:
        sock.connect((ip, port))
    except:
        print('Could not connect...')


    while msg != cc:
        msg = input()

        try:
            sock.send(msg.encode())
        except:
            print('Could not send...')
        out = sock.recv(4096).decode()
        print(f'output:\n {out}')

        if msg == 's[exit]':
            sock.close()
            return
            


    sock.close()





if __name__ == "__main__":
    Start()
    print('EOP')