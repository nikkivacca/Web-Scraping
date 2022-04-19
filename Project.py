'''
Find a 'scrappable' cryptocurrencies website where you can scrape the top 5 
cryptocurrencies and display as a formatted output one currency at a time. 
The output should display the name of the currency, the symbol (if applicable), 
the current price and % change in the last 24 hrs and corresponding price (based on % change)

Furthermore, for Bitcoin and Ethereum, the program should alert you via text if the value 
falls below $40,000 for BTC and $3,000 for ETH.

Submit your GitHub URL which should contain all the files worked in class as well as the above.
'''
from twilio.rest import Client
from urllib.request import urlopen
from bs4 import BeautifulSoup


accountSID = 'AC3dce134ef0d682e6ce6c44a3aba838cb'
authToken = '8cbf2c5ee17ff7d8cf5b628037c3a062'
client = Client(accountSID, authToken)
TwilioNumber = '+12672140922'
mycellphone = '+17327887622'


webpage = 'https://coinmarketcap.com/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title



bitcoin_table = soup.find('table')
rows = bitcoin_table.findAll('tr')

for x in range (1,6):
    cols = rows[x].findAll('td')
    rank = x
    name = cols[1].text
    current_price = cols[2].text.replace(',', '').replace('$','')
    current_price = float(current_price)
    change_percentage = cols[3].text
    change_float = float(change_percentage.text.strip('%'))
    old_price = round(current_price / (1+ (change_float/100)), 2)

    print(f"Name: {name}")
    print(f"Rank : {rank}")
    print(f"Current Price: {current_price}")
    print(f"% Change in last 24 hours: {change_percentage}")
    print(f"Old Price: {old_price}")


    if name == "Bitcoin":
        btcprice = current_price
        if btcprice < 40000:
            textmessage = client.messages.create(to  = mycellphone, from_= TwilioNumber, 
            body ='BTC is below $40,000')
    if name == "Ethereum":
        ethprice = current_price
        if ethprice < 3000:
            textmessage = client.messages.create(to  = mycellphone, from_= TwilioNumber, 
            body ='ETH is below $3,000')

    input()