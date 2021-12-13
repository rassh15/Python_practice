"""
Read article using speech module.
Extract article from the website using request module
"""

from bs4 import BeautifulSoup
from win32com.client import Dispatch
import requests

def speak(str):
        
    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)


def article_data():

    url = 'https://towardsdatascience.com/10-python-mini-projects-that-everyone-should-build-with-code-769c6f1af0c4'
    data = requests.get(url)
    soup = BeautifulSoup(data.text,'html.parser')
    articles = []
    for i in range(len(soup.select('.p'))):
        article = soup.select('.p')[i].getText().strip()
        articles.append(article)
    text = " ".join(articles)
    print(text)

    # speak(text)


if __name__ == '__main__':
    article_data()
    



