
import random

def options():
    print("which one would u like to do?")
    print("1. make a circle")
    print("2. make a certain ammount of  lines")
    print("3. come up with a random design")
    print("4. end this app")
#my drawing of a circle
def circle_drawing():
    print("  ___  ")
    print(" /   \ ")
    print("|     |")
    print(" \___/ ")
#ask how many lines and chracters and how many times to repeat it
def line_maker():
    num_lines = int(input("How many lines to draw? "))
    characters = input("What character(s) to use? ")
    repeat = int(input("How many times to repeat the character? "))
    for _ in range(num_lines):
        print(characters * repeat)
#this ramdomizes which shape to make either a box or diamond or a zigzag
def random_design():
    choice = random.randint(1, 3)
    if choice == 1:
        design1()
    elif choice == 2:
        design2()
    else:
        design3()

def design1():
    print("Design 1: box")
    print("******")
    print("*    *")
    print("*    *")
    print("******")

def design2():
    print("Design 2: zigzag ")
    for i in range(5):
        print(" " * i + "*")

def design3():
    print("Design 3: diamond ")
    print("  *  ")
    print(" * * ")
    print("*   *")
    print(" * * ")
    print("  *  ")

def main():
    while True:
        options()
        choice = input("Enter your choice: ")
        if choice == '1':
            circle_drawing()
        elif choice == '2':
            line_maker()
        elif choice == '3':
            random_design()
        elif choice == '4':
            print("thank you for using this app")
            break
        else:
            print("Invalid choice, please try again.")


main()
