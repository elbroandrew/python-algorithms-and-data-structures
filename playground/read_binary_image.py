import requests

res = requests.get('https://fastly.picsum.photos/id/180/200/200.jpg?hmac=YtJJ-CeQThqv_K6NzUnKS6Q8-tjxUVkSKeDsStrjEyM')

with open("image.jpg", 'wb') as file:
    file.write(res.content)


