def lhs(para, shift):
  temp = []
  for i in range(len(para) - shift):
    temp.append(para[i + shift])
  temp.extend(para[0:shift])
  print(temp)
  ct.extend(temp)
def rhs(para, shift):
  temp = []
  for i in range(len(para)):
    temp.append(para[i - shift])
  print(temp)
  pt.extend(temp)
def encrypt(para, shift):
  paraA = ''
  paraB = ''
  for word in para:
    paraA = paraA + str(ord(word))
  print('The ASCII value of the paragraph is -')
  print(paraA)
  paraI = int(paraA)
  paraB = bin(paraI)
  paraB = paraB[2:]
  print('The binary value is -')
  print(paraB)

  print('The encrypted text is -')
  block = []
  pos = 0
  while paraB and pos < len(paraB):
    while pos < len(paraB):
      block.append(paraB[pos])
      pos = pos + 1
      if pos % 128 == 0:
        lhs(block, shift)
        block = []
        continue
  lhs(block, shift)
def decrypt(ct, shift):
  block = []
  pos = 0
  while ct and pos < len(ct):
   while pos < len(ct):
    block.append(ct[pos])
    pos = pos + 1
    if pos % 128 == 0:
      rhs(block, shift)
      block = []
      continue
  rhs(block, shift)

  text = ''
  for i in pt:
    text = text + i
  # print(text)
  paraA = str(int(text, 2))
  j = 0
  ans = ''
  while j < len(paraA):
    ans = ans + chr(int(paraA[j] + paraA[j + 1]))
    j = j + 2
  print('\nThe decrypted text is - ',ans) 

if __name__ == "__main__":
  pt = []
  ct = []
  para = input('Enter the paragraph to be encrypted : ')
  para = para.upper()
  shift = int(input('Enter the number of bits to be shifted by : '))
  encrypt(para, shift)
  decrypt(ct, shift)