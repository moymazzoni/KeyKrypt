from utilities import Color
b, i, u, e = Color.BOLD, Color.ITALIC, Color.UNDERLINE, Color.END # Terminal text format.
g, y, r, w = Color.GREEN, Color.YELLOW, Color.RED, Color.WHITE # Terminal color format.

def main():
    while True:
        user_input = input(f'{w}>> Type {b}"Window"{e}{w} or {b}"Terminal"{e}{w} for the respective mode...{e}\n  >> ')
        if user_input.lower() in ['window', 'win']:
            print(f'>> Entering... {i}Window Mode.{e}')
            return 'window'
        elif user_input.lower() in ['terminal', 'term']:
            print(f'>> Entering... {i}Terminal Mode{e}.')
            return 'terminal'
        else:
            print(f'{r}>> {b}ERROR: {e}{i}{r}Not a valid input!{e}')

if __name__ == '__main__':
    main()