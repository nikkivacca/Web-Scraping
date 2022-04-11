'''
Find a 'scrappable' cryptocurrencies website where 
you can scrape the top 5 cryptocurrencies and 
display as a formatted output one currency at a time. 
The output should display the name of the currency, 
the symbol (if applicable), the current price and 
% change in the last 24 hrs and corresponding price 
(based on % change)

Furthermore, for Bitcoin and Ethereum, 
the program should alert you via text if the value 
falls below $40,000 for BTC and $3,000 for ETH.

Submit your GitHub URL which should contain all the 
files worked in class as well as the above.
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

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
    current_price = cols[2].text
    change_percentage = cols[3].text
   # old_price = 

    print(f"Name: {name}")
    print(f"Rank : {rank}")
    print(f"Current Price: {current_price}")
    print(f"% Change in last 24 hours: {change_percentage}")
   # print(f"Old Price: {old_price}")

    input()
