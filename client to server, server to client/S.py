import socket as SocketLib

# Values
ClientToServerMode = 0
ServerToClientMode = 1
ServerQueue = 3
CSServerCode = 0 #CS - client_server
CSClientCode = 1
ClientSide = 101 #const
ServerSide = 100 #const
BindCode = 0
ConnectCode = 1


# NetworkConfiguration
ServerIp = "127.0.0.1"
ServerPort = 9050
AcceptingIp = ""
Timeout = 1
Frame = 1024
ServerQueue = 1
Mode = ClientToServerMode
ClientIp = "127.0.0.1"
ClientPort = 9050
IpV = SocketLib.AF_INET
Protocol = SocketLib.SOCK_STREAM



# Commands
ClientEndCommand = "-c-"
ServerEndCommand = "-s-"
SetDefaultShellCommand = "-d-"
RemoveDefaultShell = "-None-"

# Flags
DebugOutputFlag = True

# Return codes
VoidRetCode = None
SuccessfulCode = 0
ErrorCode = -1
ErrorCodeTrue = 1
ErrorCodeFalse = 0


# Strings
OutputSplitter = "****************************************************"
NDefaultShellCommandSplitter = ""
YDefaultShellCommandSplitter = " "
VoidString = ""
SpaceSplitChar = " "
BindErrorMSG = "Binding error... Change the port."
CommandWaitingMSG = "Waiting for command..."
RefusedConnectionMSG = "Connection was refused by client... Reaccepting..."
SetDefaultShellCommandMSG = "Set default shell command..."
DefaultShellMSG = "Now default shell is"
ShellErrorMSG = "Shell error... Check your command."
OutputCommandMSG = "Command:"
ConnectedClientMSG = "Client connected to server:"
EndOfProgramMSG = "End of program..."
RecvErrorMSG = "Could not receive message..."
RemovedDefaultShellMSG = "Default shell was reset..."
ConnectErrorMSG = "Could not connect..."
SendErrorMSG = "Could not send..."
TimeoutMSG = "Timeout..."
AcceptMSG = "Accepted."
RestartMSG = "Restart..."




