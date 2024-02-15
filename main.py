from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import smtplib

product_link = "https://www.amazon.in/ASUS-i7-11800H-GeForce-Windows-FX506HE-HN382W/dp/B0CCYGC3TS/ref=sr_1_3?crid=2L4U37ON0BZI5&keywords=asus%2Btuf%2Bgaming%2Bf15&qid=1704447808&sprefix=asus%2Bt%2Caps%2C370&sr=8-3&th=1"

BUDGET = 70000

message = f"DEAR RAHUL SHARMA,\n\nPRODUCT: ASUS TUF Gaming F15\n\nSPECS: 15.6 (39.62 cms) FHD 144Hz\nIntel Core i7-11800H 11th Gen\n4GB NVIDIA GeForce RTX 3050 Ti\nGaming Laptop (16GB/512GB SSD/Windows 11/90WHrs Battery/Black/2.30 Kg)\nFX506HE-HN382W\n\nPRICE : "

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
accept_language = "en-US,en;q=0.9"


sender_email = "killbusyness2@gmail.com"
reciver_email = "killbusyness@gmail.com"
email_appPASS = "axqa kocp vbyh bhda"

twilio_recovery_cde = "BW3VUU1F32EAJ2MK9AW6ZA1G"
twilio_accountSID = "AC52db99bd4a316b84390fff4128c577d9"
twilio_authToken = "b2d39c266b99c5143ffdc7d063e44721"
twilio_number = "+12013545024"
recevier_number = "+918291147114"


def sendSMS(price, product_link):
    client = Client(twilio_accountSID, twilio_authToken)
    global message
    send_message = client.messages.create(
        body=message+f"{price}rs\nPRODUCT LINK : {product_link}",
        from_=twilio_number,
        to=recevier_number)

def sendEmail(price, product_link):
    send_mail = smtplib.SMTP("smtp.gmail.com")
    send_mail.starttls()
    send_mail.login(user=sender_email, password=email_appPASS)
    send_mail.sendmail(from_addr=sender_email, to_addrs=reciver_email,
                       msg=message+f"{price}rs\nPRODUCT LINK : {product_link}")

product_headers = {'User-Agent': user_agent, 'Accept-Language': accept_language}
make_connection = requests.get(url=product_link, headers=product_headers)

soup = BeautifulSoup(make_connection.text, 'html.parser')
product_price = float(soup.find_all(name="span", class_="a-price-whole")[0].getText().replace(',', ""))
if product_price <= BUDGET:
    sendSMS(product_price, product_link)
    sendEmail(product_price, product_link)
