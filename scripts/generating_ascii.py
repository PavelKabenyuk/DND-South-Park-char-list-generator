import pywhatkit as kt
import os


def main(title="title", image_title="image_title", source_path="source_path"):
    current_directory = os.getcwd()
    target_directory = os.path.join(current_directory, "data/ASCII", "characters", title)

    if not os.path.exists(target_directory):
        os.mkdir(target_directory)

    target_path = target_directory + "/" + image_title

    if not os.path.exists(target_path + ".txt"):
        kt.image_to_ascii_art(source_path, target_path)

    return target_path + ".txt"
