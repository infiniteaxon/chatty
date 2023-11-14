import socket
import Thread

# Server Connection Info
sHOST = socket.gethostbyname(socket.gethostname())
sPORT = 2003

# Initiate Client Sockets
cSOCKETS = set()
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create TCP Socket
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Set Socket to be Reusable
tcp.bind((sHOST, sPORT))  # Bind Socket to Server
tcp.listen(5)  # Only 5 Connection can queue at once
print(f"[*] Live on {sHOST}:{sPORT}")  # Print Socket Connection Info


# Function to Listen for Client Connections
def client_connect(cSOCKET):
    while True:
        try:
            message = cSOCKET.recv(1024).decode()  # Receive and decode message
        except Exception as e:  # If there's an error:
            print(f"[!] Error: {e}")  # Error handling
            cSOCKETS.remove(cSOCKET)  # Removes user from socket
        for clientSOCKET in cSOCKETS:  # For loop to send message to all connected users
            clientSOCKET.send(message.encode())  # Encode message for transit


while True:
    cSOCKET, uADDRESS = tcp.accept()  # Connects client to TCP Socket
    print(f"[+] {uADDRESS} connected.")  # Returns connection status if successful
    cSOCKETS.add(cSOCKET)  # Adds new Client to Socket list
    threading.Thread(target=client_connect, args=(cSOCKET,), daemon=True,).start()  # Sets up thread for each client, daemon ends threads when main ends


for clients in cSOCKETs:
    clients.close()
tcp.close()


for clients in cSOCKETs:
    clients.close()
tcp.close()
