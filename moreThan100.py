response = requests.get('https://finance.yahoo.com/calendar/economic?from=2018-09-09&to=2018-09-15&day=2018-09-10')
soup = bs.BeautifulSoup(response.text, 'lxml')
resultsSpan = soup('span', text=re.compile("of \d\d\d results"))[0].text
resultsSpan = resultsSpan.split("of ")[1]
resultsSpan = resultsSpan.split("results")[0]


print(resultsSpan)
