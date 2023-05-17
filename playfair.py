# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y','z']

# def get_position(letter , matrix):
#   for i in range(5):
#     for j in range(5):
#       if matrix[i][j] == letter:
#         return i ,j

# def digraphs(plain_text):
#   text = []
#   i = 0
#   j = 1
#   n = len(plain_text)

#   while i < n and j < n:
#     if plain_text[i] != plain_text[j]:
#       text.append([plain_text[i], plain_text[j]])
#       i += 2
#       j += 2
#     else:
#       text.append([plain_text[i],"x"])
#       i += 1
#       j += 1
#   if i < n:
#     text.append([plain_text[i],"x"])
#   return text

# def encrypt(matrix , text):
#   encrypted_text = ""
#   print(text)
#   for i in range(len(text)):
#     x1 , y1 = get_position(text[i][0] , matrix)
#     x2 , y2 = get_position(text[i][1] , matrix)
#     if x1 == x2:
#     # same row
#       encrypted_text += matrix[x1][(y1+1)%5]
#       encrypted_text += matrix[x2][(y2+1)%5]
#     elif y1 == y2:
#       # same column
#       encrypted_text += matrix[(x1+1)%5][y1]
#       encrypted_text += matrix[(x2+1)%5][y2]
#     else:
#       # intersection
#       encrypted_text += matrix[x1][y2]
#       encrypted_text += matrix[x2][y1]
#   return encrypted_text

# def decrypt(matrix , text):
#   encrypted_text = ""
#   print(text)
#   for i in range(len(text)):
#     x1 , y1 = get_position(text[i][0] , matrix)
#     x2 , y2 = get_position(text[i][1] , matrix)
#     if x1 == x2:
#       # same row
#       encrypted_text += matrix[x1][(y1-1)%5]
#       encrypted_text += matrix[x2][(y2-1)%5]
#     elif y1 == y2:
#       # same column
#       encrypted_text += matrix[(x1-1)%5][y1]
#       encrypted_text += matrix[(x2-1)%5][y2]
#     else:
#       # intersection
#       encrypted_text += matrix[x1][y2]
#       encrypted_text += matrix[x2][y1]
#   return encrypted_text

# def generate_matrix(key):
#   temp_list = []
#   for i in key:
#     if i not in temp_list:
#       temp_list.append(i)
#   for i in alphabets:
#     if i not in temp_list:
#       temp_list.append(i)
#   matrix = []
#   for i in range(5):
#     matrix.append(temp_list[:5])
#     temp_list = temp_list[5:]
#   return matrix

# if __name__ == "__main__":
#   key = input("Enter the key : ")
#   plain_text = input("Enter plain text : ")
#   matrix = generate_matrix(key)
#   print()
#   digraphs_text = digraphs(plain_text)
#   cipher_text = encrypt(matrix , digraphs_text)
#   print()
#   print("Encrypted text : ",cipher_text)
#   print()
#   c_digraphs_text = digraphs(cipher_text) 
#   print("\nPlain text : ",decrypt(matrix ,c_digraphs_text))

def generate_key_matrix(key):
    # Generating the key matrix
    key = key.replace("J", "I")  # Replacing 'J' with 'I'
    key = key.upper()
    key_matrix = []
    chars_added = set()
    
    # Adding the key characters to the matrix
    for char in key:
        if char not in chars_added:
            key_matrix.append(char)
            chars_added.add(char)
    
    # Adding the remaining alphabet characters to the matrix
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in chars_added:
            key_matrix.append(char)
            chars_added.add(char)
    
    return key_matrix

def preprocess_message(message):
    # Preprocessing the message
    message = message.replace("J", "I")  # Replacing 'J' with 'I'
    message = message.upper()
    
    # Splitting the message into pairs of characters
    pairs = []
    i = 0
    while i < len(message):
        if i == len(message) - 1 or message[i] == message[i+1]:
            pairs.append(message[i] + "X")
            i += 1
        else:
            pairs.append(message[i] + message[i+1])
            i += 2
    
    return pairs

def get_position(matrix, char):
  
    i=0
    while i<len(matrix):
        for j in range(5):
          if matrix[i+j] == char: 
              return int(i/5),j
        i+=5     

def encrypt_playfair(message, key):
    # Generating the key matrix
    key_matrix = generate_key_matrix(key)
    print(key_matrix)
    
    # Preprocessing the message
    pairs = preprocess_message(message)
    print(pairs)
    
    # Encrypting the pairs
    encrypted_pairs = []
    for pair in pairs:
        char1, char2 = pair[0], pair[1]
        
        # Finding positions of the characters in the key matrix
        row1, col1 = get_position(key_matrix, char1)
        print(row1,col1)
        row2, col2 = get_position(key_matrix, char2)
        print(row2,col2)
        
        # Applying the Playfair cipher rules
        if row1 == row2:
            encrypted_char1 = key_matrix[row1*5+col1 + 1]
            encrypted_char2 = key_matrix[row2*5+col2 + 1]
        elif col1 == col2:
            encrypted_char1 = key_matrix[(row1+1)*5+col1]
            encrypted_char2 = key_matrix[(row2 + 1)* 5+ col2]
        else:
            encrypted_char1 = key_matrix[row1*5+col2]
            encrypted_char2 = key_matrix[row2*5+col1]
        
        encrypted_pairs.append(encrypted_char1 + encrypted_char2)
        print(encrypted_pairs)
    
    # Combining the encrypted pairs into the final ciphertext
    ciphertext = "".join(encrypted_pairs)
    return ciphertext

def decrypt_playfair(message, key):
    # Generating the key matrix
    key_matrix = generate_key_matrix(key)
    print(key_matrix)
    
    # Preprocessing the message
    pairs = preprocess_message(message)
    print(pairs)
    
    # Encrypting the pairs
    encrypted_pairs = []
    for pair in pairs:
        char1, char2 = pair[0], pair[1]
        
        # Finding positions of the characters in the key matrix
        row1, col1 = get_position(key_matrix, char1)
        print(row1,col1)
        row2, col2 = get_position(key_matrix, char2)
        print(row2,col2)
        
        # Applying the Playfair cipher rules
        if row1 == row2: 
            encrypted_char1 = key_matrix[row1*5+(col1 - 1)]
            encrypted_char2 = key_matrix[row2*5+(col2 - 1)]
        elif col1 == col2: 
            encrypted_char1 = key_matrix[(row1-1)*5+col1]
            encrypted_char2 = key_matrix[(row2 - 1)* 5+ col2]
        else:
            encrypted_char1 = key_matrix[row1*5+col2]
            encrypted_char2 = key_matrix[row2*5+col1]
        
        encrypted_pairs.append(encrypted_char1 + encrypted_char2)
        print(encrypted_pairs)
    
    # Combining the encrypted pairs into the final ciphertext
    ciphertext = "".join(encrypted_pairs)
    return ciphertext

# Example usage
key = "MONARCHY"
message = "THISISANEASYTASK"
ciphertext = encrypt_playfair(message, key)
print("Ciphertext:", ciphertext)
print("Plaintext:", decrypt_playfair(ciphertext, key))
