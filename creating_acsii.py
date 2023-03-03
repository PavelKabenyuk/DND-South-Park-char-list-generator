import pywhatkit as kt
import os


def main(title, source_path, name):
    current_directory = os.getcwd()
    target_directory = os.path.join(current_directory, "ASCII", "characters", title)

    if not os.path.exists(target_directory):
        os.mkdir(target_directory)

    target_path = target_directory + "/" + name

    if not os.path.exists(target_path + ".txt"):
        kt.image_to_ascii_art(source_path, target_path)

    return target_path + ".txt"