import requests


url = 'https://api.stackexchange.com/2.3/search?fromdate=1671408000&todate=1671494400&order=desc&sort' \
      '=activity&tagged=Python&site=stackoverflow'
response = requests.get(url)
for el in response.json()['items']:
    if 'python' in el['title'].lower():
        print(el['title'])