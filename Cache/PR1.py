#1
##x = int(input('Введите число:'))
##newx = 0
##if x != 0:
##    while x > 0:
##        newx = newx * 10 + (x % 10)
##        x = x // 10
##print('Ответ:', newx)

#2
##x = int(input('Введите число:'))
##b = 0
##while x > 0:
##    c = x % 10
##    if c > b:
##        b = c
##    x = x // 10
##print('Ответ:', b)

#3
#while exit != 'exit':
#    a = int(input('Введите первое число:'))
#    b = int(input('Введите второе число:'))
#    o = input('Введите оператор:')
#    if o == '+':
#        r = a + b
#    elif o == '-':
#        r = a - b
#    elif o == '*':
#        r = a * b
#    else:
#        r = a/b
#    print('Ответ:', r)
#    exit = (input('Хотите продолжить?:[yes][exit]'))
#    continue

#4
#str = input('Введите слово:')
#mas = []
#for i in str:
#    mas += i
#mas.reverse()
#if  str == (''.join(mas)):
#    print('Слово является палиндромом')
#else:
#    print('Слово не является палиндромом')

#5
#c = int(input('Введите количество символов:'))
#password = ''
#alph = ['1','2','3','4','5','6','7','8','9','0',
#        'a', 'b', 'c', 'd', 'e', 'f', 'g',
#        'h', 'i', 'j', 'k', 'l', 'm', 'n',
#        'o', 'p', 'q', 'r', 's', 't', 'u',
#        'v', 'w', 'x', 'y', 'z']
#while c > 0:
#    import random
#    i = random.randrange(0, 36)
#    password += alph[i]
#    c -= 1
#print(password)

#6 бесконечно, пока не закончим. Фикс каждые 3 игры.
#import random
#game = 'yes'
#schpl = 0
#schcomp = 0
#while game == 'yes':
#    game = 3
#    win = 0
#    while game != 0:
#        game -= 1
#        pl = int(input('Ваш жест камень[1]/ножницы[2]/бумага[3] '))
#        comp = (random.randrange(0,4))
#        if  comp == 1:
#            compstr = 'камень'
#        elif comp == 2:
#            compstr = 'ножницы'
#        else:
#            compstr = 'бумага'
#        print('Жест компьютера:', compstr)
#        play = pl - comp
#        if play == 1 or play == -2:
#            win += 1
#        elif play == 0:
#            game += 1
#    if win > 1:
#        schpl += 1
#        print('Победа')
#    else:
#        schcomp += 1
#        print('Поражение')
#    game = input('Хотите продолжить?[yes]/[no] ')
#print('Счёт:', schpl, '/', schcomp)

#7
#str = input('Введите строку:')
#c = int(input('Введите сдвиг:'))
#result = ''
#alph = ['а', 'б', 'в', 'г', 'д', 'е',
#        'ж', 'з', 'и', 'й', 'к', 'л',
#        'м', 'н', 'о', 'п', 'р', 'с',
#        'т', 'у', 'ф', 'х', 'ц', 'ч',
#        'ш', 'щ', 'ъ', 'ы', 'ь', 'э',
#        'ю', 'я']
#for i in str:
#    result += alph[alph.index(i) + c]
#print(result)

#8
#queries = [
#    'смотреть сериалы онлайн',
#    'новости спорта',
#    'афиша кино',
#    'курс доллара',
#    'сериалы этим летом',
#    'курс по питону',
#    'сериалы про спорт',
#]
#two = 0
#three = 0
#for i in queries:
#    i.strip()
#    if i.count(' ') == 1:
#        two += 1
#    else:
#        three += 1
#sum = two + three
#two = round(two/sum*100, 2)
#three = round(three/sum*100, 2)
#print('Поисковых запросов, содержащих 2 слов(а):',two,'%')
#print('Поисковых запросов, содержащих 3 слов(а):',three,'%')

#9
#spis = [1,2,2,4,5,6,6,6,6,7,8]
#spis.reverse()
#for i in spis:
#    if spis.count(i) > 1:
#        while spis.count(i) > 1:
#            spis.remove(i)
#spis.reverse()
#print(spis)

#10
#str = "Python делает программирование проще"
#print(' '.join(sorted(str.split(' '), key=len)))

#квадрат полибия
alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ё',
        'ж', 'з', 'и', 'й', 'к', 'л', 'м',
        'н', 'о', 'п', 'р', 'с', 'т', 'у',
        'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
        'ы', 'ь', 'э', 'ю', 'я']
result = []
vib = input('Шифровать или дешифровать?[ш]/[д]')

if vib == 'ш': #Шифровка
    strok = input('Введите строку: ')
    for i in strok:
        if i == ' ':
            result.append(' ')
            continue
        elif alph.count(i):
            i = i.lower()
            x = alph.index(i)//6 + 1
            y = alph.index(i)%6 + 1
        else:
            print('Некорректная строка')
            result = []
            break
        xy = x*10+y
        xy = str(xy)
        result.append(xy)
    print(''.join(result))

else: #Дешифровка
    strok = str(input('Введите зашифрованную строку:'))
    c = len(strok)
    a = 0
    b = 2
    while c != 0:
        if strok[a] == ' ':
            result.append(' ')
            a += 1
            b = a + 2
            c -= 1
            continue
        else:
            w = strok[a:b]
            if w.isdigit():
                a += 2
                b += 2
                w = int(w)
                if (w // 10) > 0 and (w // 10) < 7 and (w % 10) < 7 and (w % 10) > 0 and w < 64:
                    w = alph[((w // 10) - 1) * 6 + (w % 10) - 1]
                    c -= 2
                    result.append(w)
                else:
                    print('Некорректная строка')
                    result = []
                    break

            else:
                print('Некорректная строка')
                result = []
                break
    print(''.join(result))