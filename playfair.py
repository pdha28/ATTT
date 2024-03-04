def generate_playfair_key(key):
    key = key.replace(" ", "").upper()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_square = ""

    for char in key:
        if char not in key_square:
            key_square += char

    for char in alphabet:
        if char not in key_square:
            key_square += char

    return key_square

def playfair_encrypt(plain_text, key):
    key_square = generate_playfair_key(key)
    plain_text = plain_text.replace(" ", "").upper()
    encrypted_text = ""
    plain_text = plain_text.replace("J", "I")

    if len(plain_text) % 2 != 0:
        plain_text += "X"

    for i in range(0, len(plain_text), 2):
        char1 = plain_text[i]
        char2 = plain_text[i+1]

        row1, col1 = divmod(key_square.index(char1), 5)
        row2, col2 = divmod(key_square.index(char2), 5)

        if row1 == row2:
            encrypted_text += key_square[row1 * 5 + (col1 + 1) % 5]
            encrypted_text += key_square[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += key_square[((row1 + 1) % 5) * 5 + col1]
            encrypted_text += key_square[((row2 + 1) % 5) * 5 + col2]
        else:
            encrypted_text += key_square[row1 * 5 + col2]
            encrypted_text += key_square[row2 * 5 + col1]

    return encrypted_text

# Vi du
plaintext = "HELLO"
key = "PLAYFAIREXAMPLE"
print("Plain text:", plaintext)
print("Key:", key)
print("Encrypted text:", playfair_encrypt(plaintext, key))
