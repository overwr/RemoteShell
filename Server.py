import socket as SocketLib
import os
import subprocess
import F
import S
import time as Time



def Start():

    ServerSocket = F.CreateSocket(SocketLib.AF_INET, SocketLib.SOCK_STREAM)

    SockList = F.CheckMode_BLC(ServerSocket)
    if bool(SockList):
        F.CheckAndPrint(S.BindErrorMSG)
        return S.ErrorCodeFalse
        

    F.CheckAndPrint(SockList[1]) 



    if F.GetAndExecute(ServerSocket, SockList[0]) == S.SuccessfulCode:
        return S.SuccessfulCode # 0
    else: 
        return S.ErrorCodeTrue # 1


if __name__ == "__main__":
    F.CheckAndPrint(S.ServerIp)
    F.KeepConnectLoop(Start)
    F.CheckAndPrint(S.EndOfProgramMSG)
