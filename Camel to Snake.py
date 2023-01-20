camel_case = input()

def camel_to_snake(word):
    #CamelCase to snake_case
    snakecase = ""
    for i in word:
        if i.isupper():
            snakecase += "_"+i.lower()
        else:
            snakecase += i
    return snakecase[1:]


print(camel_to_snake(camel_case))

#or
"""
# Python3 program to convert string
# from camel case to snake case

def change_case(str):
	res = [str[0].lower()]
	for c in str[1:]:
		if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
			res.append('_')
			res.append(c.lower())
		else:
			res.append(c)
	
	return ''.join(res)
	
# Driver code
str = "GeeksForGeeks"
print(change_case(str))

"""