def encrypt_affine(plaintext: str, a: int, b: int) -> str:
    ciphertext = ""
    alphabet = ""
    for i in range(ord("а"), ord("я") + 1):
        alphabet += chr(i)
    m = len(alphabet)
    for char in plaintext:
        char_lower = char.lower()
        if char_lower in alphabet:
            x = alphabet.index(char_lower)
            encrypted_pos = (a * x + b) % m
            encrypted_char = alphabet[encrypted_pos]
            if char.isupper():
                ciphertext += encrypted_char.upper()
            else:
                ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

