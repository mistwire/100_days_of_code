from bs4 import BeautifulSoup
import requests as r
import lxml


def send_email():
    return


AMAZON_URL = "https://www.amazon.com/WEN-3410-3-Speed-Remote-Controlled-Filtration/dp/B00LPD9BDI/ref=sr_1_2?keywords=air+filter+woodworking&qid=1644867461&sprefix=air+filter+wood%2Caps%2C71&sr=8-2"
PRICE_TARGET = '100'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36'
accept_language = 'en-US,en;q=0.9'

headers = {
        'Accept-Language': accept_language,
        'User-Agent': user_agent,
        }

amazon_response = r.get(AMAZON_URL, headers=headers)
amazon_soup = BeautifulSoup(amazon_response.content, 'lxml')

current_price_class = 'a-price-whole'
current_whole_price = amazon_soup.find(name='span', class_=current_price_class).getText()

print(current_whole_price.replace('.', ''))
current_price = current_whole_price.replace('.', '')

if current_price < PRICE_TARGET:
    send_email()
