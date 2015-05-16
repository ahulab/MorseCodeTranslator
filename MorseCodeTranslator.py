# defining lists
morse_alphabet = [
                 (1, 3), (3, 1, 1, 1), (3, 1, 3, 1), (3, 1, 1), 1, (1, 1, 3, 1), (3, 3, 1), (1, 1, 1, 1), (1, 1),
                 (1, 3, 3, 3), (3, 1, 3), (1, 3, 1, 1), (3, 3), (3, 1), (3, 3, 3), (1, 3, 3, 1), (3, 3, 1, 3),
                 (1, 3, 1), (1, 1, 1), 3, (1, 1, 3), (1, 1, 1, 3), (1, 3, 3), (3, 1, 1, 3), (3, 1, 3, 3,), (3, 3, 1, 1),
                 0, (3, 3, 3, 3, 3), (1, 3, 3, 3, 3), (1, 1, 3, 3, 3,), (1, 1, 1, 3, 3), (1, 1, 1, 1, 3),
                 (1, 1, 1, 1, 1), (3, 1, 1, 1, 1), (3, 3, 1, 1, 1), (3, 3, 3, 1, 1), (3, 3, 3, 3, 1), (1, 3, 1, 3, 1, 3)
                 , (3, 3, 1, 1, 3, 3,), (1, 1, 3, 3, 1, 1,), (1, 3, 3, 3, 3, 1), (3, 1, 3, 1, 3, 3), (3, 1, 1, 3, 1),
                 (3, 1, 3, 3, 1), (3, 1, 3, 3, 1, 3), (1, 3, 1, 1, 1), (3, 3, 3, 1, 1, 1), (3, 1, 3, 1, 3, 1),
                 (3, 1, 1, 1, 3), (1, 3, 1, 3, 1), (3, 1, 1, 1, 1, 3), (1, 1, 3, 3, 1, 3), (1, 3, 1, 1, 3, 1),
                 (1, 1, 1, 3, 1, 1, 3), (1, 3, 3, 1, 3, 1)
                 ]

english_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                    ".", ",", "?", "'", "!", "/", "(", ")", "&", ":", ";", "=", "+", "-", "_", '"', "$", "@"]

morse_sound = []
output_list = []
# captures text to translate to morse as a string


def text_to_morse(input_list):
    del output_list[:]  # deletes the content of the list in case the user has already translated once
    for char in input_list:
        # morse_char is equal to the tuple corresponding to the english letter. so if char == "p" then morse_char
        # should equal .__.
        morse_char = morse_alphabet[english_alphabet.index(char)]
        # append tuple to end of output list. the for loop below then goes thru it and translates dits and dahs to
        # .s and _s
        output_list.append(morse_char)
        # append a space at the end of the for loop so that when we print the output we have spaces between each char
        # so "hi" would now look like output_list = [(1,1,1,1), 1, " ", (3, 3, 3), (3, 3), (3, 3, 3)]
        output_list.append(" ")

    output_text = []                # create blank list for output
    for i in output_list:
        # if i is either 1 or 3, meaning it is not a tuple, then it is translated to . or _ respectively
        # see above where "hi" is translated to (1,1,1,1), 1. Python cannot iterate thru the 1 so it errors out without
        # the first two parts of the if statement below if it comes across a 1 or 3.
        if i == 1:
            output_text.append(".")
        elif i == 3:
            output_text.append("_")
        elif i == 0:
            output_text.append(" / ")
        elif i == " ":
            output_text.append(i)
        # if i is a tuple then
        else:
            # if i is not an integer then it is a tuple and can be iterated over. we go thru the tuple and append .s and
            # _s to the list as necessary. uncomment out the print statement below to see
            for item in i:
                if item == 1:
                    output_text.append(".")
                elif item == 3:
                    output_text.append("_")
                # print output_text

    output_text = ''.join(output_text)
    print(output_text)


def morse_to_text(input_list):
    del output_list[:]
    if len(input_list) == 1:
        if input_list[0] == ".":
            index_number = 1
        elif input_list[0] == "_":
            index_number = 3
        print(english_alphabet[morse_alphabet.index(index_number)])
    else:
        morse_to_text_second_half(input_list)
        # i split this function up because it was becoming to complicated to do all within one
        # the if statement above fixes an error that was generated when input_list was of length 1


def morse_to_text_second_half(input_list):
    word_holder_list = []
    x = 0
    for i in input_list:
        x += 1
        if i == " " or x == len(input_list):
            # if there is a space or we're at the end of the input then......
            # this means there is a space and we should move onto the next letter
            # here we should find the current letter and add it to a list, then empty the temp list and move on
            # to the next letter. tuple(list) turns list into tuple
            if i == ".":
                word_holder_list.append(1)
                output_list.append(english_alphabet[morse_alphabet.index(tuple(word_holder_list))])
                # print word_holder_list
            elif i == "_":
                word_holder_list.append(3)
                output_list.append(english_alphabet[morse_alphabet.index(tuple(word_holder_list))])
            elif i == " ":
                if len(word_holder_list) > 1:
                    output_list.append(english_alphabet[morse_alphabet.index(tuple(word_holder_list))])
                    del word_holder_list[:]
                elif len(word_holder_list) == 1:
                    output_list.append(english_alphabet[morse_alphabet.index(word_holder_list[0])])
                    del word_holder_list[:]

        elif i == ".":
            word_holder_list.append(1)
        elif i == "_":
            word_holder_list.append(3)
        elif i == "/":
            output_list.append(" ")
            del word_holder_list[:]

    output_list_string = ''.join(output_list)
    print(output_list_string)


def begin():

    print("This program translates text to morse-code and vice versa. \nIf you would like turn text into morse then "
          "type 'text' without quotes. \nOtherwise type 'morse' to turn morse into text.")

    valid_input = True
    while valid_input:
        encode_or_decode = input("Type \"text\" or \"morse\": ")
        if encode_or_decode.lower() == "text" or encode_or_decode == "morse":
            valid_input = False
        else:
            print("Your input is not valid. Please try again by entering either \"text\" or \"morse\"")

    input_text = input("Enter what you would like to be translated: \n>").lower()
    input_chars = list(input_text)  #
    # i think this is actually redundant... iterating thru a string would work the same way

    if encode_or_decode == "text":
        text_to_morse(input_chars)

    elif encode_or_decode == "morse":
        morse_to_text(input_chars)


done = False

while not done:
    begin()
    again = input("Would you like to translate something else? \nY or N")
    if again.lower() == "y":
        continue
    else:
        done = True

exit()
