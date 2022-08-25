import requests
import lxml.html as html
import os
import datetime

HOME_URL = 'https://elcomercio.pe/ultimas-noticias/'

XPATH_LINK_TO_ARTICLE = '//div[@class="story-item__information-box w-full"]/h2/a/@href'
XPATH_TITLE = '//div[@class="f just-center"]/div[@class="st-sidebar__container f f-col w-full pos-rel"]/h1[@class="sht__title"]/text()'
XPATH_SUMMARY = '//section/p[@class="story-contents__font-paragraph "]/text()'


def parse_notice(link, today):
    try:
        response = requests.get(link)

        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)

            try:
                title = parsed.xpath(XPATH_TITLE)[0]
                title = title.replace('\"', '')
                summary = parsed.xpath(XPATH_SUMMARY)[0]

            except IndexError as ve:
                return

            with open(f'{today}/title.txt', 'w', encoding='utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(summary)

        else:
            raise ValueError(f'Error: {response.status_code}')

    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response = requests.get(HOME_URL)

        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            link_to_notice = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            
            #print(len(link_to_notice))

            today = datetime.date.today().strftime('%d-%m-%Y')
            if not os.path.isdir(today):
                os.mkdir(today)

            for link in link_to_notice:
                parse_notice(link, today)
            
        else:
            raise ValueError(f'Error: {response.status_code}')


    except ValueError as ve:
        print(ve)

def run():
    parse_home()


if __name__ == "__main__":
    run()