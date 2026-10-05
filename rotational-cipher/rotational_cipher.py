def rotate(text, key):
    result = []
    for char in text:
        if char.isupper():
            result.append(chr((ord(char) - ord("A") + key) % 26 + ord("A")))
        elif char.islower():
            result.append(chr((ord(char) - ord("a") + key) % 26 + ord("a")))
        else:
            result.append(char)
    return "".join(result)
