from bs4 import BeautifulSoup
import requests

def URL_creator(days, tag, tag_2 = ''):
	if tag_2:
		URL = 'https://jobs.tut.by/search/vacancy?search_period={x}&clusters=true&area=1002&currency_code=BYR&text={y}+{z}&enable_snippets=true'.format(x = days, y = tag, z = tag_2)
	if not tag_2:
		URL = 'https://jobs.tut.by/search/vacancy?search_period={x}&clusters=true&area=1002&currency_code=BYR&text={y}&enable_snippets=true'.format(x = days, y = tag)
	return URL


headers = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/78.0.3904.97 Chrome/78.0.3904.97 Safari/537.36'}
URL = 'https://jobs.tut.by/search/vacancy?search_period=3&clusters=true&area=1002&currency_code=BYR&text=Python&enable_snippets=true'

def search(URL):

	session = requests.Session()
	request = session.get(URL, headers=headers)
	data = []

	if request.status_code == 200:
		print('Status 200')

		soup = BeautifulSoup(request.content, 'html.parser')
		divs = soup.find_all('div', attrs = {'data-qa':'vacancy-serp__vacancy'})
		
		for div in divs:
			title = div.find('a', attrs={'data-qa':'vacancy-serp__vacancy-title'}).text
			href = div.find('a', attrs={'data-qa':'vacancy-serp__vacancy-title'})['href']
			employer = div.find('a', attrs = {'data-qa':'vacancy-serp__vacancy-employer'}).text
			location = div.find('span', attrs = {'data-qa': 'vacancy-serp__vacancy-address'}).text
			what_to_do = div.find('div', attrs = {'data-qa':'vacancy-serp__vacancy_snippet_responsibility'}).text
			requirements = div.find('div', attrs = {'data-qa':'vacancy-serp__vacancy_snippet_requirement'}).text
			
			result = {"title":title,
			"employer":employer,
			"what_to_do":what_to_do,
			"requirements":requirements,
			"href":href}
			
			data.append(result)

	return data		


print(len(search(URL_creator("3", "Java"))))