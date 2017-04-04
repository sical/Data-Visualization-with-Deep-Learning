

import requests, json
data = {'file':open("train/a330.jpg", "rb"), \
    "appId":("", "14e66690-6efb-46c1-a9c7-559d4b406c28")}
url = "http://demo.nanonets.ai/ImageCategorization/Label/"
r = requests.post(url, files=data)
print (r.content)
