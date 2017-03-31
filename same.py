import wave, struct, math

#constants
preamble = '10101011101010111010101110101011101010111010101110101011101010111010101110101011101010111010101110101011101010111010101110101011'
footer = '01001110010011100100111001001110'
highbit = 2083.3
lowbit = 1562.5
bitlength = 0.00192


def binencode(arg):
 c = ''
 for s in arg:
  c+=''.join(str(ord(s) >> i & 1) for i in range(8)[::-1])
 return c


def sameencode(message):
 encodedmessage = preamble + binencode(message)
 wavef = wave.open('same.wav', 'w')
 wavef.setnchannels(1)
 wavef.setsampwidth(2)
 wavef.setframerate(44100)
 for s in encodedmessage:
  sb = 0.0
  if s == "1":
   sb = highbit
  else:
   sb = lowbit
  i = 0
  while i < bitlength*44100:
   value = int(16383.0*math.sin((2*math.pi)*(float(i/44100))*sb))
   data = struct.pack('<h', value)
   wavef.writeframesraw(data)
   i+=1

 wavef.close()
if __name__ == '__main__':
 headerinput = input("Enter message: ")  
 sameencode(headerinput)
