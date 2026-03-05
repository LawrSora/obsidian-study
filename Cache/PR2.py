#1
#str = 'Привет, мир!'
#str = str.upper()
#str = str.replace(',', '!')
#print(str)

#2
#str = input('ведите строку:')
#count = (str.strip()).count(' ') + 1
#print(count)

#3
#str = input('Введите слово для проверки:')
#str = (str.strip()).lower()
#str2 = ''
#for i in str:
#    str2 = i + str2
#if str == str2:
#    print('Это палиндром')
#else:
#    print('это не палиндром')

#4
#spis =  [3, 1, 4, 1, 5, 9]
#spis.append(2)
#spis.pop(0)
#spis.sort()
#print(spis)

#5
#slov = {'ФИО' : 'Филимонов Иван Олегович',
#        'группа' : 'ИВ2-23-2', 'средний балл' : 5.5}
#slov.update({'email':'fill@mil.ussr'})
#slov.update({'средний балл': 5.6})
#print(slov)

#6
#kor = (2, 3, 2, 4, 2, 5, 2, 6, 2)
#print(kor.count(2))

#Доп.
#str = input('Введите строку:')
#slov = {}
#for i in str:
#    slov.setdefault(i, str.count(i))
#print(slov)
