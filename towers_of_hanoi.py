# This program simulates the Towers of Hanoi game.

# A global variable `count` is declared to track
# the total number of  iterations of the game.
count = 0


def main():
    # Set up some initial values.
    from_peg = 1
    to_peg = 3
    temp_peg = 2
    while True:
        try:
            num_discs = int(input("Number of rings to move: "))
            if num_discs < 1 or num_discs > 20:
                # Program will reject large numbers to prevent excessive computation
                raise ValueError("Please enter a positive integer > 20 \n"
                                 "Large numbers requre significant computation")
            # Break if not an unacceptable number
            else:
                break

        except ValueError as e:
            # Print our error
            print(e)

    # Play the game.
    move_discs(num_discs, from_peg, to_peg, temp_peg)
    print('All the pegs are moved!')
    # Print the number of moves required to complete the game
    print(f"The game was solved in {count} moves.")


# The moveDiscs function displays a disc move in
# the Towers of Hanoi game.
# The parameters are:
#   num:        The number of discs to move.
#   from_peg:   The peg to move from.
#   to_peg:     The peg to move to.
#   temp_peg:   The temporary peg.
def move_discs(num, from_peg, to_peg, temp_peg):
    # Call our global count variable
    global count
    if num > 0:
        move_discs(num - 1, from_peg, temp_peg, to_peg)
        print(f'Move a disc from peg {from_peg} to peg {to_peg}.')
        move_discs(num - 1, temp_peg, to_peg, from_peg)
        # Iterates the counter tracking the total
        # number of recursive operations.
        count += 1


# Call the main function.
if __name__ == '__main__':
    main()
