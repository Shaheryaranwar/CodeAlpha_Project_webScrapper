import requests
from PIL import Image
from io import BytesIO
import urllib.request
from bs4 import BeautifulSoup
url = "https://yts.mx/browse-movies/"
response = requests.get(url)
# print(response)
soup1 = BeautifulSoup(response.text,'html.parser')
frames = soup1.findAll('div',{'class','browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4'})#define class
def save_image_from_url(url, file_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img.save(file_path)
            print(f"Image saved successfully at {file_path}")
        else:
            print("Failed to download image")
    except Exception as e:
        print(f"An error occurred: {e}")


for frame in frames:
    figure = frame.find('figure')
    photo_url = figure.img['src']
    print(photo_url)
    name = photo_url.split('/')
    name = name[-2] + name[-1]
    print(name)
    try:
        save_image_from_url(photo_url, './images/'+name)
        print(f"Image '{name}' downloaded successfully.")
    except Exception as e:
        print(f"Error downloading image '{name}': {e}")


