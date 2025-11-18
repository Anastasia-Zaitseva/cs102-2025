def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    extended_keyword = (keyword * (len(plaintext) // len(keyword) + 1))[: len(plaintext)]

    num_A = ord("A")
    num_Z = ord("Z")
    alph = 26
    for pos, char in enumerate(plaintext):
        shift = ord(extended_keyword[pos].upper()) - num_A
        is_lowercase = not char.isupper()
        char_upper = char.upper()
        if char_upper.isalpha():
            code = ord(char_upper) + shift
            if code > num_Z:
                code -= alph
            ciphertext += chr(code).lower() if is_lowercase else chr(code)
        else:
            ciphertext += char
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    extended_keyword = (keyword * (len(ciphertext) // len(keyword) + 1))[: len(ciphertext)]
    num_A = 65
    for pos, char in enumerate(ciphertext):
        shift = ord(extended_keyword[pos].upper()) - num_A
        is_lowercase = not char.isupper()
        char_upper = char.upper()
        if char_upper.isalpha():
            code = ord(char_upper) - shift
            if code < num_A:
                code += 26
            plaintext += chr(code).lower() if is_lowercase else chr(code)
        else:
            plaintext += char
    return plaintext
