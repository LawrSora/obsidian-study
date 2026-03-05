###1
#def sum(a, b):
#    sum = a + b
#    return sum
#print(sum(1, 2))

###2
#def fio(fio):
#    fio = fio.split(' ')
#    fio = fio[0] + ' ' + (fio[1])[0] + '.' + (fio[2])[0] + '.'
#    return(fio)
#print(fio("Игнашев Никита Сергеевич"))

###3
#def sum_range(start, end):
#    result = 0
#    if(start < end):
#        a = start
#        b = end + 1
#    else:
#        a = end
#        b = start + 1
#    for i in range(a, b):
#        result += i
#    return result
#
#print(sum_range(1, 3))

###4
#def time_do_konca_dnya():
#    from time import localtime
#    now = localtime()
#    total_seconds = (23 - now.tm_hour) * 3600 + (59 - now.tm_min) * 60 + (59 - now.tm_sec)
#    hours = total_seconds // 3600
#    remainder = total_seconds % 3600
#    minutes = remainder // 60
#    seconds = remainder % 60
#    return f"До конца суток осталось: {hours} часов, {minutes} минут, {seconds} секунд"
#
#print(time_do_konca_dnya())

###5
#def amountList(spis):
#    result = 0
#    for i in spis:
#        result += i
#    return result
#
#print(amountList([1, 2, 3, 4, 5, 6, 7]))

###6
#def ploshKrug(rad):
#    S = rad * rad * 3,14
#    return S
#
#print(ploshKrug(15))

###7
#def del3(x):
#    if (x % 3 == 0):
#        return True
#    else:
#        return False
#
#print(del3(11))

###8
#def max(spis):
#    result = spis[1]
#    for i in spis:
#        if(i > result):
#            result = i
#    return result
#print(max([1, 2, 3, 27, 2, 22]))

###9
#def chot(spis):
#    result = 0
#    for i in spis:
#        if(i % 2 == 0):
#            result += 1
#    return result
#print(chot([1, 2, 3, 4, 5, 6, 7, 8, 10]))

###10
#def uniq(spis):
#    result = []
#    for i in spis:
#        for x in range(spis.count(i) - 1):
#            spis.remove(i)
#    return spis
#
#print(uniq([1, 2, 2, 3, 3, 3, 5, 6, 7, 7, 7, 7]))

###11
#def split_fio(full_name):
#    parts = []
#    for part in full_name.split(' '):
#        if part:
#            parts.append(part)
#    return parts[:3]
#
#fio_parts = split_fio("Иванов       Иван   Иванович")
#for i in fio_parts:
#    if i == fio_parts[0]:
#        print("Фамилия:", i)
#    elif i == fio_parts[1]:
#        print("Имя:", i)
#    elif i == fio_parts[2]:
#        print("Отчество:", i)

###12
#def emailProv(email):
#    if(email.endswith('@gmail.com') and email.islower() and ((email.replace('@gmail.com', '')).isalnum()
#            or (email.replace('@gmail.com', '')).isalpha())):
#        return True
#    else:
#        return False
#
#print(emailProv('lawrsora@gmail.com'))

###13
#def get_region(plate_number):
#    region_codes = {
#        '10': 'Москва',
#        '20': 'Санкт-Петербург',
#        '21': 'Архангельск',
#        '19': 'Вологда',
#    }
#
#    cifr = []
#    for char in reversed(plate_number):
#        if char.isdigit():
#            cifr.append(char)
#        else:
#            break
#
#    if (len(cifr) >= 2):
#        code = ''.join(reversed(cifr[-2:]))
#        return region_codes.get(code, 'Код региона неизвестен')
#    else:
#        return 'Код региона не найден'
#
#print(get_region('к118кк20'))
#print(get_region('а123бв21'))
#print(get_region('х999хх19'))
#print(get_region('м000мм10'))

###14
#def convert_temperature(temp, to_fahrenheit=True):
#    if (to_fahrenheit):
#        return temp * 9 / 5 + 32
#    else:
#        return (temp - 32) * 5 / 9
#
#print(convert_temperature(0))
#print(convert_temperature(100))
#print(convert_temperature(32, False))
#print(convert_temperature(212, False))

###15
#def get_season(month_number):
#    if (isinstance(month_number, int) or month_number < 1 or month_number > 12):
#        if month_number in [12, 1, 2]:
#            return "зима"
#        elif month_number in [3, 4, 5]:
#            return "весна"
#        elif month_number in [6, 7, 8]:
#            return "лето"
#        elif month_number in [9, 10, 11]:
#            return "осень"
#        else:
#            return -1
#    else:
#        return -1
#
#print(get_season(4))
#print(get_season(8))
#print(get_season(12))
#print(get_season(0))
#print(get_season(13))
#print(get_season(3.5))

###16
#import math
#
#def treug_S(a, b, c):
#    if (a <= 0 or b <= 0 or c <= 0):
#        return -1
#    if a + b <= c or a + c <= b or b + c <= a:
#        return -1
#    perimeter = a + b + c
#    polu_perimeter = perimeter / 2
#    S = math.sqrt(polu_perimeter * (polu_perimeter - a) * (polu_perimeter - b) * (polu_perimeter - c))
#    return S
#
#print(treug_S(3, 4, 5))
#print(treug_S(5, 5, 5))
#print(treug_S(1, 1, 3))
#print(treug_S(0, 4, 5))
#print(treug_S(7, 10, 5))