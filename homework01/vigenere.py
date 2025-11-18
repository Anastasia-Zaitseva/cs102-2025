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
    keyword = (keyword * (len(plaintext) // len(keyword) + 1))[: len(plaintext)]
    pos = 0
    num_A = ord("A")
    num_Z = ord("Z")
    alph = 26
    for word in plaintext:
        shift = ord((keyword[pos]).upper()) - num_A
        pos += 1
        is_lowercase = not word.isupper()
        word = word.upper()
        if word.isalpha():
            code = ord(word) + shift
            if code > num_Z:
                code -= alph
            ciphertext += chr(code).lower() if is_lowercase else chr(code)
        else:
            ciphertext += word
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
    keyword = (keyword * (len(ciphertext) // len(keyword) + 1))[: len(ciphertext)]
    pos = 0
    num_A = 65
    for word in ciphertext:
        shift = ord((keyword[pos]).upper()) - num_A
        pos += 1
        is_lowercase = not word.isupper()
        word = word.upper()
        if word.isalpha():
            code = ord(word) - shift
            if code < num_A:
                code += 26
            plaintext += chr(code).lower() if is_lowercase else chr(code)
        else:
            plaintext += word
    return plaintext