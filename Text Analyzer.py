def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

try:
    path = input("Enter Path to the file: ")
    with open(r"{0}".format(path), "r") as f:
        read_file = f.read()
        read_file_to_lowercase = read_file.lower()

        for i in "abcdefghijklmnopqrstuvwxyz":
            percentage =( ( 100 * count_char(read_file_to_lowercase, i)) / len(read_file_to_lowercase) )
            print("{0} takes {1}% of the whole text.".format(i, round(percentage, 2)))

except:
    print("File Does Not Exist.")


