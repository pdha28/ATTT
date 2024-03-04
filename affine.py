def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(plain_text, a, b):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
            else:
                encrypted_text += chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

# Vi du
plaintext = "HELLO"
a = 5
b = 7
print("Plain text:", plaintext)
print("a:", a)
print("b:", b)
print("Encrypted text:", affine_encrypt(plaintext, a, b))
