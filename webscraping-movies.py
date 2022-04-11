
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font


#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title


#############################################################



movie_table = soup.find('table')

rows = movie_table.findAll('tr')


'''
## start at 1 not 0 because of the header 
for x in range (1,6):
    cols = rows[x].findAll('td')
    rank = cols[0].text
    name = cols[1].text
    gross = cols[5].text
    total_gross =  cols[7].text


    print(f'Movie Title: {name}')
    print(f'Rank: {rank}')
    print(f'Gross: {gross}')
    print(f'Total Gross: {total_gross}')
    input()
'''


wb = xl.Workbook()

MySheet = wb.active 
MySheet.title = 'Box Office Report'

header_font = Font(name = "Calabri", size = 16, bold = True )


MySheet['A1'] = "No."
MySheet['A1'].font = header_font
MySheet['B1'] = "Movie Title"
MySheet['B1'].font = header_font
MySheet['C1'] = "Release Date"
MySheet['C1'].font = header_font
MySheet['D1'] = "Gross"
MySheet['D1'].font = header_font
MySheet['E1'] = "Total Gross"
MySheet['E1'].font = header_font
MySheet['F1'] = "% of Total Gross"
MySheet['F1'].font = header_font


for x in range (1,6):
    cols = rows[x].findAll('td')
    rank = cols[0].text
    name = cols[1].text
    gross = int(cols[5].text.replace(",", '').replace("$",''))
    total_gross =  int(cols[7].text.replace(",", '').replace("$",''))
    release_date = cols[8].text
    percent_gross = round((gross / total_gross) * 100 , 2)


    MySheet['A' + str(x+1)] = rank
    MySheet['B' + str(x+1)] = name
    MySheet['C'+ str(x+1)] = release_date
    MySheet['D'+ str(x+1)] = gross
    MySheet['E'+ str(x+1)] = total_gross
    MySheet['F'+ str(x+1)] = str(percent_gross) + "%"

MySheet.column_dimensions['A'].width = 5 
MySheet.column_dimensions['B'].width = 30
MySheet.column_dimensions['C'].width = 25
MySheet.column_dimensions['D'].width = 16
MySheet.column_dimensions['E'].width = 20
MySheet.column_dimensions['F'].width = 26


wb.save('BoxOfficeReport.xlsx')