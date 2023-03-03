import requests
import os
import urllib
from bs4 import BeautifulSoup as BS

request_titles = requests.get("https://southpark.fandom.com/wiki/Portal:Characters")
html_titles = BS(request_titles.content, "html.parser")


# Parsing names of all characters
def all_names(name):
    counter = 0
    for i in range(0, 30):
        for galary in html_titles.select('#mw-content-text'):
            for title in galary.select("#gallery-" + str(i) + " .wikia-gallery-item"):

                counter += 1

                if title.find("i"):
                    character = title.select('.lightbox-caption > i > a')
                else:
                    character = title.select('.lightbox-caption > a')

                if name == character[0].text:
                    return searching_specs(name)


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
        image_path = directory + "/" + image_name + ".png"

        if not os.path.exists(image_path):
            urllib.request.urlretrieve(image, image_path)

    for el in html.select("section.pi-item > div.pi-item"):
        title_specs = el.select('h3')
        value_specs = el.select('div.pi-font')

        print(title_specs[0].text + ": " + value_specs[0].text)

    print("\n")


all_names("Adolf Hitler")
