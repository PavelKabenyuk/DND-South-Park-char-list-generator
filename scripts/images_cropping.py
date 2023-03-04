import PIL


# Cropping image for suitable size
def main(path="path"):
    image = PIL.Image.open(path)
    origin_width, origin_height = image.size

    ratio = origin_width/origin_height

    if ratio < 1:
        width = int(200 * ratio)
        height = 200
    else:
        width = 200
        height = int(200 * 1/ratio)

    image_cropped = image.resize((width, height))
    image_cropped.save(path)