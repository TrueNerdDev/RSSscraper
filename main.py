from bs4 import BeautifulSoup
import requests
import json
import lxml

def save_news(article_list):
    with open('../articles.txt', 'w', encoding="utf-8") as outfile:
        json.dump(article_list, outfile, ensure_ascii=False)



def getnews_rss():

    article_list = []

    try:
        r = requests.get('https://www.astrobl.ru/rss')
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')


        for a in articles:
            title = a.find('title').text
            description = a.find('description').text
            link = a.find('link').text
            published = a.find('pubDate').text

            article = {
                'title' : title,
                'description' : description,
                'link' : link,
                'published' : published
            }

            article_list.append(article)

        return save_news(article_list)
        #return print('The scraping job succeded: ', r.status_code)
    except Exception as e:
        print('The scraping job fail. See exception: ')
        print(e)

def main():
    print('Starting scraping')
    getnews_rss()
    print('Finished scraping')

if __name__ == '__main__':
    main()