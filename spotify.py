from bs4 import BeautifulSoup
from urllib.request import urlopen


url = 'https://open.spotify.com/playlist/37i9dQZEVXbMnZEatlMSiu/'
html = urlopen(url)
html_doc = BeautifulSoup(html,"html.parser")
print(html_doc.prettify())

data1 = html_doc.find("div")
print(data1)


song_name = data1.find_all("span",class_ = "track-name")

for i in song_name:
    try:
        print(i.text)
    except Exception:
        pass
print(len(song_name))    


time = data1.find_all("span",class_ = "total-duration")
for i in time:
    print(i.text)
print(len(time))    


data3 = data1.find_all("div",class_ = "tracklist-col name")
print(data3)


data4 = data1.find_all("span",class_ = "artists-albums")
print(data4[0])


data5 = []
for i in data4:
    singer = i.find("span")
    data5.append(i.text)


split_list =[i.split("•") for i in data5]
print(split_list)



singers = []
songs = []
print(singers)
for i in split_list:
    singers.append(i[0])
    print(i[0])
    songs.append(i[1])
    print(i[1])



print(singers)



print(songs)


from datetime import date
import csv
today = date.today()
file_name = str(today) + '.csv'
file = open(file_name,'a+',encoding='utf8')
file.write("song,singer\n")

for i in range(len(singers)):
    data = f'{songs[i]},{singers[i]},\n'
    file.write(data)  