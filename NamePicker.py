from random import randrange
import string

def pickNames(vowels, consonants, nameLen, count):
	vowelNum = 1 if nameLen == 5 else 2	
	names = []
	for _ in xrange(count):
		name = ""
		for _ in xrange(nameLen):
			letter = getConsonant(consonants)
			name += letter
		if nameLen == 5:
			name = name[:2] + getVowel(vowels) + name[3:]
		names.append(name)
	return names

def getVowel(vowels):
	return vowels[randrange(len(vowels))]

def getConsonant(consonants):
	return consonants[randrange(len(consonants))]

if __name__ == "__main__":
	vowels = set(["a", "e", "i", "o", "u"])
	consonants = set(string.lowercase) - vowels
	names = pickNames(list(vowels), list(consonants), 5, 100)
	print names