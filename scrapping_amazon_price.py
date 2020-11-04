
import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = 'https://www.amazon.in/Beautiful-Solid-Crystal-Enlightening-Living/dp/B08D8D7L3S/ref=sr_1_23?dchild=1&keywords=epoxy+resin+table&qid=1604382365&sr=8-23'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

page = requests.get(url, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')
# To visualize the result use
# print(soup.prettify())

def send_mail():
  server = smtplib.SMTP('smtp.gmail.com',587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('#sender email','#google password authentication')

  subject = 'Price fell down!'

  body = ' Check out the product at: https://www.amazon.in/Beautiful-Solid-Crystal-Enlightening-Living/dp/B08D8D7L3S/ref=sr_1_23?dchild=1&keywords=epoxy+resin+table&qid=1604382365&sr=8-23'

  msg = f"Subject:{subject}\n\n{body}"

  server.sendmail(
      '#sender email',
      '#recipient email',
      msg
  )
  print('Email has been sent for price drop!')


def check_price():
  page = requests.get(url, headers = headers)
  soup = BeautifulSoup(page.content, 'html.parser')

  title = soup.find(id = "title").get_text()
  print(title.strip())

  price = soup.find(id = "priceblock_ourprice").get_text()[2:8]
  price = price.replace(',','')
  price = float(price)
  print(price)

  if(price<66000):
    send_mail()

while(True):
  check_price()
  time.sleep(30)
