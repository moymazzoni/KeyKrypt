"""MODULE utilities.py contains utilities for color coding and text formatting in the terminal."""
# Credit to: https://stackoverflow.com/a/17303428

class Color:
    """ANSI escape sequences for terminal text formatting."""
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    ITALIC = '\x1B[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

b, i, u, e = Color.BOLD, Color.ITALIC, Color.UNDERLINE, Color.END  # Text formatting
g, y, r, w = Color.GREEN, Color.YELLOW, Color.RED, Color.WHITE  # Text colors

# Define import items.
__all__ = ['b', 'i', 'u', 'e', 'g', 'y', 'r', 'w']
