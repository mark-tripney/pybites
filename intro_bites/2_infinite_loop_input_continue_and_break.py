VALID_COLORS = ["blue", "yellow", "red"]


def print_colors():
    """In the while loop ask the user to enter a color,
    lowercase it and store it in a variable. Next check:
    - if 'quit' was entered for color, print 'bye' and break.
    - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
    - otherwise print the color in lower case."""
    while True:
        user_colour = input("Please enter a color: ")
        if user_colour.lower() == "quit":
            print("bye")
            break
        else:
            if user_colour in VALID_COLORS:
                print(user_colour.lower())
            else:
                print("Not a valid color")
                continue
