def isogram(word):
    StandardWord = word.lower()
    indicator = 0
    letters = []
    letters.extend(StandardWord)

    for i in letters:
        if StandardWord.count(i) <= 1:
            indicator += 1
            if indicator == len(StandardWord):
                print("true")
        else:
            print("false")
            break

isogram(input())