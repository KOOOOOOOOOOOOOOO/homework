import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo')

soup = BeautifulSoup(data.text, 'html.parser')

base_rank = soup.select('#regularTeamRecordList_table > tr')

for ranking in base_rank:
        rank = ranking.select_one('th > strong').text
        name = ranking.select_one('td.tm > div > span').text
        score = float(ranking.select_one('td > strong').text)
        if score > 0.5:
            print(rank, name, score)