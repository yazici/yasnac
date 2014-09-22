import serial, time


class YASNAC():  # a classs to handle the yasnac
  def __init__(self):
    self.com = serial.Serial(port='/dev/ttyS0', baudrate=4800,parity=serial.PARITY_EVEN) 
    #initialize the class a connection to the serial port
    time.sleep(4)# wait for the port to be ready (this is an arbitrary period) 
  

  def rx(self, cue):
    print self.com.readlines()
    """inq = self.com.readlines()
    print(inq)
    if inq:  #if the inquiry ezists 
      if cue in inq:
       return(True)
    elif cue == None:
      return(inq)
    return(False)"""
      
  def  tx(self, response): # automatic or custom reply
    if response is None: 
      response = "02030041434B2Eff".encode("hex") 
    self.com.write("{0}".format(response))
  
  #rx() and tx() are the two most basic methods of this class
  #handshake is an example of combining rx() and tx() 
  
  def handshake(self): # press flesh with the yasnac
    if(self.rx("ENQ")  == True):  #default value for handshake
      self.tx(None) #default value for handshake 
    else:
      print("handshake failed, no inquiry heard")    
    return(self.rx(None))  #ready for the next step

  def list_files(self, filenames): #filenames as a single string in ASCII separated by FOUR (4) spaces
    self.tx("0273004C5354{0}1FE0".format(filenames.encode("hex")))
    
    if self.rx("ACK") == True:
      self.tx("020300454F4623".decode("hex"))
      if self.rx("EOT") == True:
        print("filenames sent... proceeding")
        
# some procedural style stuff to get you started:
moto = YASNAC()  #instantiate the class
while True:
  moto.rx(None)
"""if "LST" in moto.handshake():
  moto.list_files()
else:
  print ("no list requested")
  exit(0)
"""