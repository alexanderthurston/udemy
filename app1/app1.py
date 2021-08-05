import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def main():
    word = input("Enter word: ")
    output = define(word)

    to_string(output)


def define(word):

    word = word.lower()
    close_matches = get_close_matches(word, data.keys(), cutoff=0.8)

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(close_matches) > 0:
        response = input("Did you mean %s instead? Y or N :" % close_matches[0])

        if response.lower() == "y":
            return data[close_matches[0]]
        elif response.lower() == "n":
            return "That word doesn't exist in our database. Please double check it"
        else:
            return "Sorry, we couldn't find the word you were looking for. Please try a different word"

    else:
        return "That word is not in our library. Please try a different spelling or a different word."

def to_string(output):
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
while True:
    main()
