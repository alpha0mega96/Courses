import json
from difflib import get_close_matches

data = json.load(open("data.json","r"))

def translate(word):
    str = ""
    if word in data:		#the word is entered correctly, hence matches right away
	for translation in data[word]:
	    str += translation +"\n"
	return str
    elif word.title() in data:
	return translate(word.title())	#correct the word and retry
    elif word.upper() in data:
	return translate(word.upper())	#a recursion technique (1 depth only)
    elif len( get_close_matches(word, data.keys(), cutoff=0.8) ) >= 1:
	matched = get_close_matches(word, data.keys(), cutoff=0.8)
	hunch = input("Did you mean %s? Press Y for yes or N for no: " % matched[0])
	if hunch.upper() == "Y":
	    return translate(matched[0])
	elif hunch.upper() == "N":
	    return "Please try again."
	else:
	    return "Sorry, we didn't understand your entry."
    else:
	return "This word doesn't exist in our Dictionary. Please check the entered word."


query = input("Enter word: ")

print(translate(query))


