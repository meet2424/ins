def get_num(c):
  return ord(c.lower()) - 97

def get_char(n):
  return chr(n+97)

def encryption(text,a,b):
  # (ax+b) mod 26
  cipher = ""
  for i in text: 
    cipher += get_char((a*get_num(i)+b)%26)

  return cipher

def decryption(text,a,b):
  # c*(x-b) mod 26
  c = pow(a , -1,26)
  pt = ""

  for i in text:
    pt += get_char(c*(get_num(i)-b)%26)
  return pt

if __name__ == "__main__":
  text = input("Enter plain text : ")#Hello world
  a = int(input("Enter value of a : "))#5
  b = int(input("Enter valur of b : "))#8
  ct = encryption(text , a , b)
  print("Encrypted",ct)
  pt = decryption(ct , a,b)
  print("Decrypted",pt)