import requests
from bs4 import BeautifulSoup as BS
import pandas as pd

url = 'https://www.catch.co.kr/api/v1.0/jobn/interview/comp/mainQuestionList?JobCode=&RecruitGubun=&Year=&Term=&JinhakCode=&Keyword=삼성&CurPage=1&PageSize=3'
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}

r = requests.get(url, headers=head)

bs = BS(r.text)

print(bs)