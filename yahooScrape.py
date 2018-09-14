import datetime
import requests
import bs4 as bs

i = 0
dateNow = datetime.datetime.now().date()
response = requests.get('https://finance.yahoo.com/calendar/ipo?day='+ str(dateNow))
soup = bs.BeautifulSoup(response.text, 'lxml')
for table in soup.findAll('table'):
    for tbody in table.findAll('tbody'):
        for tr in table.findAll('tr'):
            if tr.find('th'):
                continue
            else:
                ticker = tr.findAll("td")[0]
                companyName = tr.findAll("td")[1]
                indexName = tr.findAll("td")[2]
                ipoDate = tr.find("span")
                price = tr.findAll("td")[3]
                priceRange = tr.findAll("td")[4]
                currency = tr.findAll("td")[5]
                shares = tr.findAll("td")[6]
                actions = tr.findAll("td")[7]
                print(ipoDate.text)
