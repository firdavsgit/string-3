input  = input("Enter the letter:")
s = "cheese casserole"

def vow_replace(input,  s):
    vowels = "aoiue"
    for x in vowels:
        if x in s:
            s = s.replace(x , input)
    return s


print(vow_replace(input,s))

