input1 = input('Enter a number: ')
if input1 == 'done':
    quit()                                # Exits if no input

number = check_for_float(input1)          # Ensure input is a float

smallest = number
largest = number

while True:                               # Stays in loop until break
    input1 = input('Enter a number: ')
    if input1 == 'done':
        break                             # Exits loop

    number = check_for_float(input1)      # Ensure input is a float

    if number > largest:                  # Condition for maximum
        largest = number
    if number < smallest:                 # Condition for minimum
        smallest = number

print(largest, smallest)
