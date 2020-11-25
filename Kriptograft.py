class cipher():
  def __init__(self): 
    self.ref_stream_num = {num:char for num,char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    self.ref_stream_char= {char:num for num,char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}

  def to_number(self,char):
    return self.ref_stream_char[char]

  def to_char (self,number):
    return self.ref_stream_num[number]

  def cleaning_input (self, input):
    input           = input.upper()
    self.listchar   = [i for i in input]

class caesar_chipher(cipher):
  def __caesar_chipher(self,plain_text, key):
    plain_text          = self.cleaning_input(plain_text)
    self.keys           = key

  def function(self, char):
    return self.to_char((26+self.to_number(char)+self.keys)%26)

  def encode(self, plain_text, key):
    self.__caesar_chipher(plain_text, key)
    b    = map (self.function ,self.listchar)
    print(", ".join(list(b)))

  def decode(self, plain_text, key):
    self.__caesar_chipher(plain_text, (key*(-1)))
    b    = map (self.function ,self.listchar)
    print (", ".join(list(b)))

class vigenere_chipher(cipher):
  def __vigenere_chipher (self ,plain_text, key):
    self.cleaning_input(plain_text)
    key             = key.upper()
    self.key_stream = [ key[i%len(key)] for i in range(len(self.listchar)) ]
    data1 = map ( self.to_number , self.key_stream )
    data2 = map ( self.to_number , self.listchar )
    return data1, data2

  def calculate_cipher(self, char1, char2):
    return self.to_char((char1 + char2) % 26)
  
  def decipher(self, char1, char2):
    return self.to_char((26+(char2 - char1)) % 26)
  
  def encode(self, plain_text, key):
    data1, data2 = self.__vigenere_chipher(plain_text,key)
    result= map ( self.calculate_cipher, data1, data2 )
    print (list(result))

  def decode(self, plain_text, key):
    data1, data2 = self.__vigenere_chipher(plain_text,key)
    result= map ( self.decipher, data1, data2 )
    print (list(result))

class affine_cipher(cipher):
  def __affine_cipher(self, plain_text, key_a ,key_b):
    self.cleaning_input(plain_text)
    self.key_a, self.key_b = key_a, key_b
    return map (self.to_number, self.listchar)
  def encoder(self, number):
    temp = (number*self.key_a+self.key_b)%26
    return self.to_char(temp)
  
  def decoder(self, number):
    temp = key_a%26
    temp = (number*self.key_a+self.key_b)%26
    return self.to_char(temp)

  def encode (self, plain_text, key_a, key_b):
    self.cleaning_input(plain_text)
    self.key_a, self.key_b = key_a, key_b
    result = map (self.to_number, self.listchar)
    result = map (self.encoder, result)
    print(list(result))
  
  def decode (self, plain_text, key_a, key_b):
    result = self.__affine_cipher(plain_text,key_a,key_b)
    result = map (self.decoder, result)
    print(list(result))

    self.cleaning_input(plain_text)
    self.key_a, self.key_b = key_a, key_b
    result = map (self.to_number, self.listchar)

    self.cleaning_input(plain_text)
    self.key_a, self.key_b = key_a, key_b
    result = map (self.to_number, self.listchar)
text = vigenere_chipher() 
text.encode("decoder", 'key')
text.decode("niayhcb", 'key')
text = affine_cipher() 
text.encode("decoder", 3,5)
# text.decode("niayhcb", 3,5)