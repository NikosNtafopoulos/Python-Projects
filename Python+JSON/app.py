import json


data = json.load(open("data.json"))


def wordCheck(passedword):
    passedword = passedword.lower()

    if passedword in data:
        return data[passedword]
    else:
        return "{} does not exist".format(passedword)


word = input('Enter a word you want to check: ')


print (wordCheck(word))
