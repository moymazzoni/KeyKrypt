# / Used for the terminal to display color, bold, italic,
# \ and other forms of text.
# Credit to: https://stackoverflow.com/a/17303428
class Color:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    ITALIC = '\x1B[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'