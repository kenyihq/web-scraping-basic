import requests
import lxml.html as html


XPATH_LINK_TO_ARTICLE = '//div[@class="story-item__information-box w-full"]/h2/a/@href'
XPATH_TITLE = '//div[@class="f just-center"]/div[@class="st-sidebar__container f f-col w-full pos-rel"]/h1[@class="sht__title"]/text()'
XPATH_SUMMARY = '//section/p[@class="story-contents__font-paragraph "]/text()'


def parse_home():
    pass

def run():
    parse_home()


if __name__ == "__main__":
    run()