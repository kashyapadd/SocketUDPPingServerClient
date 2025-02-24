# UDPPingerClient.py
import random

from socket import *

import time

serverName = "127.0.0.1" # Creating the server name

serverPort = 12000     # Creating the server port

clientSocket = socket(AF_INET, SOCK_DGRAM) # Creating the socket for the server

clientSocket.settimeout(1.0) # Setting the timeout to 1 second

sequence_number = 1

Pingtime = time.time()

try:

      inputmessage = raw_input ('pingtime, sequence_number:') # Taking input message from the user

      clientSocket.sendto(inputmessage,(serverName, 12000))   # Sending the input message to the server.

      message,serveraddress = clientSocket.recvfrom(1024)     # Receive the response from the server

      timegap = (time.time() - Pingtime)                      # Calculating the timegap between sending and receving the message.

      #print message           

      print 'RTT is:' +str(timegap)                           # Printing the RTT(Round trip time)

      sequence_number += 1

except timeout:

    print 'Request timed out'

while sequence_number > 12:

    clientSocket.close()                                      # Closing the corresponding socket.

