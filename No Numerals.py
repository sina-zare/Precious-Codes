phrase = input()

dict = {
        "0": "zero", "1": "one", "2": "two",
        "3": "three", "4": "four", "5": "five",
        "6": "six", "7": "seven", "8": "eight",
        "9": "nine", "10": "ten"
}


phrase_list = phrase.split(" ")

for i in phrase_list:
        if i in dict:
                index = phrase_list.index(i)
                phrase_list.insert(index, dict[i])
                phrase_list.remove(i)

prc_phrase = " ".join(phrase_list)
print(prc_phrase)



