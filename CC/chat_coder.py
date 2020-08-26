from colorama import Fore, init
import pickle
import os

init(convert=True)

name1, name2 = ["Алекс", "Мария"]

def remove(value, deletechars='''1234567890!@"'#$%^&*()_+={[]?><}/:;,.'''):
	for c in deletechars:
		value = value.replace(c, '')
	return value

def remove2(value, deletechars='''!@"'#$%^&*() _+={[]?><}/:;,.'''):
	for c in deletechars:
		value = value.replace(c, '')
	return value

def admin(txt):
	print(Fore.RED + txt)
	print(Fore.WHITE)

def adminr(txt):
	print(Fore.LIGHTRED_EX + txt)
	print(Fore.WHITE)

print(Fore.LIGHTRED_EX + """Добро пожаловать в данную программу по кодировании переписок. 
Прошу писать слова правильно. Так же важный момент: важно писать в нижнем регистре, 
кроме слов, где это обязательно. Например: "я решил полететь во Францию". Заметно, 
что первое слово в нижнем регистре, но слово "Франция" с большой, так как это страна.

ВАЖНО: не добавлять личную информацию по типу города, номера телефона, своё имя или пол и т.д.""")
print(Fore.WHITE)

adminr('Что бы выйти с программы нажмите сочетание клавиш "Ctrl" + "C"')

#Функция начала работы программы
def QUESTION():
	Q = input(Fore.RED + 'Вы готовы начать кодирование переписки? Если да - введите "1", если же хотите выйти, то нажмите "0": ' + Fore.WHITE)
	print(Fore.WHITE)
	if Q == "1":
		return True
	elif Q == "0":
		exit()
	else:
		admin("Вы ввели неправильный вариант. Повторите корректно...")
		return QUESTION()

W = QUESTION()

#Пустые БД
chat_list = {
	"word_list": [],
	"first": [],
	"second": [],
}

chat_datalist = []

#Если файл не пуст, то происходит считывание данных из БД
f = open('coder.data','rb')
if os.stat(f.name).st_size != 0:
	chat_datalist = pickle.load(f)
	# print(chat_datalist)
f.close

#Сам цикл по вылопнению кодировки переписок

while W:
	for i in range(2):
		try:
			in1 = input(Fore.BLUE +name1 + ": " + Fore.WHITE)
			in2 = input(Fore.YELLOW + name2 + ": " + Fore.WHITE)
			if remove2(in1) != '':
				chat_list['first'] += [in1,]
				chat_list['word_list'] += remove(chat_list['first'][-1]).split(" ")
			if remove2(in2) != '':
				chat_list['second'] += [in2,]
				chat_list['word_list'] += remove(chat_list['second'][-1]).split(" ")
			chat_list['word_list'] = list(set(chat_list['word_list']))
			# print(chat_datalist)
		except:
			f = open("coder.data",'wb')
			if chat_list['word_list'] != []:
				chat_datalist += [chat_list,]
			pickle.dump(chat_datalist, f)
			f.close
			exit()
input()