string = input("Enter the word:")
vowels = "aeuio"

def is_vowel_sandwich(string, vowels):
    if len(string) != 3:
        return False

    if string[0] not in vowels and string[2] not in vowels:
        if string[1] in vowels:
            return True

    return False

print(is_vowel_sandwich(string, vowels))