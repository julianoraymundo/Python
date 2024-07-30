import curses
import random
import time

def initialize_curses():
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    stdscr.keypad(True)
    return stdscr

def cleanup_curses(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def main(stdscr):
    # Set up colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Define characters
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    # Define line parameters
    line_spacing = 1
    max_y, max_x = stdscr.getmaxyx()
    num_lines = max_x // 2  # Half the width of the terminal

    # Create a list of characters for each line
    lines = [[] for _ in range(num_lines)]

    try:
        # Main loop
        while True:
            # Clear the screen
            stdscr.clear()

            # Get updated dimensions
            max_y, max_x = stdscr.getmaxyx()
            num_lines = max_x // 2

            # Update lines list if number of lines has changed
            if len(lines) != num_lines:
                lines = [[] for _ in range(num_lines)]

            # Add a new character to each line
            for i in range(num_lines):
                char = random.choice(characters)
                lines[i].append(char)
                if len(lines[i]) > max_y:
                    lines[i].pop(0)

            # Draw lines of characters
            for i, line in enumerate(lines):
                for j, char in enumerate(line):
                    if j * line_spacing < max_y:
                        stdscr.addstr(j * line_spacing, i * 2, char, curses.color_pair(1))

            stdscr.refresh()
            time.sleep(0.1)

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    stdscr = initialize_curses()
    curses.wrapper(main)
    cleanup_curses(stdscr)
