
def count(word, letter):
    counter = 0

    for character in word:
        if character == letter:
            counter = counter + 1
    print(counter)


input_word = input('Enter the word: ')
input_letter = input('Enter the letter: ')
count(input_word, input_letter)
