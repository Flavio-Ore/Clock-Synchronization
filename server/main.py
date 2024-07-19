# Python3 program imitating a clock server
import socket
import datetime

# function used to initiate the Clock Server
def initiateClockServer():
	s = socket.socket()
	print("Socket successfully created")
	
	# Server port
	port = 3333
	host = '192.168.1.44'
	s.bind(('', port))
	
	# Start listening to requests
	s.listen(5)	 
	print("Socket is listening...")
	
	serverStatus = True
 
	# Clock Server Running forever
	while serverStatus:
		# Establish connection with client
		connection, address = s.accept()
		print('Server connected to', address)
		# Respond the client with server clock time
		connection.send(str(datetime.datetime.now()).encode())
		connection.close()

# Driver function
if __name__ == '__main__':

	# Trigger the Clock Server 
	initiateClockServer()
