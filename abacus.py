import os

os.system('cls')
print("Running Abacus...")


def abacus():
    numbers = input("\nEnter a number between 1 and 9999: ")

    if len(numbers) > 4:
        os.system('cls')
        print("I will only accept 4 digit numbers.\n")
        input("Press ENTER to continue...")
        abacus()
    else:
        for number in numbers[::-1]:
            right = ("x"*int(number))
            left = ( "x"*(10-int(number)))
            print("|" + left + "-"*6 + right + "|")

abacus()

