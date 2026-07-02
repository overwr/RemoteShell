import socket as SocketLib
import Settings

def Bind(Socket, Ip, Port):
    try:
        Socket.bind((Ip, Port))
    except:
        return -1 
    return 0

def SendAndEncode(Socket, Message): return Socket.send(Message.encode())

def Send(Socket, Message): return Socket.send(Message)

def CreateSocket(Ipv, Protocol): return SocketLib.socket(Ipv, Protocol)

def RecvAndDecode(Socket, Frame): 
    Message = Socket.recv(Frame).decode()
    return Message

def Recv(Socket, Frame): return Socket.recv(Frame)

def CheckAndPrint(Flag, Message):
    if Flag:
        print(Message)
