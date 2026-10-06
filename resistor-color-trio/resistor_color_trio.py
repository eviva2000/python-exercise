COLORS = [
    "black", "brown", "red", "orange", "yellow",
    "green", "blue", "violet", "grey", "white",
]

PREFIXES = ["", "kilo", "mega", "giga"]


def label(colors):
    first, second, third = (COLORS.index(color) for color in colors[:3])
    value = (first * 10 + second) * 10 ** third

    magnitude = 0
    while value >= 1000 and magnitude < len(PREFIXES) - 1:
        value //= 1000
        magnitude += 1

    return f"{value} {PREFIXES[magnitude]}ohms"
