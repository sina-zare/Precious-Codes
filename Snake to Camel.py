def snake_to_camel(word):
    #snake_case to CamelCase
    lst_prm = word.split("_")
    lst_fnl = []
    for i in lst_prm:
        lst_fnl.append(i.capitalize())
    return "".join(lst_fnl)


