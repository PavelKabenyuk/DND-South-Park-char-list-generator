from scripts import parsing


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
                    with open(ascii_path) as ascii_txt:
                        ascii = ascii_txt.read()
                        print(ascii + "\n")

                print("\n")

                for title, value in specs.items():
                    print(title + ": " + value)

                print("\nTry another one:")


if __name__ == '__main__':
    main()
