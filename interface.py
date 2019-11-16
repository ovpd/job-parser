from tkinter import *
 

# photo = PhotoImage(file="icon.gif")
# w = Label(parent, image=photo)
# w.photo = photo
# w.pack()

def help_press():
	pass

def parse_press():
	pass

root = Tk()

root.title('Поиск работы jobs.tut.by')

root.geometry('500x430')
 
 

tags = Entry(root)
tags.place(x = 250, y = 90)

tags_label = Label(root, text = ' ключевые слова ')
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