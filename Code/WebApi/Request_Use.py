import requests


def askbasicurl(url):
    data = {'url': ("", url), \
            "appId": ("", "9bdde7d8-e4cf-46d5-a346-dc912e33487b")}
    url = "http://demo.nanonets.ai/ImageCategorization/Label/"
    r = requests.post(url, files=data)
    return r.content


def askbasiclocal():
    data = {'file': open("image.jpg", "rb"), \
            "appId": ("", "14e66690-6efb-46c1-a9c7-559d4b406c28")}
    url = "http://demo.nanonets.ai/ImageCategorization/Label/"
    r = requests.post(url, files=data)
    return r.content
