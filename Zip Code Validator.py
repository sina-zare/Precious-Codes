def ZipCodeValidator(zipcode):
    if zipcode.isnumeric() and (len(zipcode) == 5) and (" " not in zipcode):
        print("true")
    else:
        print("false")

while True:
    ZipCodeValidator(input("Postal Code: "))



