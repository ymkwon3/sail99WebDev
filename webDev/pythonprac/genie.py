from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701', headers=headers)

# html 파싱
soup = BeautifulSoup(data.text, 'html.parser')

# 노래 순위
music = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for m in music:
    rank = m.select_one('tr > td.number').text[0:2].strip()
    title = m.select_one('tr > td.info > a.title').text.strip().lstrip("19금").strip()
    singer = m.select_one('tr > td.info > a.artist').text.strip()
    print(rank, title, singer)