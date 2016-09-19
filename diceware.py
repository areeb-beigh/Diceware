# Author: Areeb Beigh
# Created: 11th June 2016

# github.com/areebbeigh

"""
This application generate 'n' number of diceware passwords each with
'm' number of phrases, whole number value both 'n' and 'm' depend upon the user
"""

from random import randint


# Error message for invalid input
invalid_input = " [-] Invalid input"

# The name of the diceware list file
diceware_file = "diceware_list.txt"


def generate_diceware_dict():
    """
    Generates and returns key - value pairs of diceware keys and phrases
    in the form of a dictionary
    """

    dictionary = {}

    with open(diceware_file, 'r') as f:
        lines = f.readlines()

        for line in lines:
            line = line.split()
            dictionary[int(line[0])] = line[1]

    return dictionary


def generate_password(phrases, diceware_dict):
    """
    Returns a diceware pass_phrase string with 'n' number of phrases.

    Parameters:
        phrases:
            Number of phrases in each pass phrase

        diceware_dict:
            The diceware dictionary
    """

    # Diceware keys will be appended to this list
    dice_keys = []
    # Phrases from the diceware dictionary will be concatinated here
    pass_phrase = ""

    for i in range(phrases):
        # Virtually roll a dice five times and store the numbers
        roll_dice1 = randint(1,6)
        roll_dice2 = randint(1,6)
        roll_dice3 = randint(1,6)
        roll_dice4 = randint(1,6)
        roll_dice5 = randint(1,6)

        # Makes a diceware key with the dice roll results
        diceware_key = \
            str(roll_dice1) + \
            str(roll_dice2) + \
            str(roll_dice3) + \
            str(roll_dice4) + \
            str(roll_dice5)

        # Appends the key to the dice_keys list
        dice_keys.append(int(diceware_key))

    # Generates a pass_phrase using the keys in the dice_keys list
    for key in dice_keys:
        value = diceware_dict[key]
        pass_phrase += ' ' + value

    return pass_phrase


def prompt(dictionary):
    """ Asks details about the desired password """

    print(" How many password(s) do you want to generate?")

    # Prints invalid input message if the input is not an integer
    try:
        passwords = int(input(' > '))
    except ValueError:
        print(invalid_input)
        prompt(dictionary)

    print(" How many phrases do you want in your password(s)? (Recommended: 6)")

    try:
        phrases = int(input(' > '))
    except ValueError:
        print(invalid_input)
        prompt(dictionary)

    # Phrases and passwords must be greater than 0 (duh?)
    if phrases > 0 and passwords > 0:
        print("--------------------------------------------------------------------")
        print(" Your diceware passphrases: ")

        for i in range(passwords):
            print("\n" + generate_password(phrases, dictionary))

        print("--------------------------------------------------------------------")
    else:
        print(invalid_input)

    prompt(dictionary)

if __name__ == '__main__':

    print(" Extracting diceware list from {}\n".format(diceware_file))

    diceware_dict = generate_diceware_dict()

    print("--------------------------------------------------------------------\n")
    print(" Diceware password generator by Areeb Beigh - github.com/areebbeigh")
    print(" This is a simple application that will generate n number of diceware"),
    print(" pass-phrases, based on your input\n")

    print(" Hit enter to continue...")
    input()
    prompt(diceware_dict)