names = ["John", "Oscar", "Jacob"]
x = open(r"C:\Users\Sina\Desktop\test4.txt", "a")

str = ""
for i in names:
    str += (i + "\n")
x.write(str)

x.close()

x = open(r"C:\Users\Sina\Desktop\test4.txt", "r")
x.read()
x.close()