"""FUNCTION error_catcher() catches potential errors that could occur and returns."""

from utilities import Color
b, i, u, e = Color.BOLD, Color.ITALIC, Color.UNDERLINE, Color.END # Terminal text format.
g, y, r, w = Color.GREEN, Color.YELLOW, Color.RED, Color.WHITE # Terminal color format.
def error_catcher(x):
    """Function "error_catcher()" catches potential errors that could occur and returns."""
    match x:
        case 0:
            print(f'{b}{r}>> ERROR: {e}{i}{r}Not a valid input!{e}')
            return
        case 1:
            print()
        case 2:
            print()