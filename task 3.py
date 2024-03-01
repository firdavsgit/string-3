
string = "TrAdE2W1n95!"

def left_digit(string):
    lst = []
    for item in string:
        if item.isdigit():
            lst.append(item)

    print(lst[0])


left_digit(string)
