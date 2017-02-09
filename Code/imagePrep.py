from PIL import Image
import os, os.path

def main():
    convert2gray("jpg", "/home/theo/Dropbox/TER/Images/bar chart/", "/home/theo/temp/la/")
    resize("jpg", "/home/theo/Dropbox/TER/Images/bar chart/", "/home/theo/temp/lo/", 100, 100)
    resize2gray("jpg", "/home/theo/Dropbox/TER/Images/bar chart/", "/home/theo/temp/li/", 100, 100)


def convert2gray(ext, path, output):
    output = checkpath(output)
    to = "L"

    if ext == "png":
        to = "LA"

    i = 0
    for imgp in getimgs(path):
        img = Image.open(imgp).convert(to) # convert the image to a 'L' or 'LA' format (both are black and white format)
        img.save(output + str(i) + "." + ext)
        i = i + 1

def getimgs(path):
    imgs = []
    valid_images = [".jpg", ".gif", ".png", ".tga"]
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1] # reverse search of '.' and send it. If no '.', send empty String
        if ext.lower() not in valid_images:
            continue
        imgs.append(os.path.join(path, f))
    return imgs

def resize(ext, path, outputDir, width, height):
    size = width, height
    outputDir = checkpath(outputDir)

    i = 0
    for imgp in getimgs(path):
        img = Image.open(imgp).resize(size, Image.ANTIALIAS) # Resize the image
        img.save(outputDir + str(i) + "." + ext)
        i+=1

def resize2gray(ext, path, outputDir, width, height):
    size = width, height
    outputDir = checkpath(outputDir)
    to = "L"

    if ext == "png":
        to = "LA"

    i = 0
    for imgp in getimgs(path):
        # Resize the image, then
        # convert the image to a 'L' or 'LA' format (both are black and white format).
        img = Image.open(imgp).resize(size, Image.ANTIALIAS).convert(to)  
        img.save(outputDir + str(i) + "." + ext)
        i+=1

def checkpath(path):
    if not (path.endswith("/")):
        path += "/"
    return path

if __name__ == '__main__':
    main()
