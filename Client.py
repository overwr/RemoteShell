import socket as SocketLib
import S
import F 
import time as Time


def Start():

    Message = S.VoidString

    Socket = F.CreateSocket(SocketLib.AF_INET, SocketLib.SOCK_STREAM)

    F.ConnectionLoop(Socket, S.ServerIp, S.ServerPort)

    F.CommandLoop(Socket)
            
    Socket.close()

    return S.SuccessfulCode





if __name__ == "__main__":
    Start()
    F.CheckAndPrint(S.EndOfProgramMSG)
