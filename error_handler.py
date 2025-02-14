"""MODULE error_handler.py ensures that any errors get treated efficiently."""

from utilities import Color
b, i, u, e = Color.BOLD, Color.ITALIC, Color.UNDERLINE, Color.END # Terminal text format.
g, y, r, w = Color.GREEN, Color.YELLOW, Color.RED, Color.WHITE # Terminal color format.
def error_catcher(x, *args):
    """Function "error_catcher()" catches potential errors that could occur and returns safely."""
    match x:
        case 0: # General input is invalid.
            print(f'{b}{r}>> ERROR: {e}{i}{r}Not a valid input!{e}')
            return
        case 1: # General file was not found.
            print(f'{b}{r}>> ERROR: {e}{i}{r}File {args} was not found!{e}')
        case 2:
            print()