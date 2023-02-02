import numpy as np
import traceback
import sys

# Initialize the puzzle with a bidimensional array of integers
puzzle_22027 = np.array([
    [1, 2, 3, 4, 5, 6, 5, 0, 4, 0, 7, 8, 0],
    [5, 6, 8, 0, 0, 6, 9, 8, 10, 9, 3, 5, 9],
    [6, 9, 0, 11, 11, 0, 0, 5, 12, 8, 9, 12, 5],
    [2, 0, 11, 3, 2, 1, 2, 12, 13, 5, 7, 9, 0],
    [0, 11, 3, 2, 7, 10, 8, 7, 9, 12, 7, 5, 0],
    [7, 3, 9, 5, 10, 7, 7, 2, 3, 5, 9, 0, 0],
    [5, 0, 7, 10, 8, 7, 9, 14, 10, 12, 7, 2, 0],
    [3, 0, 9, 7, 7, 5, 6, 2, 0, 9, 5, 3, 10],
    [0, 7, 5, 7, 9, 12, 2, 0, 15, 0, 16, 9, 12],
    [10, 3, 2, 5, 0, 9, 15, 7, 9, 15, 10, 12, 9],
    [16, 9, 15, 15, 10, 0, 2, 3, 13, 9, 0, 17, 0],
    [9, 14, 5, 10, 12, 8, 0, 10, 13, 5, 8, 2, 12],
])

# Create a dictionary to store the correspondence between numbers and letters
correspondence_22027 = {7: 'T', 5: 'I', 3: 'R'}

puzzle_22026 = np.array([
    [1, 0, 1, 0, 2, 3, 4, 0, 2, 5, 4, 6, 3],
    [6, 2, 3, 7, 7, 1, 0, 8, 5, 0, 5, 9, 10],
    [3, 9, 0, 5, 0, 0, 6, 3, 4, 6, 3, 2, 1],
    [0, 7, 5, 11, 8, 10, 1, 4, 4, 9, 12, 5, 0],
    [7, 5, 11, 8, 2, 1, 4, 4, 5, 2, 1, 0, 8],
    [9, 11, 13, 2, 3, 6, 6, 3, 2, 1, 0, 1, 2],
    [0, 8, 2, 1, 4, 6, 3, 13, 9, 10, 9, 2, 1],
    [8, 2, 5, 4, 4, 9, 11, 9, 0, 10, 14, 0, 7],
    [15, 3, 14, 5, 9, 0, 1, 10, 11, 1, 6, 6, 9],
    [0, 2, 1, 0, 0, 1, 14, 1, 3, 0, 1, 5, 4],
    [6, 1, 0, 7, 3, 4, 6, 0, 2, 1, 4, 6, 9],
    [5, 0, 10, 1, 14, 6, 9, 7, 7, 15, 9, 1, 0],
])
correspondence_22026 = {6: 'T', 9: 'I', 2: 'R', 5: 'O'}


def display_puzzle(puzzle, correspondence):
    """
    Display the puzzle with the numbers and letters
    """
    flag = 0
    print()
    for row in puzzle:
        print("          ", end='')
        for cell in row:
            if cell in correspondence:
                print("{:>2}".format(correspondence[cell]), end=' ')
            else:
                if cell != 0:
                    print("{:>2}".format(cell), end=' ')
                    flag = 1
                else:
                    print("   ", end='')
        print("\n")
    if flag == 0:
        print("Completed!\n")


def add_correspondence(number, letter):
    """
    Add a new correspondence between a number and a letter
    """
    global correspondence
    correspondence[number] = letter
    print(f"{number} now corresponds to {letter}")


def remove_correspondence(letter):
    """
    Remove a correspondence between a number and a letter
    """
    global correspondence
    correspondence = {key:val for key, val in correspondence.items() if val != letter}
    print(f"{letter} no longer corresponds to any number")


# begin

puzzle = puzzle_22026
correspondence_start = correspondence_22026
correspondence = correspondence_start.copy()

display_puzzle(puzzle, correspondence)

# User interaction section
while True:
    command = input("Enter a command (or \"h\" for help): ")
    cchain = command.strip().split()
    if len(cchain) == 0:
        cchain.append('REFRESH')
    else:
        cchain[0] = cchain[0].upper()
    # screen refresh
    if cchain[0] == "REFRESH":
        display_puzzle(puzzle, correspondence)

    # add corresp
    elif cchain[0] == "A":
        try:
            for a in range(1, len(cchain), 2):
                if not cchain[a].isdigit():
                    print("{} is not an integer, skipping".format(cchain[a]))
                    continue
                else:
                    current_number = int(cchain[a])

                current_letter = cchain[a+1].upper()
                if len(current_letter) > 1:
                    print("{} is not a single letter, skipping".format(current_letter))
                    continue

                if current_number in correspondence:
                    print("{} already corresponds to {}, skipping".format(current_number, correspondence[current_number]))
                elif current_letter in correspondence.values():
                    print("{} already corresponds to {}, skipping".format(current_letter, list(correspondence.keys())[list(correspondence.values()).index(current_letter)]))
                elif (current_number < 1) or (current_number > 26):
                    print("Number must be between 1 and 26.")
                else:
                    add_correspondence(current_number, current_letter)
        except Exception: # PEP 8 E722
            traceback.print_exc()
        display_puzzle(puzzle, correspondence)

    elif cchain[0] == "R":
        try:
            for a in range(1, len(cchain)):
                current_letter = cchain[a].upper()
                if (not current_letter.isalpha() or (len(current_letter) > 1)):
                    print("{} is not a single letter, skipping".format(cchain[a]))
                elif current_letter not in correspondence.values():
                    print("{} has no correspondence, skipping".format(current_letter))
                else:
                    remove_correspondence(current_letter)
        except Exception:
            traceback.print_exc()
        display_puzzle(puzzle, correspondence)
    elif cchain[0] == "P":
        print()
        print(correspondence)
        print()
        for key in correspondence:
            print("{} {} ".format(key, correspondence[key]), end='')
        print("\n\n")
    elif cchain[0] == "X":
        correspondence = correspondence_start.copy()
        display_puzzle(puzzle, correspondence)
    elif cchain[0] == "Q":
        print("Bye!")
        sys.exit(0)
    elif cchain[0] == "H":
        print('\n'
              '\n'
              '                  A: add correspondence(s)\n'
              '                     A number letter [number letter] [...]\n'
              '                  R: remove correspondence(s)\n'
              '                     R letter [letter] [...]\n'
              '                  P: print current solution\n'
              '  REFRESH | <empty>: refresh display\n'
              '                  X: reset corresponcences\n'
              '                  H: this text\n'
              '\n')
    else:
        print("Invalid command")
