import json
import difflib
from difflib import get_close_matches
data = json.load(open("./dictionary/data.json"))
def translate(word):
    word = word.lower()
    if word  in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean {}".format(get_close_matches(word, data.keys())[0]))
        re_input = input("Type Yes or No : ")
        re_input = re_input.lower()
        if re_input == "yes":
            word = get_close_matches(word, data.keys())[0]
            return data[word]
        elif re_input == "no":
            return "Please Check your Spelling"
        else:
            return "Not Found!!!!!"

    else:
        return "Not Found"

user_input = input("Please enter the word: ")

output = translate(user_input)

if len(output) > 1 and type(output) == list:
    [print(i) for i in output]
else:
    print(output[0])

