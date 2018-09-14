import datetime
import requests
import bs4 as bs
from datetime import datetime, timedelta
import csv

#figure out today's date and the first and last day of this week

weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday", "Sunday"]
today = datetime.today().weekday()
todayDate = datetime.today()
beginWeek = datetime.today() - timedelta(days=(today+1))
endWeek = beginWeek + timedelta(days=6)

#make a list for all dates in this week
datesInWeek =[]

for x in range (0, 7):
    datesInWeek.append((beginWeek + timedelta(days = x)).strftime('%Y-%m-%d'))


with open('econEvents.csv', 'a') as csvfileB:
    fieldnames = ['Date',
                  'Event',
                  'Country',
                  'Event Time',
                  'For',
                  'Actual',
                  'Expected',
                  'Prior',
                  'Revised From',
                  ]
    writer = csv.DictWriter(csvfileB, fieldnames=fieldnames, lineterminator = '\n')
    writer.writeheader()
    #perform main function for each day in week
    for x in range (0, 7):
        response = requests.get('https://finance.yahoo.com/calendar/economic?from=' + beginWeek.strftime("%Y-%m-%d") +'&to=' + endWeek.strftime("%Y-%m-%d") + '&day=' + datesInWeek[x] )
        soup = bs.BeautifulSoup(response.text, 'lxml')
        for table in soup.findAll('table'):
            for tbody in table.findAll('tbody'):
                for tr in table.findAll('tr'):
                    if tr.find('th'):
                        continue
                    else:
                        if tr.findAll("td")[1].text == "US":
                            dateListed = str(datesInWeek[x])
                            event = tr.findAll("td")[0].text
                            country = tr.findAll("td")[1].text
                            eventTime = tr.findAll("td")[2].text
                            forPeriod = tr.findAll("td")[3].text
                            actual = tr.findAll("td")[4].text
                            expected = tr.findAll("td")[5].text
                            prior = tr.findAll("td")[6].text
                            revised = tr.findAll("td")[7].text
                        
                            writer.writerow({'Date': dateListed,
                                             'Event': event,
                                             'Country': country,
                                             'Event Time': eventTime,
                                             'For': forPeriod,
                                             'Actual': actual,
                                             'Expected': expected,
                                             'Prior': prior,
                                             'Revised From': revised,
                                             })

print("Done.")
