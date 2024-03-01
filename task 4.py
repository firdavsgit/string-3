string1 = "R!=:~0o0./c&}9k`60=y"

def letters_only(string1):
    lst = []
    for item in string1:
        if item.isalpha():
            lst.append(item)


    print("".join(lst))


letters_only(string1)
