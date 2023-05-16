def gcd(a , b):
  while b != 0:
    a , b = b , a % b
  return a

def encryption(pk , pt):
  e , n = pk
  return pow(pt,e,n)

def decryption(pk , ct):
  d , n = pk
  return pow(ct,d,n)

def main():
  p = int(input("Enter large prime number : "))#3
  q = int(input("Enter large prime number : "))#11
  n = p * q
  phi = (p - 1)*(q - 1)
  e = 2
  while gcd(e , phi) != 1:
    e += 1
  d = pow(e , -1,phi) 

  public_key = (e,n)
  private_key = (d,n)
  
  plain_text = int(input("Enter plain text :"))#31
  
  ct = encryption(public_key , plain_text)
  print("Encrypted",ct)
  
  pt = decryption(private_key , ct)
  print("Decrypted",pt)

main()


# import math
# def find_e(p,phi_n):
# for i in range(p,phi_n):
# if math.gcd(i,phi_n) == 1:
# return i
# def find_d(e,phi_n,q):
# for k in range(1,phi_n):
# temp=(1+k*phi_n)/e
# int_temp=int(temp)
# if temp==int_temp:
# return int_temp
# def encrypt_rsa(f,g,plain):
# cipher = int(pow(plain,((f - 1)//2)) % ((g + 1)//2))
# return cipher
# def decrypt_rsa(d,g,cipher):
# decipher=int((pow(cipher,d)) % ((g+1)//2))
# return decipher
# p = int(input("Enter a prime number p : "))
# q = int(input("Enter a prime number q : "))
# n = p*q
# print("n : ",n)
# phi_n = (p-1)*(q-1)
# print("phi_n : ",phi_n)
# e = find_e(p,phi_n)
# print("e : ",e)
# f = (e * 2) + 1
# g = (n * 2) - 1
# d = find_d(e,phi_n,q)
# print("d : ",d)
# print("Public key : ",f,g)
# print("Private key : ",d,g)
# plain = int(input("Enter plain text : "))
# cipher = encrypt_rsa(f,g,plain)
# decipher = decrypt_rsa(d,g,cipher)
# print("Cipher text : ",cipher)
# print("Decipher text : ",decipher)
