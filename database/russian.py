import pickle
# Русский словарь
word_lists = []
f = open('russian.txt', 'r', encoding='cp1251')
print(f)
q = 0
for i in f:
	q += 1
	word_lists.append(i.replace("\n",""))
	print("\r" + str(q//1532629*100)+"%", end = "\r")
f.close()
print()
fout = open('words.data', 'wb')
if word_lists != []:
	pickle.dump(word_lists, fout)
fout.close()