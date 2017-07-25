# encoding=utf-8

import requests
from bs4 import BeautifulSoup
import codecs


def download_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    data = requests.get(url, headers=headers).content
    return data

def parse_html(html):
    global count
    soup = BeautifulSoup(html, "html.parser")
    music_list_soup = soup.find('div', attrs={'class': 'indent'})

    music_name_list = []
    for music_li in music_list_soup.find_all('table'):
        detail = music_li.find('div', attrs={'class': 'pl2'})
        count += 1
        music_name = 'Top ' + str(count)
        music_name = music_name + detail.find('a').getText() + '\n'
        music_name_list.append(music_name)

    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    if next_page:
        return music_name_list, next_page['href']
    else:
        return music_name_list, None

def main():
    url = 'https://music.douban.com/top250'
    fp = codecs.open('music.txt', 'w', encoding='utf-8')
    while url:
        html = download_page(url)
        musics, url = parse_html(html)
        fp.write(''.join(musics))

    print('done\n')


if __name__ == '__main__':
    count = 0
    main()