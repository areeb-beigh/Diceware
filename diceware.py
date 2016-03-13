#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import exit
from random import randint

# Error message for invalid input
invalidInput = " [-] Invalid input"

# The name of the diceware list file
dicewareFile = "diceware_list.txt"

def main():
	print " Extracting diceware list from {}\n".format(dicewareFile)
	extractor().extract()
	generate_dictionary()
	greet()

def greet():
	print "--------------------------------------------------------------------\n"
	print " Diceware password generator by Areeb Beigh - www.areebbeigh.tk"
	print " This is a simple application that will generate n number of diceware", \
		"passphrases for you, based on your input\n"

	print " Hit enter to continue..."
	raw_input()
	prompt()

# Print the code description and ask details about desired password
def prompt():
	print " How many passwords do you want to generate?"

	# Print invalidInput if the input is not an integer
	try:
		passwords = int(raw_input(' > '))
	except ValueError:
		print invalidInput
		prompt()
	except KeyboardInterrupt:
		print " Thank you for using Diceware Generator"
		exit(0)

	print " How many phrases do you want in your password(s)? (Recommended: 6)"

	try:
		phrases = int(raw_input(' > '))
	except ValueError:
		print invalidInput
		prompt()
	except KeyboardInterrupt:
		print " Thank you for using Diceware Generator"
		exit(0)

	# Phrases and passwords must be greater than 0
	if phrases > 0 and passwords > 0:
		print "--------------------------------------------------------------------"
		print " Your diceware passphrases: "
		for i in range(0, passwords):
			print "\n" + generate_password(phrases)
		print "--------------------------------------------------------------------"
	else:
		print invalidInput
		prompt()

	prompt()

# A minimal version of my word extractor - https://gist.github.com/areeb-beigh/7832e5e2a17727934bf5
class extractor(object):
	# Make a list of the extracted words
	def make_list(self):
		global finalList
		words = string.split()
		check = []
		finalList = []
		for word in words:
			if not(word in check):
				check.append(word)
				finalList.append(word)

	# Assemble the words and unwanted characters to different variables
	def assemble(self):
		global string
		string = ""
		for char in stuff:
			string = (str(string) + str(char))
		extractor().make_list()

	# Extract stuff from the diceware_list.txt file
	def extract(self):
		global stuff
		myFile = open(dicewareFile, 'r')
		stuff = myFile.read().replace('\n', ' ')
		myFile.close()
		extractor().assemble()

# Generate a python dictionary of the diceware list
def generate_dictionary():
	# The dicewareDict is needed by other methods
	global dicewareDict

	# Dictionary of keys and phrases will be added here
	dicewareDict = {}

	for i in range(0, len(finalList)):
		try:
			key = int(finalList[i])
			if len(str(key)) == 5:
				value = finalList[i + 1]
				pair = {key: value}
				dicewareDict.update(pair)
			else:
				pass
		except ValueError:
			pass

# Generate diceware passwords
def generate_password(phrases):
	# Diceware keys will be appended to this list
	diceResults = []

	# For iterations according to the number of phrases requested
	for i in range(0, phrases):
		# Digitally "roll a dice" five times and store the numbers
		rollDice1 = randint(1,6)
		rollDice2 = randint(1,6)
		rollDice3 = randint(1,6)
		rollDice4 = randint(1,6)
		rollDice5 = randint(1,6)

		# Make a diceware key with the dice roll results
		dicewareKey = str(rollDice1) + str(rollDice2) + str(rollDice3) + str(rollDice4) + str(rollDice5)

		# Append the key to the diceRestuls list
		diceResults.append(int(dicewareKey))

	# Phrases from the diceware dictionary will be concatinated here
	passphrase = ""

	# Iterate over the keys in diceResults and then take every
	# phrase associated with the respective key to for a passphrase
	for key in diceResults:
		phrase = dicewareDict[key]
		passphrase += ' ' + phrase
	
	return passphrase

if __name__ == '__main__':
	main()