def is_valid(isbn):
    digits = isbn.replace("-", "")
    if len(digits) != 10:
        return False

    total = 0
    for position, char in enumerate(digits):
        if char.isdigit():
            value = int(char)
        elif char == "X" and position == 9:
            value = 10
        else:
            return False
        total += value * (10 - position)

    return total % 11 == 0
