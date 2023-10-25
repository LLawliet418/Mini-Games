from art import *
from prettytable import PrettyTable


class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def print_header():
    headline = text2art("Substitution Game", font="small")
    print(headline)


def create_letter_table(characters, columns_per_row):
    num_missing = columns_per_row - (len(characters) % columns_per_row)
    characters += [""] * num_missing
    positions = [str(i + 1) for i in range(len(characters))]
    table = PrettyTable()
    for i in range(columns_per_row):
        table.add_column("Letter", characters[i::columns_per_row])
        table.add_column("Position", positions[i::columns_per_row])
    return table


def print_game_info(alphabet, input_text):
    print("The goal of this game is to substitute letters in a given text to find the deciphered text.")
    print("___________________________________________________________________________________________", end="\n\n")
    print("The alphabet is:", alphabet)
    print("The input text is:", bcolors.HEADER + input_text + bcolors.ENDC)
    table = create_letter_table(list(input_text), columns_per_row=6)
    print(table)


def substitute_letters(text):
    # Type position of the letter to substitute
    user_input = int(
        input("Enter the position of the letter you want to substitute: ")) - 1
    user_input2 = input("Enter the letter you want to substitute with: ")

    # Convert the text into a list of characters
    text_characters = list(text)

    # Substitute the letter at the specified position
    if 0 <= user_input < len(text_characters):
        text_characters[user_input] = user_input2

        # If the substition letter is not in the alphabet, tell the user to try again
        if user_input2 not in alphabet:
            print(
                bcolors.FAIL + "The letter you entered is not in the alphabet. Try again." + bcolors.ENDC)
        else:
            print(bcolors.OKGREEN + "The letter has been substituted with " +
                  user_input2 + bcolors.ENDC)

    # Join the characters back into a string
    return ''.join(text_characters)


def play_substitution_game():
    input_text = "Ngx voss yqet dqfn rtytqzl of soyt, wxz ftctk stz ngxkltsy wt rtytqztr"
    deciphered_text = "You will face many defeats in life, but never let yourself be defeated"

    output_text = input_text

    print_header()
    print_game_info(alphabet, input_text)

    while True:
        # Print the table again
        output_text = substitute_letters(output_text)
        print("______________________________________________________________", end="\n\n")
        print("The alphabet is:", alphabet)
        print("The output text is:", bcolors.HEADER + output_text + bcolors.ENDC)
        table = create_letter_table(list(output_text), columns_per_row=6)
        print(table)

        if output_text == deciphered_text:
            print(bcolors.OKGREEN +
                  "You have deciphered the text! Congratulations!" + bcolors.ENDC)
            break


play_substitution_game()
