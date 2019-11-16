from bs4 import BeautifulSoup
import requests
import xlwt
from collections import OrderedDict



my = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/78.0.3904.97 Chrome/78.0.3904.97 Safari/537.36'



def urls_list(agent, days:int, tag:str, tag_2 = ''):
	"""Возвращает список из ссылок для парсинга данных с сайта jobs.tut.by
	Принимает параметры: 
	1) days - за сколько дней собирать данные (1, 3, 7, 30)
	3) agent - агент браузера(можно узнать вбив в гугл 'my user agent')
	2) 4) tag, tag_2 - строки в виде поисковых тегов, пример "Python" "разработчик" """
	URLS = []

	for page in range(100):

		if tag_2:
			URL = 'https://jobs.tut.by/search/vacancy?L_is_autosearch=false&area=16&clusters=true&currency_code=BYR&enable_snippets=true&search_period={x}&text={y}+{z}&page={ai}'.format(x = days, y = tag, z = tag_2, ai = str(page))
		else:
			URL = 'https://jobs.tut.by/search/vacancy?L_is_autosearch=false&area=16&clusters=true&currency_code=BYR&enable_snippets=true&search_period={x}&text={y}&page={ai}'.format(x = days, y = tag, ai = str(page))

		headers = {'user-agent':'{user_agent}'.format(user_agent=agent)}
		session = requests.Session()
		request = session.get(URL, headers=headers)

		if request.status_code == 200:
			soup = BeautifulSoup(request.content, 'html.parser')
			divs = soup.find('div', attrs = {'data-qa':'vacancy-serp__vacancy'})
			if divs:
				print('Status 200' + ', PAGE:' + str(page+1))
				URLS.append(URL)
			else:
				break
		else:
			break

	return URLS



def vacancy_parse(agent:str, URLS:list):
	'''Cобирает информацию с сайта jobs.tut.by
	Принимает два параметра: 
	1) URLS - список урлов. 
	2) Agent - агент браузера(можно узнать вбив в гугл 'my user agent') 
 	Возвращает переменную data(список из диктов с фильтрованной информацией)'''
	data = []
	headers = {'user-agent':'{user_agent}'.format(user_agent=agent)}
	session = requests.Session()

	for page in URLS:
		request = session.get(page, headers=headers)
		
		if request.status_code == 200:
			print('Status 200' + str(page))
			soup = BeautifulSoup(request.content, 'html.parser')
			divs = soup.find_all('div', attrs = {'data-qa':'vacancy-serp__vacancy'})
			
			for div in divs:

				result=OrderedDict()

				title = div.find('a', attrs={'data-qa':'vacancy-serp__vacancy-title'}).text
				href = div.find('a', attrs={'data-qa':'vacancy-serp__vacancy-title'})['href']
				employer = div.find('a', attrs = {'data-qa':'vacancy-serp__vacancy-employer'}).text
				location = div.find('span', attrs = {'data-qa': 'vacancy-serp__vacancy-address'}).text
				what_to_do = div.find('div', attrs = {'data-qa':'vacancy-serp__vacancy_snippet_responsibility'}).text
				requirements = div.find('div', attrs = {'data-qa':'vacancy-serp__vacancy_snippet_requirement'}).text
				
				result['Вакансия']=title
				result['Работодатель']=employer
				result['Местонахождение']=location
				result['Обязанности']=what_to_do
				result['Требования']=requirements
				result['Ссылка']=href

				try:
					home = div.find('div', attrs = {'data-qa':'vacancy-serp__vacancy-work-schedule'}).text
				except AttributeError:
					result['Можно находится дома'] = 'Нет'
				else:
					result['Можно находится дома'] = 'Да'
				

				data.append(result)

	return data		



def unique_name(days:int, tag:str, tag_2=''):
	"""генерирует правильную имя для будущего документа эксель, ест параметры: 
	days - за сколько дней собирать данные (1, 3, 7, 30)
	tag и tag_2 - строки в виде поисковых тегов, пример "Python" "developer" """
	
	if not tag_2:
		name = "TUTBY_" + str(days) + "day(s)" + "_" + tag.lower()
	else:
		name = "TUTBY_" + str(days) + "day(s)" + "_" + tag.lower() + "_" + tag_2.lower()
	return name



def excel_save(data:list, name:str):
	'''eats list with dicts and returns exele document'''
	row = 0
	column = 0

	book = xlwt.Workbook(encoding="utf-8")
	sheet1 = book.add_sheet("Hello, World", cell_overwrite_ok=True) 

	for i in data:
		column_naming=0
		for j in i:
			sheet1.write(0, column_naming, j)
			column_naming+=1

	for i in data:
		row+=1
		column=0
		for j in i:
			sheet1.write(row, column, i[j])
			column+=1

	book.save("{x}.xls".format(x = name))

excel_save(vacancy_parse(my, urls_list(my, 1, "Python", "разработчик")), unique_name(1, "Python", "разработчик"))



