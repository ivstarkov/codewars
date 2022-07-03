def decrypt(encrypted_text, n):
    for _ in range(n):
        text = list(encrypted_text)
        for i in range(len(encrypted_text) // 2):
            text[i * 2 + 1] = encrypted_text[i]
            text[i * 2] = encrypted_text[i + len(encrypted_text) // 2]
        encrypted_text = "".join(text)

    return encrypted_text


def encrypt(text, n):
    for _ in range (n):
        encrypted_text = ""
        for x in text[1::2]:
            encrypted_text += x
        for x in text[::2]:
            encrypted_text += x
        text = encrypted_text

    return text
            

print(encrypt("0123456", 2))
print(decrypt(encrypt("0123456", 2), 2))