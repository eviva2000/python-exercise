ACTIONS = ["wink", "double blink", "close your eyes", "jump"]


def commands(binary_str):
    number = int(binary_str, 2)
    actions = [action for i, action in enumerate(ACTIONS) if number & (1 << i)]
    if number & (1 << len(ACTIONS)):
        actions.reverse()
    return actions
