letters = "hApPy"

def cap_to_front(letters):
    string1 = []
    string2 = []
    for x in letters:
        if x.isupper():
            string1.append(x)
        else:
            string2.append(x)

    print("".join(string1 + string2))

cap_to_front(letters)

