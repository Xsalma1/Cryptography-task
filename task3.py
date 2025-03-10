def create_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace("J", "I") + "ABCDEFGHIKLMNOPQRSTUVWXYZ"))
    return [key[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for r in range(5):
        if letter in matrix[r]: return r, matrix[r].index(letter)

def playfair_cipher(text, matrix, shift):
    text = text.upper().replace("J", "I").replace(" ", "") 
    if len(text) % 2: text += "X"
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2: c1, c2 = (c1+shift)%5, (c2+shift)%5
        elif c1 == c2: r1, r2 = (r1+shift)%5, (r2+shift)%5
        else: c1, c2 = c2, c1
        result += matrix[r1][c1] + matrix[r2][c2]
    return result
key = input("Enter keyword: ")
matrix = create_matrix(key)
for row in matrix: print(" ".join(row).replace("I", "I/J", 1))
mode = 1 if input("Encrypt or Decrypt? ").lower() == "e" else -1
print("Output:", playfair_cipher(input("Enter text: "),matrix,mode)) 