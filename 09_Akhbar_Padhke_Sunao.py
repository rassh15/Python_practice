# Program to read news from News Api
# By using News API 
#can get easily from newsapi website

from py import parameters
import json
from win32com.client import Dispatch
import requests
#I save my API key in another python file and 
# importing from it.

my_api = parameters.news_api

def speak(str):
        
    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)


def news_data():

    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=47fb8bbf57d6480ab2689bfc9ec729e4'
    data = requests.get(url)
    parsed_data = json.loads(data.content)

    
    size = len(parsed_data["articles"])
    print("Started")
    speak(f"Total number of healines {size}")
    for i in range(len(parsed_data["articles"])):
        channel_name = parsed_data["articles"][i]["source"]["name"]
        news = parsed_data["articles"][i]['title']
        speak(f"News from {channel_name}")
        speak(news)


if __name__ == '__main__':
    news_data()
    



