def checkCharacter(character):
    result = "None"
    if character == 'a' or character == 'A':
        result = "Vowel"
    elif character == 'e' or character == 'E':
        result = "Vowel"
    elif character == 'i' or character == 'I':
        result = "Vowel"
    elif character == 'o' or character == 'O':
        result = "Vowel"
    elif character == 'u' or character == 'U':
        result = "Vowel"
    else:
        result = "Consonant"

    return result

def main():
    character = str(input("Enter any character: "))
    character = character[0]
    if not character.isalpha() :
        print("Invalid Input")
    else:
        print("{}".format(checkCharacter(character)))

main()