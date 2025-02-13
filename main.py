from utilities import Color
import error_handler
b, i, u, e = Color.BOLD, Color.ITALIC, Color.UNDERLINE, Color.END # Terminal text format.
g, y, r, w = Color.GREEN, Color.YELLOW, Color.RED, Color.WHITE # Terminal color format.

def main():
    while True:
        user_input = input(f'{w}>> Type {b}"Window"{e}{w} or {b}"Terminal"{e}{w} for the respective mode...\n  {u}>{e} ')
        if user_input.lower() in ['window', 'win']:
            print(f'{w}>> Entering... {i}Window Mode{e}{w}.{e}')
            return 'window'
        elif user_input.lower() in ['terminal', 'term']:
            print(f'{w}>> Entering... {i}Terminal Mode{e}{w}.{e}')
            return 'terminal'
        else:
            error_handler.error_catcher(0)

if __name__ == '__main__':
    main()