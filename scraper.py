from turtle import title
import requests
import time
from bs4 import BeautifulSoup
import smtplib #enables us to send emails
URL = 'https://www.amazon.in/FADDY-NATIVE-Naruto-Anime-Hokage/dp/B09PYSSSFS?ref_=ast_sto_dp&th=1&psc=1'

headers = { "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'} 
def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    print(title)
    price = soup.find("span", attrs={
        "class": "a-price-whole"}).get_text()
    converted_price = float(price[0:4])
   
    if(converted_price < 649):
        send_mail()

    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() #a command sent by an email server to identify itself when connecting to another email server to start
    #the process of sending an email.
    server.starttls() # it encrypts our connection
    server.ehlo()

    server.login('shourya.bhatnagar131@gmail.com','ygctkhcuyzqnshuk')
    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/FADDY-NATIVE-Naruto-Anime-Hokage/dp/B09PYSSSFS?ref_=ast_sto_dp&th=1&psc=1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'shourya.bhatnagar131@gmail.com',
        'shouryabeast14@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')
    server.quit()
while(True):
    check_price()
    time.sleep(86400)








