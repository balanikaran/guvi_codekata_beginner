def checkCharacter(character):
    if character.isalpha():
        return "Alphabet"
    else:
        return "Not Alphabet"

def main():
    character = str(input("Enter any character: "))
    character = character[0]
    result = checkCharacter(character)
    print("{}".format(result))

main()