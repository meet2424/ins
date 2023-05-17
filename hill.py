# import numpy as np
# def get_index(c):
#   return ord(c.lower()) - 97
# def get_char(n):
#   return chr(n+97)

# matrix = []

# def create_mat(key , size):
#   n = int(len(key) / size)
#   j = 0
#   for i in range(n):
#     matrix.append([])
#     for _ in range(size):
#       matrix[i].append(get_index(key[j]))
#     j += 1
#   print(matrix)

# def encryption(text , size):
#   pt = []
#   ct = []
#   cipher = ""
#   i = 0
#   n = len(text)
#   while i < n:
#     pt.append(list(text[i:i+size]))
#     i += size
#   print(pt)

#   for i in range(len(pt)):
#     for j in range(len(pt[0])):
#       pt[i][j] = get_index(pt[i][j])
#   for i in range(len(pt)):
#     ct.append(np.dot(matrix , pt[i]))
  
#   for i in range(len(ct)):
#     for j in range(len(ct[0])):
#       cipher += get_char(ct[i][j] % 26)
#   return cipher

# def multiplicative_insverse(dete):
#   m_l = -1
#   for i in range(26):
#     if (i * dete) % 26 == 1:
#       return i
#     i += 1
#   return m_l

# def decryption(text , size):
#   print(text)
#   ct = []
#   pt = []
#   i = 0
#   n = len(text)
#   while i < n:
#     ct.append(list(text[i:i+size]))
#     i += size
  
#   for i in range(len(ct)):
#     for j in range(len(ct[0])):
#       ct[i][j] = get_index(ct[i][j])
  
#   # inverse matrix
#   dete = matrix[0][0] * matrix[1][1] - matrix[1][0] *matrix[0][1]
#   dete = dete % 26
#   multi_inv = pow(dete,-1,26)
#   print(dete)
#   m_inverse = matrix
#   m_inverse[0][0] , m_inverse[1][1] = m_inverse[1][1] ,m_inverse[0][0]
#   m_inverse[0][1] *= -1
#   m_inverse[1][0] *= -1

#   for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#       m_inverse[i][j] *= multi_inv
#       m_inverse[i][j] = m_inverse[i][j] % 26
#   print(m_inverse)
  
#   for i in range(len(ct)):
#     pt.append(np.dot(m_inverse , ct[i]))

#   plain = ""
#   i = 0
#   j = 0
#   for i in range(len(pt)):
#     for j in range(len(pt[0])):
#       plain += get_char(pt[i][j] % 26)
#   print(plain)

# if __name__ == "__main__":
#   key = "CDDG"
#   size = 2
#   create_mat(key , size)
#   pt = "attack"
#   cipher = encryption(pt , size)
#   decryption(cipher , size)

import numpy as np

def normalize_text(x,n):
    newx=x
    p = len(x)%n
    for i in range(p):
        newx+="x"
    return newx

def encrypt(x,mat,n):
    if len(x)%n!=0:
        new_x = normalize_text(x,n)
    else:
        new_x=x
    cipher=""
    for i in range(0,len(new_x),n):
        temp=[]
        for j in range(n):
            temp.append(ord(new_x[i+j])-ord('a'))
        sol=np.dot(mat,temp)
        for j in sol:
            cipher+=chr((j%26)+ord('a'))
    return cipher
def decrypt(cipher,mat,n):
    text=""
    det=round(np.linalg.det(mat))
    new_det = pow(det,-1,26)
    adjoint = (np.linalg.inv(mat)*det)
    new_adj=[]
    for i in range(len(adjoint)):
        temp=[]
        for j in range(len(adjoint[i])):
            if adjoint[i][j]<0:
                temp.append((round(adjoint[i][j])+26)*new_det)
            else:
                temp.append(round(adjoint[i][j])*new_det)
            
        new_adj.append(temp)

    text = encrypt(cipher,new_adj,n)
    return text


def main():
    x="attack"
    n=2
    mat=[[2,3],[3,6]]
    print(mat)
    cipher = encrypt(x,mat,n)
    print("Encrypted Text: ",cipher)
    print()
    x_ = decrypt(cipher,mat,n)
    print("Decrypted Text: ",x_)
main()
