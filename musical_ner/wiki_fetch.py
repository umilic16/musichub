import requests
from bs4 import BeautifulSoup
import csv
import re

# this functions just gets all text from genres page, i formated it manually using regex


def get_all_genres():
    try:
        # URL of the Wikipedia page with the list of music artists
        url = "https://en.wikipedia.org/wiki/List_of_music_genres_and_styles"
        # Send a GET request to the URL and retrieve the HTML content
        response = requests.get(url)
        html_content = response.content
        # print(html_content)
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, "lxml")
        uls = soup.find_all("li")
        genres = []
        for ul in uls:
            line = str(ul.text)
            genres.append(line)
        # save genres, print, whatever
    except:
        pass

# this function gets all artists from all wiki pages in the lists of musicians page
# not 100% accurate needs more cleaning up, but i gave up and cleaned it with regex
def get_all_artists():
    try:
        # URL of the Wikipedia page with the list of music artists
        url = "https://en.wikipedia.org/wiki/Lists_of_musicians"
        # Send a GET request to the URL and retrieve the HTML content
        response = requests.get(url)
        html_content = response.content
        # print(html_content)
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, "lxml")
        links = []
        # get all links for artist lists
        for a in soup.find_all('a', href=True):
            result = re.search(r"/wiki/List_of_.+", a['href'])
            if result:
                # print(result)
                links.append(result.string)
        # print(links)
        # collect every artist from every link
        for link in links:
            url = f"https://en.wikipedia.org/{link}"
            # print(f'contacted link {link}')
            response = requests.get(url)
            html_content = response.content
            soup = BeautifulSoup(html_content, "lxml")
            uls = soup.find_all("li")

            found_start = False
            found_end = False
            text = []
            # the uls that contain artist names have no ids but the ul before the artist names and after it has an id
            # so we go through the uls in between those
            for ul in uls:
                # Skip ul elements until we find the first ul without an id
                if not found_start and ul.has_attr('id'):
                    continue
                else:
                    found_start = True
                # Stop saving ul elements once we find the next ul with an id or class
                if ul.has_attr("id") or ul.has_attr('class'):
                    if not found_end:
                        found_end = True
                        break
                    else:
                        break
                line = str(ul.text)
                if len(line) > 1:
                    text.append(line)
            # save the artists into csv
            with open("data/wiki_data/wiki_artists.csv", "w", newline='', encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['artist'])
                # print(f'writing data from {link}')
                for line in text:
                    writer.writerow([line])
    except Exception as ex:
        print(ex)

get_all_artists()


def get_all_instruments():
    try:
        # URL of the Wikipedia page with the list of insturments
        url = "https://en.wikipedia.org/wiki/List_of_musical_instruments"
        # Send a GET request to the URL and retrieve the HTML content
        response = requests.get(url)
        html_content = response.content
        # print(html_content)
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, "lxml")
        tables = soup.find_all('table', class_='wikitable')
        data = []
        for table in tables:
            if table is not None:
                rows = table.find_all('tr')
                # print(rows)
                for row in rows:
                    if row is not None:
                        instrument = row.find('td')
                        # print(type(instrument))
                        if instrument is not None:
                            data.append(instrument.text.strip())
        # save the instruments into csv
        with open("data/instruments.csv", "w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['instrument'])
            for row in data:
                writer.writerow([row.lower()])
    except Exception as ex:
        print(ex)


# get_all_instruments()
