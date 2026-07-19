import time as Time
import socket as SocketLib
import F 
import S
import sys


def Client():
    Message = S.VoidString
    Socket = F.CreateStart(S.ConnectCode)
    F.CommandLoop(Socket)
    Socket.close()
    return S.SuccessfulCode


def Server():
    Socket, ClientSocket = F.CreateStart(S.BindCode)
    if Socket == S.ErrorCode or Socket == None:
        F.CheckAndPrint("Socket error")
        return S.ErrorCodeFalse



    if F.GetAndExecute(Socket, ClientSocket) == S.SuccessfulCode:
        return S.SuccessfulCode # 0
    else: 
        return S.ErrorCode # -1
    
def GetCSAndStart(CSCode):
    if CSCode == S.CSClientCode:
        Client()
        F.CheckAndPrint("Client")
    elif CSCode == S.CSServerCode:
        F.CheckAndPrint("Server")
        Server()
    return 0

if __name__ == "__main__":
    GetCSAndStart(int(sys.argv[1]))

    