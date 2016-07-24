# Python Diceware Generate by Areeb 
# Created: 11th June 2016

# github.com/areeb-beigh

"""
This application generate 'n' number of diceware passwords each with
'm' number of phrases, whole number value both 'n' and 'm' depend upon the user
"""

from sys import exit
from random import randint

# Error message for invalid input
invalidInput = " [-] Invalid input"

# The name of the diceware list file
dicewareFile = "diceware_list.txt"

def generateDicewareDict():
	# Generates and returns key - value pairs of diceware keys and phrases
	# in the form of a dictionary

	dictionary = {}

	with open('diceware_list.txt', 'r') as f:
		lines = f.readlines()

		for line in lines:
			line = line.split()
			dictionary[int(line[0])] = line[1]

	return dictionary

def generatePassword(phrases, dicewareDict):
	# Returns a diceware passphrase string with 'n' number of phrases
	# Arguement phrases is a whole number

	# Diceware keys will be appended to this list
	diceKeys = []
	# Phrases from the diceware dictionary will be concatinated here
	passphrase = ""

	for i in range(phrases):
		# Virtually roll a dice five times and store the numbers
		rollDice1 = randint(1,6)
		rollDice2 = randint(1,6)
		rollDice3 = randint(1,6)
		rollDice4 = randint(1,6)
		rollDice5 = randint(1,6)

		# Makes a diceware key with the dice roll results
		dicewareKey = str(rollDice1) + str(rollDice2) + str(rollDice3) + str(rollDice4) + str(rollDice5)

		# Appends the key to the diceKeys list
		diceKeys.append(int(dicewareKey))

	# Generates a passphrase using the keys in the diceKeys list
	for key in diceKeys:
		value = dicewareDict[key]
		passphrase += ' ' + value
	
	return passphrase

def prompt(dictionary):
	# Asks details about desired password

	print(" How many password(s) do you want to generate?")

	# Prints invalid input message if the input is not an integer
	try:
		passwords = int(input(' > '))
	except(ValueError):
		print(invalidInput)
		prompt(dictionary)

	print(" How many phrases do you want in your password(s)? (Recommended: 6)")

	try:
		phrases = int(input(' > '))
	except(ValueError):
		print(invalidInput)
		prompt(dictionary)

	# Phrases and passwords must be greater than 0 (duh?)
	if (phrases > 0 and passwords > 0):
		print("--------------------------------------------------------------------")
		print(" Your diceware passphrases: ")

		for i in range(passwords):
			print("\n" + generatePassword(phrases, dictionary))

		print("--------------------------------------------------------------------")
	else:
		print(invalidInput)

	prompt(dictionary)

if __name__ == '__main__':
	
	print(" Extracting diceware list from {}\n".format(dicewareFile))
	
	dicewareDict = generateDicewareDict()

	print("--------------------------------------------------------------------\n")
	print(" Diceware password generator by Areeb Beigh - github.com/areeb-beigh")
	print(" This is a simple application that will generate n number of diceware"),
	print(" passphrases for you, based on your input\n")

	print(" Hit enter to continue...")
	input()
	prompt(dicewareDict)