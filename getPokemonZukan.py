# coding: UTF-8
import urllib.request
from bs4 import BeautifulSoup

# URL
url = "https://ja.wikipedia.org/wiki/" + urllib.parse.quote_plus('全国ポケモン図鑑順のポケモン一覧', encoding='utf-8')
# urllib.parse.quote_plus('エヴァンゲリオン', encoding='utf-8')

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = urllib.request.urlopen(url).read()

# htmlをBeautifulSoupで扱う
# soup = BeautifulSoup(html, "html.parser")

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "lxml")


for row in soup.find("table").findAll("a"):
	pokemonUrl = urllib.parse.quote_plus(row.get("href"), encoding='utf-8')
	print(pokemonUrl)
	


