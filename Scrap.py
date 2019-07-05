from bs4 import BeautifulSoup
import requests
import json
import re
import os

def MovieData(number):
    fileToWrite = open(os.getcwd()+"\dataMovie.txt", "a+")
    url = 'https://www.imdb.com/search/title?title_type=feature,tv_movie&colors=color,black_and_white&count=250&start={0}&ref_=adv_nxt'.format(
        str((number * 250) + 1))
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    
    movies = soup.find_all('div', class_="lister-item mode-advanced")
    for movie in movies:
        # Name of movie
        name = movie.h3.a.text
        year = movie.h3.find('span', class_="lister-item-year text-muted unbold")
        yearOfRelease = year.text
        StarRating = "N/A"
        try:
            StarRating = movie.find('div', class_="inline-block ratings-imdb-rating")['data-value']
        except:
            StarRating = "N/A"
            continue
        ListerItem = movie.find('div', class_='lister-item-content')
        getAllPTags = ListerItem.find_all('p')
        CastString = getAllPTags[2].text
        movieDump = {
            "name": name,
            "YOR": yearOfRelease,
            "starCast": CastString,
            "starRating": StarRating,
        }
        fileToWrite.write(json.dumps(movieDump) + "," + "\n")
    fileToWrite.close()


def movie():
    number = 5
    for x in range(0, number + 1):
        MovieData(x)
    print('Done with scrapping do check data.txt file')


if __name__ == '__main__':
    movie()
