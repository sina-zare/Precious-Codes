import math

input = input()
word_list_without_punctuation_1 = input.split("!")
word_list_without_punctuation_2 = "".join(word_list_without_punctuation_1).split("?")
word_list_without_punctuation_3 = "".join(word_list_without_punctuation_2).split(".")
word_list_without_punctuation_4 = "".join(word_list_without_punctuation_3).split(",")
word_list_without_punctuation_5 = "".join(word_list_without_punctuation_4).split(":")
word_list_without_punctuation_6 = "".join(word_list_without_punctuation_5).split(";")
word_list_without_punctuation_7 = "".join(word_list_without_punctuation_6).split(" ")

amount = len(word_list_without_punctuation_7)

strings = "".join(word_list_without_punctuation_7)

average = len(strings) / amount

print(math.ceil(average))


