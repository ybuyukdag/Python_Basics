import requests
from bs4 import BeautifulSoup


url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html = requests.get(url).content

soup = BeautifulSoup(html,"html.parser")

list = soup.find("tbody",{"class":"lister-list"}).find_all("tr")

for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).text.replace("\n"," ").replace("      ","").replace("       ", " ")
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).text.replace("\n","")
    print(title,"- Rate: ",rating)

