from scripts import parsing
import os


def main():

    print("DND South Park char list generator. Please, enter the name of a character.")

    while True:
        name = input("> ")

        if name == "":
            print("Character doesn't exist, try again!")
        else:
            package = parsing.main(name)

            if not package:
                print("Character doesn't exist, try again!")
            else:
                character, specs, ascii_array = package

                print(character + "\n")

                for ascii_path in ascii_array:
                    if os.path.exists(ascii_path):
                        with open(ascii_path) as ascii_txt:
                            ascii = ascii_txt.read()
                            print(ascii + "\n")
                    else:
                        print("Sorry, but ASCII version of this character doesn't exist."
                              " You can see default picture here: " + ascii_path + "\n")

                for title, value in specs.items():
                    print(title + ": " + value)

                print("\nTry another one:")


if __name__ == '__main__':
    main()
