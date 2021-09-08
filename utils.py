from constants import BASE_URL
import requests
from bs4 import BeautifulSoup




def get_jokes(page_number):
    url = BASE_URL + f"/latest/?page={page_number}"
    jokes = []
    page = requests.get(url)
    try:
        soup = BeautifulSoup(page.content, 'html.parser')
        fetched_jokes = soup.find_all(class_='quote post-content post-body')
        for result in fetched_jokes:
            jokes.append(str(result.text.strip()))
    except Exception as e:
        print("Getting Error: ", str(e))
    return jokes