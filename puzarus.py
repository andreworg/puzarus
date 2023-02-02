import traceback
import sys
import db_puz

def display_puzzle(puzzle):
    """
    Display the puzzle with the numbers and letters
    """
    flag = 0
    print()
    for row in puzzle:
        print("          ", end='')
        for cell in row:
            if cell in matches:
                print("{:>2}".format(matches[cell]), end=' ')
            else:
                if cell != 0:
                    print("{:>2}".format(cell), end=' ')
                    flag = 1
                else:
                    print("   ", end='')
        print("\n")
    if flag == 0:
        print("Completed!\n")


def add_matches(number, letter):
    """
    Add a new match between a number and a letter
    """
    global matches
    matches[number] = letter
    print(f"{number} now matches {letter}")


def remove_matches(letter):
    """
    Remove a match between a number and a letter
    """
    global matches
    matches = {key:val for key, val in matches.items() if val != letter}
    print(f"{letter} no longer corresponds to any number")


# begin

# init puzzle data
puzzle = db_puz.puzzle_22026
matches_start = db_puz.matches_22026
matches = matches_start.copy()

display_puzzle(puzzle)

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
        display_puzzle(puzzle)

    # add new match(es)
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

                if current_number in matches:
                    print("{} already corresponds to {}, skipping".format(current_number, matches[current_number]))
                elif current_letter in matches.values():
                    print("{} already corresponds to {}, skipping".format(current_letter, list(matches.keys())[list(matches.values()).index(current_letter)]))
                elif (current_number < 1) or (current_number > 26):
                    print("Number must be between 1 and 26.")
                else:
                    add_matches(current_number, current_letter)
        except Exception: # PEP 8 E722
            traceback.print_exc()
        display_puzzle(puzzle)

    # remove match(es)
    elif cchain[0] == "R":
        try:
            for a in range(1, len(cchain)):
                current_letter = cchain[a].upper()
                if (not current_letter.isalpha() or (len(current_letter) > 1)):
                    print("{} is not a single letter, skipping".format(cchain[a]))
                elif current_letter not in matches.values():
                    print("{} has no correspondence, skipping".format(current_letter))
                else:
                    remove_matches(current_letter)
        except Exception:
            traceback.print_exc()
        display_puzzle(puzzle)

    # print current matches
    elif cchain[0] == "P":
        print()
        print(matches)
        print()
        for key in matches:
            print("{} {} ".format(key, matches[key]), end='')
        print("\n\n")

    # revert to initial matches (start over)
    elif cchain[0] == "X":
        matches = matches_start.copy()
        display_puzzle(puzzle)

    # quit
    elif cchain[0] == "Q":
        print("Bye!")
        sys.exit(0)

    # help
    elif cchain[0] == "H":
        print('\n'
              '\n'
              '                  A: add matches\n'
              '                     usage: A number letter [number letter] [...]\n'
              '                  R: remove matches\n'
              '                     usage: R letter [letter] [...]\n'
              '                  P: print current solution (matches)\n'
              '  REFRESH | <empty>: refresh display\n'
              '                  X: reset all matches (revert to start)\n'
              '                  H: this text\n'
              '\n')

    # what?
    else:
        print("Invalid command")
