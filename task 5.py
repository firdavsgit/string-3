string = ("anime",
"meme",
"vines",
"roasts",
"Danny DeVito")
words = input("Enter the name:")

def prevent_distractions(string, words):
    for item in string:
        if item in words:
            return "NO!"

    return "Safe Watching!"


print(prevent_distractions(string, words))

