import math
import numpy as np
from math import exp
import pickle
import os
# from fuzzywuzzy import fuzz as fz

# Global variables
max_words = 100
coder = 500000
hidden_neurons_variable = [15, 25]
data = []
gender = "m" # m (man) or w (woman)
word_lists = []
input_neurons = [0 for i in range(max_words)]
hidden_neurons = [[0 for i in range(hidden_neurons_variable[0])],[0 for i in range(hidden_neurons_variable[1])]]
# output_neurons = [0 for i in range(len(answer))] << строка в коде
answer = [] # список ответов (output нейроны)
w1 = np.random.sample((max_words, hidden_neurons_variable[0]))
# w2 = np.random.sample((hidden_neurons_variable, len(answer))) << строка в коде
# per = 75

# Удаление ненужных символов

def remove(value, deletechars='''1234567890!@"'#$%^&*()_+={[]?><}/:;,.'''):
	for c in deletechars:
		value = value.replace(c, '')
	return value

class Func_Activate:
	# Нахождение сигмоиды
	def sigmoid(self, x):
		return 1 / (1 + math.exp(-x))

	def tozhdestv(self, x):
		return  x

	def default_activation(self, x):
		return self.tozhdestv(self, x)

# Кодирование текста по его индексу из словаря (если же слова нет в списке, то устанавливается значение по умолчанию = 0)
def coder_for_index(txt):
	txt = txt.replace('ё',"е")
	words = txt.split(' ')
	words_out = []
	print(words)
	for i in words:
		q = False
		if remove(i.lower()) != '':
			if remove(i.lower()) in word_lists:
				words_out.append(int(word_lists.index(remove(i.lower()))))
				q = True
			# for j in word_lists:
			# 	if fz.ratio(j,i.lower()) >= per:
			# 		words_out.append(int(word_lists.index(remove(j.lower()))))
			# 		q = True
			# 		break
		if q == False and remove(i.lower()) != '':
			words_out.append(0)
	print(words_out)
	return words_out

###################### Сам код ############################

# Считывание БД словаря
fin = open('words.data', 'rb')
if os.stat(fin.name).st_size != 0:
	word_lists = pickle.load(fin)
fin.close()

# Считывание данных (если они есть)
fin = open('../CC/coder.data', 'rb')
if os.stat(fin.name).st_size != 0:
	data = pickle.load(fin)
fin.close()

for i in data:
	for j in i["second"]:
		answer.append(j)

# data >> [ словарь i-ой переписки { [word_list], [first], [second] } ]

# Рандомные значения для весов
w2 = [np.random.sample((hidden_neurons_variable[0], hidden_neurons_variable[1]))], [np.random.sample((hidden_neurons_variable[1], len(answer)))]
output_neurons = [0 for i in range(len(answer))]



#################### NN ###########################################################



message = ''

while message != 'stop':

	input_neurons = [0 for i in range(max_words)]
	hidden_neurons = [[0 for i in range(hidden_neurons_variable[0])],[0 for i in range(hidden_neurons_variable[1])]]
	output_neurons = [0 for i in range(len(answer))]
	message = input("Ваше сообщение: ")
	message = coder_for_index(message)
	print(message)

	for i in range(len(message)):
		input_neurons[i] = Func_Activate.default_activation(Func_Activate ,message[i])

	# Первый слой от input до первого hidden
	for _hidden in range(hidden_neurons_variable[0]):
		neuron = 0
		# for _in in range(len(message)):
		for _in in range(max_words):
			neuron += (w1[_in][_hidden] * input_neurons[_in])
		hidden_neurons[0][_hidden] = Func_Activate.default_activation(Func_Activate ,neuron)


	#Промежуточные слои
	for count in range(1, len(hidden_neurons_variable)):
		for _hidden_second in range(hidden_neurons_variable[count]):
			neuron = 0
			for _hidden_fisrt in range(hidden_neurons_variable[count-1]):
				# print(count, _hidden_second, _hidden_fisrt, hidden_neurons_variable[1])
				neuron += (w2[count-1][0][_hidden_fisrt][_hidden_second] * hidden_neurons[count-1][_hidden_fisrt])
			hidden_neurons[count][_hidden_second] = Func_Activate.default_activation(Func_Activate, neuron)

	# Послдений слой hidden к output
	for _out in range(len(answer)):
		neuron = 0
		for _hidden in range(hidden_neurons_variable[-1]):
			neuron += (w2[-1][0][_hidden][_out] * hidden_neurons[-1][_hidden])
		output_neurons[_out] = Func_Activate.default_activation(Func_Activate, neuron)

	print(output_neurons)
	# print(output_neurons.index(max(output_neurons)))
	# print("Нейронка: "+answer[output_neurons.index(sorted(output_neurons)[-1])], answer[output_neurons.index(sorted(output_neurons)[-2])], answer[output_neurons.index(sorted(output_neurons)[-3])])
	print(output_neurons.index(max(output_neurons)))
	print("Нейронка: "+answer[output_neurons.index(max(output_neurons))])



######################################################################################

fout = open('words.data', 'wb')
pickle.dump(word_lists, fout)
fout.close()