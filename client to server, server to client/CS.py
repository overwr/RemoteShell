import time as Time
import socket as SocketLib
import F 
import S
import sys


def Client():

    Message = S.VoidString

    
    Socket = F.CheckModeBLC(S.ClientSide)

    F.ConnectionLoop(Socket, S.ServerIp, S.ServerPort)

    F.CommandLoop(Socket)
            
    Socket.close()

    return S.SuccessfulCode


def Server():

    Socket = F.CheckModeBLC(S.ServerSide)
    if Socket == S.ErrorCode or Socket == None:
        F.CheckAndPrint("Socket error")
        return S.ErrorCodeFalse



    if F.GetAndExecute(Socket, Socket) == S.SuccessfulCode:
        return S.SuccessfulCode # 0
    else: 
        return S.ErrorCode # -1
    
def GetCSAndStart(CSCode):
    if CSCode == S.CSClientCode:
        Client()
    elif CSCode == S.CSServerCode:
        print("server")
        Server()
    return 0

if __name__ == "__main__":
    GetCSAndStart(int(sys.argv[1]))

    