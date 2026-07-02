import socket as SocketLib
import Settings
import Functions
import time as Time


def Start():

    Message = Settings.VoidString

    Socket = Functions.CreateSocket(SocketLib.AF_INET, SocketLib.SOCK_STREAM)

    while True:
        try:
            Socket.connect((Settings.ServerIp, Settings.ServerPort))
            break
        except:
            Functions.CheckAndPrint(Settings.DebugOutputFlag, Settings.ConnectErrorMessage)
            Functions.CheckAndPrint(Settings.DebugOutputFlag, Settings.TimeoutMessage)
            Time.sleep(Settings.Timeout)



    while Message != Settings.ClientEndCommand:
        Functions.CheckAndPrint(Settings.DebugOutputFlag, Settings.OutputSplitter)


        Message = Settings.VoidString
        while Message == Settings.VoidString:
            Message = input()
   
        if Message == Settings.ClientEndCommand:
            Socket.close()
            return Settings.SuccessfulCode

        try:
            Functions.SendAndEncode(Socket, Message)
        except:
            Functions.CheckAndPrint(Settings.DebugOutputFlag, Settings.SendErrorMessage)
        Output = Functions.RecvAndDecode(Socket, Settings.Frame)
        Functions.CheckAndPrint(Settings.DebugOutputFlag, Output)
            


    Socket.close()

    return Settings.SuccessfulCode





if __name__ == "__main__":
    Start()
    print('EOP')
