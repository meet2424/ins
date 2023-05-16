def encryption(text , key):
  key_list = sorted(list(key))
  
  matrix = []
  n = len(text)
  row = len(key)
  i = 0
  index = 0
  while i < n:
    matrix.append([])
    for _ in range(row):
      if i < n:
        matrix[index].append(text[i])
      else:
        matrix[index].append("#")
      i += 1
    index += 1
  print(matrix)
  
  row_size = len(matrix)
  col_size = row
  cipher_text = ""
  i = 0
  
  for _ in range(len(key_list)):
    if i != 0 and key_list[i-1] == key_list[i]:
      curr_index = key.index(key_list[i]) + 1
    else:
      curr_index = key.index(key_list[i])
    for j in range(row_size):
      cipher_text += matrix[j][curr_index]
    i += 1
  return cipher_text

def decryption(text , key):
  row = int(len(text) / len(key))
  matrix = []

  for _ in range(row):
    matrix.append(['a'] * len(key))
  
  key_list = sorted(list(key))
  i = 0
  c_t = 0
  
  for _ in range(len(key_list)):
    if i != 0 and key_list[i-1] == key_list[i]:
      curr_index = key.index(key_list[i]) + 1
    else:
      curr_index = key.index(key_list[i])
    for j in range(row):
      matrix[j][curr_index] = text[c_t]
      c_t += 1
    i += 1
  
  pt = ""
  
  for i in range(row):
    pt += "".join(matrix[i])
  return pt

if __name__ == "__main__":
  key = input("Enter the key : ")
  text = input("Enter the text : ")
  ct = encryption(text , key)
  print("Encrypted Text : ",ct)
  pt = decryption(ct , key)
  print("Decrypted Text : ",pt)