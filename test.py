import requests
import lxml.html as html
import os
import datetime


URL = 'http://quotes.toscrape.com/'
XPATH_ABOUT_AUTHOR = '//div[@class="quote"]/span/a/@href'
XPATH_AUTHOR = '//div[@class="author-details"]/h3[@class="author-title"]/text()'
XPATH_AUTHOR_DETAILS = '//div[@class="author-details"]/p/span/text()'
XPATH_DESCRIPTION = '//div[@class="author-description"]/text()'


def parse_author(link, today):
    try:
        response = requests.get(link)

        if response.status_code != 200:
            return f'Error: {response.status_code}'

        info_author = response.content.decode('utf-8')
        parsed = html.fromstring(info_author)
        
        try:
            title = parsed.xpath(XPATH_AUTHOR)[0]
            title = title.replace(' ', '-')
            title = title[:-6]
            born = parsed.xpath(XPATH_AUTHOR_DETAILS)[0]
            born += ' '
            born += parsed.xpath(XPATH_AUTHOR_DETAILS)[1]
            description = parsed.xpath(XPATH_DESCRIPTION)[0]
        except IndexError as e:
            return

        with open(f'{today}/{title}.txt', 'w', encoding='utf-8') as f:
            f.write(title)
            f.write('\n')
            f.write(born)
            f.write(description)

    except ValueError as ve:
        return ve

def run():
    response = requests.get(URL)

    if response.status_code != 200:
        return f'Error: {response.status_code}'

    try:
        summary = response.content.decode('utf-8')
        parsed = html.fromstring(summary)

        author = parsed.xpath(XPATH_ABOUT_AUTHOR)

        author = [f'http://quotes.toscrape.com{i}' for i in author]

        today = datetime.date.today().strftime('%d-%m-%Y')
        if not os.path.isdir(today):
            os.mkdir(today)

        for link in author:
            parse_author(link, today)

        print(author)

    except ValueError as ve:
        return ve    

if __name__ == '__main__':
    run()