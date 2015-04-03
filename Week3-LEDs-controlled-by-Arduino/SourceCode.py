import serial, mosquitto, random # importing libraries

client = mosquitto.Mosquitto("DAT205") #connect to Broker
client.connect("127.0.0.1")

client.subscribe("arduino")

port = serial.Serial("/dev/tty.usbmodem1411", 9600, timeout=2) # connnect to arduino to working serial port
input = port.readline()

def messageReceived(broker, obj, msg): # get the message from broker and push date to connected arduino
  global client
  print("Message " + msg.topic + " containing: " + msg.payload)
  port.write(str(msg.payload))

# client = None

client.on_message = messageReceived #confirms that message was received
	while (True): 
		client.loop()


# for i in range(1,10):
#   port.write('1')
#   time.sleep(1)
#   port.write('0')
#   time.sleep(1)
