import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

#html 파싱
soup = BeautifulSoup(data.text, 'html.parser')

#영화 정보들 선택
movies = soup.select('#old_content > table > tbody > tr')
# print(movies)

#순위, 제목, 평점순으로 출력
for m in movies:
    a = m.select_one('td.title > div > a')
    if a is not None:
        title = a.text
        rank = m.select_one('td.ac > img')['alt']
        star = m.select_one('td.point').text
        print(rank, title, star)