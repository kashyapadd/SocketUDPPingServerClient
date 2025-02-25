# SocketUDPPingServerClient

1.Study a simple Internet ping server written in the Python and then implement a corresponding
client using ping protocol allowing a client machine to send a packet of data to a remote machine and have the remote
machine return the data back to the client unchanged
2. Develop a client code by studying the server code considering the packet loss, specific message format
3. Developed Client code should include
  (A) send the ping message using UDP (Note: Unlike TCP, you do not need to establish a connection
  first, since UDP is a connectionless protocol.),
  (B) print the response message from server, if any
  (c) calculate and print the round trip time (RTT), in seconds, of each packet, if the server responds;
  otherwise, print “Request timed out”
  (D) report the minimum, maximum, median, and mean RTTs at the end of all pings from the
  client.
4. Message Format - Ping time sequence_number
