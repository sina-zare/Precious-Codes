alphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabet_rev = [" ", "z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j" ,"i", "h", "g", "f", "e", "d", "c", "b", "a"]

rev_alpha_dic = dict(zip(alphabet, alphabet_rev))

clear_text = input().lower()
cipher_list = []

for i in clear_text[0:]:
    cipher_list.append(rev_alpha_dic[i])

cipher_text = "".join(cipher_list)

print(cipher_text)