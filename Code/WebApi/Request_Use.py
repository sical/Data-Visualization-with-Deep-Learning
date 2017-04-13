import requests, json


def askbasicurl(url):
    print(url+'aaaadsqdsq')
    data = {'url': ("", url), \
            "appId": ("", "14e66690-6efb-46c1-a9c7-559d4b406c28")}
    url = "http://demo.nanonets.ai/ImageCategorization/Label/"
    r = requests.post(url, files=data)
    return r.content


def askbasiclocal():
    data = {'file': open("image.jpg", "rb"), \
            "appId": ("", "14e66690-6efb-46c1-a9c7-559d4b406c28")}
    url = "http://demo.nanonets.ai/ImageCategorization/Label/"
    r = requests.post(url, files=data)
    return r.content
