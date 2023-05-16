def get_num(c):
  return ord(c.lower()) - 97

def get_char(n):
  return chr(n+97)

def encryption(string , key):
  cipher_text = ""
  for i in string:
    cipher_text += get_char((get_num(i)+key) % 26)
  return cipher_text

def decryption(string,key):
  plain_text = ""
  for i in string:
    plain_text += get_char((get_num(i)-key) % 26)
  return plain_text

if __name__ == "__main__":
  text = input("Enter plain text : ")
  key = int(input("Enter the key : "))
  ct = encryption(text , key)
  print(f"Encrypted text: {ct}") 
  pt = decryption(ct , key)
  print(f"\nDecrypted text: {pt}") 