import requests
import os
import urllib
from bs4 import BeautifulSoup as BS
# import other scripts
from scripts import images_cropping
from scripts import generating_ascii

request_titles = requests.get("https://southpark.fandom.com/wiki/Portal:Characters")
html_titles = BS(request_titles.content, "html.parser")

letters = {'main_characters': 0,
           'a': 1, 'b': 2, 'c': 3, 'd': 4,
           'e': 5, 'f': 6, 'g': 7, 'h': 8,
           'i': 9, 'j': 10, 'k': 11, 'l': 12,
           'm': 13, 'n': 14, 'o': 15, 'p': 16,
           'q': 17, 'r': 18, 's': 19, 't': 20,
           'u': 21, 'v': 22, 'w': 23, 'x': 24,
           'y': 25, 'z': 26, "#": 27}


def main(title="title"):

    specs_array = {}
    ascii_array = []

    # Parsing certain group
    def parsing_group(symbol="letter", target_title="title"):
        for galary in html_titles.select('#mw-content-text'):
            for source_title in galary.select("#gallery-" + str(symbol) + " .wikia-gallery-item"):

                if source_title.find("i"):
                    character = source_title.select('.lightbox-caption > i > a')
                else:
                    character = source_title.select('.lightbox-caption > a')

                if target_title == character[0].text:
                    return searching_specs(target_title)

        return False

    # Parsing specs
    def searching_specs(character):
        title = character.replace(" ", "_")
        title = title.replace("'", "%27")

        request = requests.get("https://southpark.fandom.com/wiki/" + title)
        html = BS(request.content, "html.parser")

        # Parsing images
        for img_html in html.select("figure.pi-image > a > img"):
            current_directory = os.getcwd()
            directory = os.path.join(current_directory, "data/images", "characters", title)

            if not os.path.exists(directory):
                os.mkdir(directory)

            image = img_html['src']
            image_name = img_html['data-image-name']
            image_path = directory + "/" + image_name

            if not os.path.exists(image_path):
                urllib.request.urlretrieve(image, image_path)
                images_cropping.main(path=image_path)

            ascii_path = generating_ascii.main(title=title, image_title=image_name, source_path=image_path)

            if ascii_path not in ascii_array:
                ascii_array.append(ascii_path)

        # Parsing specs
        for el in html.select("section.pi-item > div.pi-item"):
            title_specs = el.select('h3')
            value_specs = el.select('div.pi-font')

            specs_array[title_specs[0].text] = value_specs[0].text

        # Return of data to main.py
        return character, specs_array, ascii_array

    # Start of parsing. Parsing names of all characters
    if not str(title[0]).isnumeric():
        letter = letters[title[0].lower()]
        return parsing_group(letter, title)
    else:
        return parsing_group(letters['#'], title)