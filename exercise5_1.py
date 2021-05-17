"""
Python for Everybody: Exploring Data Using Python 3 by Charles R. Severance

Exercise 5.1: Write a program which repeatedly reads numbers until the user
enters "done". Once "done" is entered, print out the total, count, and average
of the numbers. If the user enters anything other than a number, detect their
mistake using try and except and print an error message and skip to the next
number.
Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.33333333333333

"""


def check_for_float(input1, exit = True):
    """
    Checks if the type of "input1" is a float and returns the value if so.
    Input:    input1 -- variable to check
    Output: val -- value of float
    """
    try:
        val = float(input1)                   # Only allows input floats
        return val
    except (ValueError, TypeError):
        print('Error, please enter numeric input')
        if exit:
            quit()
        return False


if __name__ == "__main__":
    count = 0                                 # Initializes values
    total = 0.0
    average = 0.0

    while True:                               # Stays in loop until break
        input_number = input('Enter a number: ')
        if input_number == 'done':
            break                             # Exits the while loop

        number = check_for_float(input_number, False)
        if not number:
            continue

        count += 1                            # Counter
        total = total + number                # Running total

    # Ensures count is not 0 which would cause division error
    if count:
        average = total / count               # Computes the average

    print(total, count, average)
