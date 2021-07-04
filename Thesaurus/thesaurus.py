import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		match0 = get_close_matches(word, data.keys())[0]
		yn = input(f"Did you mean {match0} instead? Enter Y if yes, or N if no: ").lower()
		if yn == "y":
			return data[match0]
		elif yn == "n":
			return "The word doesn't exist. Please double check it."
		else:
			return "We didn't understand your entry." 	
	else:
		return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
	for item in output:
		print(output)
else:
	print(output)