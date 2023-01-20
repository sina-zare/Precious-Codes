sentence = input()
list = sentence.split(" ")
pig_list = []

for i in list:
    x = i[1:] + i[0] + "ay"
    pig_list.append(x)

print( " ".join(pig_list) )
