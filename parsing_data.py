import requests
import os
import urllib
from bs4 import BeautifulSoup as BS
import PIL
# Import scripts
import creating_acsii

request_titles = requests.get("https://southpark.fandom.com/wiki/Portal:Characters")
html_titles = BS(request_titles.content, "html.parser")
# todo: Make some refactoring about vars and imports, diverse program with files (make main.py)

letters = {'main_characters': 0,
           'a': 1, 'b': 2, 'c': 3, 'd': 4,
           'e': 5, 'f': 6, 'g': 7, 'h': 8,
           'i': 9, 'j': 10, 'k': 11, 'l': 12,
           'm': 13, 'n': 14, 'o': 15, 'p': 16,
           'q': 17, 'r': 18, 's': 19, 't': 20,
           'u': 21, 'v': 22, 'w': 23, 'x': 24,
           'y': 25, 'z': 26, "#": 27}


# Cropping image for suitable size
def cropping_image(path):
    # todo Need to check size of non-cropped element and then crop it with estimating it (bad example: 6th Graders
    #  Bruisers, Beth (Dawg's Bitch)
    image = PIL.Image.open(path)
    width, height = image.size

    koef = width/height

    if koef < 1:
        print(1)
        image_cropped = image.resize((100, 100))
    else:
        image_cropped = image.resize((100, 100))

    image_cropped.save(path)


# Parsing certain group
def parsing_group(symbol):
    for galary in html_titles.select('#mw-content-text'):
        for title in galary.select("#gallery-" + str(symbol) + " .wikia-gallery-item"):

            if title.find("i"):
                character = title.select('.lightbox-caption > i > a')
            else:
                character = title.select('.lightbox-caption > a')

            if name == character[0].text:
                return searching_specs(name)

    return False


# Parsing names of all characters
def all_names(name):

    if not str(name[0]).isnumeric():
        letter = letters[name[0].lower()]
        if parsing_group(letter) == False:
            print("Character doesn't exist, try again!")
    else:
        if parsing_group(letters['#']) == False:
            print("Character doesn't exist, try again!")


# Parsing specs
def searching_specs(character):
    title = character.replace(" ", "_")

    request = requests.get("https://southpark.fandom.com/wiki/" + title)
    html = BS(request.content, "html.parser")

    print(character + "\n")

    for img_html in html.select("figure.pi-image > a > img"):
        current_directory = os.getcwd()
        directory = os.path.join(current_directory, "images", "characters", title)

        if not os.path.exists(directory):
            os.mkdir(directory)

        image = img_html['src']
        image_name = img_html['data-image-name']
        image_path = directory + "/" + image_name

        if not os.path.exists(image_path):
            urllib.request.urlretrieve(image, image_path)
            cropping_image(image_path)

        ascii_path = creating_acsii.main(title, image_path, image_name)

        with open(ascii_path) as ascii_txt:
            ascii = ascii_txt.read()
            print(ascii + "\n")

    for el in html.select("section.pi-item > div.pi-item"):
        title_specs = el.select('h3')
        value_specs = el.select('div.pi-font')

        print(title_specs[0].text + ": " + value_specs[0].text)

    print("\n")


while True:
    name = input("> ")
    all_names(name)
