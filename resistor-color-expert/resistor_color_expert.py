COLORS = [
    "black", "brown", "red", "orange", "yellow",
    "green", "blue", "violet", "grey", "white",
]

PREFIXES = ["", "kilo", "mega", "giga"]

TOLERANCES = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}


def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"

    *digits, multiplier, tolerance = colors
    value = 0
    for digit in digits:
        value = value * 10 + COLORS.index(digit)
    value *= 10 ** COLORS.index(multiplier)

    magnitude = 0
    while value >= 1000 and magnitude < len(PREFIXES) - 1:
        value /= 1000
        magnitude += 1

    formatted_value = f"{value:g}"
    return f"{formatted_value} {PREFIXES[magnitude]}ohms ±{TOLERANCES[tolerance]:g}%"
