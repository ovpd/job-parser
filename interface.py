from tkinter import *
from skrapper import urls_list, vacancy_parse, unique_name, excel_save
 

def help_press():
	'''запускает окно справки'''
	help_root = Tk()
	help_root.title('')
	text = Text(help_root, wrap = WORD)
	insert_text = "                              Агент пользователя\n\nВведите в поисковую строку google фразу 'my user agent', первое что вам покажет, будет выглядеть примерно так: 'Mozilla/2.5 (Z33) AppleWebKit/111.89 (KHTML, like Gecko) Windows Chromium/12.4.1224.11 Chrome/19.1.2222.12 Safari/231.32'. Эта информация нужна алгоритму, чтобы сымитировать действия вашего браузера.\n\n\n                                Вывод данных\n\nПосле того, как программа нашла данные, она заносит их в таблички и сохраняет в формате xls, вы сможете открыть этот документ с помощью excel и других офисных программ, на Linux с помощью Libre office.\n\n\n\n\n\n\n\n\n                 Разработчик: https://github.com/python77777121/"
	text.insert(INSERT, insert_text)
	text.pack()
	help_root.resizable(False, False)

def parse_press():
	'''передает данные все данные из полей и передаёт в нужные функции из документ skrapper.py'''
	agent_str = agent.get()
	day = 1

	get_days = lbox.curselection()
	days = lbox.get(get_days)

	if days == "за один день":
		day = 1
	elif days == "за три дня":
		day = 3
	elif days == "за семь дней":
		day = 7
	elif days == "за тридцать дней":
		day = 30 


	tags_list = tags.get().split()

	if len(tags_list) == 1:
		excel_save(vacancy_parse(agent_str, urls_list(agent_str, day, tags_list[0])), unique_name(day, tags_list[0]))
	else:
		excel_save(vacancy_parse(agent_str, urls_list(agent_str, day, tags_list[0], tags_list[1])), unique_name(day, tags_list[0], tags_list[1]))






root = Tk()
root.title('Поиск работы jobs.tut.by')
root.geometry('500x430')
root.resizable(False, False)
 

tags = Entry(root)
tags.place(x = 250, y = 90)

tags_label = Label(root, text = ' поисковые теги ')
tags_label.config(font=("Courier", "14"))
tags_label.place(x = 57, y = 88)

agent = Entry(root)
agent.config(width = 15)
agent.place(x = 290, y = 140)


agent_label = Label(root, text = ' агент пользователя ')
agent_label.config(font=("Courier", "14"))
agent_label.place(x = 57, y = 138)


dates = ["за один день", "за три дня", "за семь дней", "за тридцать дней"]


lbox = Listbox(root)
lbox.config(height = 4, width=18)
lbox.place(x = 270, y = 190)
for i in reversed(dates):
	lbox.insert(0, i)

lbox_label = Label(root, text = " собрать вакансии ")
lbox_label.config(font=('Courier', '14'))
lbox_label.place(x = 57, y = 188)

help_button = Button(root, text = ' справка ', command=help_press)
help_button.config(width=14)
help_button.place(x = 70, y = 300)

launch_button = Button(root, text = ' запустить парсинг ', command=parse_press)
launch_button.config(width=20)
launch_button.place(x = 231, y = 300)




root.mainloop()