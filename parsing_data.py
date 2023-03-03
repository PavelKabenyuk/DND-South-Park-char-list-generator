import requests
from bs4 import BeautifulSoup as BS

request_titles = requests.get("https://southpark.fandom.com/wiki/Portal:Characters")
html_titles = BS(request_titles.content, "html.parser")

characters = []
specifications = []


# Parsing names of all characters
def all_names():
    counter = 0
    for i in range(0, 30):
        for galary in html_titles.select('#mw-content-text'):
            for title in galary.select("#gallery-" + str(i) + " .wikia-gallery-item"):

                counter += 1

                if title.find("i"):
                    character = title.select('.lightbox-caption > i > a')
                else:
                    character = title.select('.lightbox-caption > a')

                print(str(counter) + ": " + character[0].text)
                characters.append(character[0].text)


# Parsing specs
def searching_specs():
    for character in characters:
        title = character.replace(" ", "_")

        request = requests.get("https://southpark.fandom.com/wiki/" + title)
        html = BS(request.content, "html.parser")

        print(character + "\n")

        for el in html.select("section.pi-item > div.pi-item"):
            title_specs = el.select('h3')
            value_specs = el.select('div.pi-font')

            print(title_specs[0].text + ": " + value_specs[0].text)

        print("\n")


all_names()
searching_specs()
