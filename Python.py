def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    return encrypt(message, -shift)

# Ejemplo de uso
plaintext = "Hola, este es un mensaje de prueba!"
shift = 3
ciphertext = encrypt(plaintext, shift)
decrypted_text = decrypt(ciphertext, shift)

print("Texto original:", plaintext)
print("Texto cifrado:", ciphertext)
print("Texto descifrado:", decrypted_text)
