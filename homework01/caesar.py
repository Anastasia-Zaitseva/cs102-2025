def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    alph = 26
    lower_start = ord("a")
    upper_start = ord("A")
    for char in plaintext:
        if char.isalpha():
            base = upper_start if char.isupper() else lower_start
            shifted_char = chr((ord(char) - base + shift) % alph + base)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    alph = 26
    lower_start = ord("a")
    upper_start = ord("A")
    for char in ciphertext:
        if char.isalpha():
            base = upper_start if char.isupper() else lower_start
            shifted_char = chr((ord(char) - base - shift) % alph + base)
            plaintext += shifted_char
        else:
            plaintext += char
    return plaintext
