def value(colors):
    """Return the value of the first two resistor color bands."""
    color_code = {
        "black": "0",
        "brown": "1",
        "red": "2",
        "orange": "3",
        "yellow": "4",
        "green": "5",
        "blue": "6",
        "violet": "7",
        "grey": "8",
        "white": "9",
    }

    digits = []
    for index, color in enumerate(colors):
        if index >= 2:
            break
        digits.append(color_code[color])

    return int("".join(digits))
