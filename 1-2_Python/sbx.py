# new_str = 'Perfect'
# print(new_str[5])
# print(new_str[1:])
# print(new_str[::2])
#----------------------
# s1 = "Per"
# s2 = "fec"
# s3 = "fe"
# s4 = "ct"
# new_string = s1 + s2 + s4[1:]
# print(new_string)
# print(new_string.find('fe'))
# poem = '''Two roads diverged in a yellow wood,
# And sorry I could not travel both
# And be one traveler, long I stood
# And looked down one as far as I could
# To where it bent in the undergrowth.'''
# poem_list = poem.split('\n')
# print(poem_list)
#----------------------8.6
# numbers = '1 2 3 4 5 6 7'
# num_lst = numbers.split()
# num_abs = '\n'.join(num_lst)
# print(num_abs)
#----------------------8.6
# help(str.format)

#--------------------------------------------Python 2--------------------------------------------

# lst = range(1,11)
# print(lst)
# lst = list(lst)
# print(lst)
# invert_lst = lst[::-1]
# print(invert_lst)

# a = 1
# b = 2
# c = 3
# orderds = []
# orderds.append(a)
# orderds.append(b)
# orderds.append(c)
# print(orderds)
# print(orderds.count(1))
# orderds.clear()
# print(orderds)
# a = [1, 2, 3]
# b = a.copy()
# c = a[:]
# print(b, c)
# a.extend(b)
# print(a)
# a.reverse()
# print(a)
# a.sort()
# print(a)
# #--------------------------------------------Dictionary--------------------------------------------
# phones = {'+79033923029': 'Ivan Ivanov', '+78125849204': 'Kirill Smirnov', '+79053049385': 'Mark Parkhomenko', '+79265748370': 'Ekaterina Dmitrieva', '+79030598495': 'Ruslan Belyi'}
# print(phones.keys())
# phones.clear()
# # print(phones)
# test_dict = {1:"one", 2:"two", 3:"three",}
# # print(test_dict[4]) # KeyError
# print(test_dict.get(4, 'DefaultValue'))
# print(test_dict.get(3))
# test_dict.update({4:'four', 5:'five'})
# print(test_dict)
# test_dict.update({5:'PYAT'})
# print(test_dict)
# test_dict.pop(5)
# print(test_dict)
# complex_dict = {'name':'Alex', 'age':30, 'bio':
#                 {'company':'Yandex',
#                  'job':'Developer'}}
# print(complex_dict['bio']['job'])


# #--------------------------------------------Sets--------------------------------------------
# test_set = {1, 2, 3, 4, 5}
# str_set = set('sdlkjaslkdjalkfa')
# print(str_set)
# str_set.add('O')
# print(str_set)
# str_set.add('newlettersinstring')
# print(str_set)
# str_set.discard('O') # no KeyError if missing
# str_set.discard('a') # KeyError if missing
# print(str_set)

# cluster1 = {"item1", "item2", "item3", "item4"}
# cluster2 = {"item2", "item3", "item5", "item7"}
# print('cl1: ', cluster1)
# print('union cl: ', cluster1.union(cluster2))
# cluster3 = cluster1.union(cluster2)
# print('cl3: ', cluster3)
# intcl = cluster1.intersection(cluster2)
# print('intersection: ', intcl)

# #--------------------------------------------Type transformation--------------------------------------------

# float_var = float(10)
# int_var = int(10.2)
# print(int_var)
# print(str(float_var + int_var))
# str_var = str(float_var + int_var)


# #--------------------------------------------Operations--------------------------------------------
# tst_str = 'qwepoi'
# print(tst_str[::-1])
# str1 = "коту тащdт уток"
# str1 = str1.replace(" ", "")
# str1 = str1.lower()
# print(str1)
# print(str1 == str1[::-1])

# a, b, c = 2, 5, 8
# print((a**2 > b) and (a**2 > c))
# a = 154
# b = a
# print(b)
# print(a is b)
# a = 3
# print(a is b)
# print(b)


# arrival_of_goods = {
#     '148902': {
#         'Футболка с принтом': 180,
#         'Свитшот черный': 245,
#         'Джинсы серые': 252
#     },
#     '893516': {
#         'Футболка с принтом': 43,
#         'Свитшот черный': 64,
#         'Джинсы черные': 102
#     },
#     '893481': {
#         'Кружка керамическая': 35,
#         'Свитшот черный': 10,
#         'Джинсы сервые': 14
#     }
# }
# print(arrival_of_goods.get('148902'))

# #--------------------------------------------Conditions--------------------------------------------

# mx = 0
# s = 0

# x = -5
# if x < 0:
#     s = x

# if x > mx:
#     mx = x

# print(s)
# print(mx)
# age = 18
# name = 'Jora'
# print('Hi {}, ue age is {}'.format(name, age))
# num = 0
# if num:
#     print(num, ' is not 0')
# else:
#     print(num, ' is 0')


# dish_time_dict = {
#     'Рамен с говядиной': 15,
#     'Суши': 18,
#     'Лагман с курицей': 20,
#     'Лагман с говядиной': 24,
#     'Плов с курицей': 28
# }
# street_time_dict  = {
#     'Дзержинский': 39,
#     'Солнечный': 40,
#     'Заводской': 27,
#     'Гагаринский': 43,
#     'Кировский': 37,
#     'Октябрьский': 34
# }
# dish, street = 'Плов с курицей', 'Солнечный'
# if street not in street_time_dict: print('No express in your area')
# elif dish not in dish_time_dict: print('Wrong dish')
# else:
#     t_dish = dish_time_dict.get(dish)
#     t_street = street_time_dict.get(street)
#     delay = t_dish + t_street - 60
#     if delay < 0: print('Coureer will get in time')
#     else: print('Coureer will late on', delay, 'minutes')

#------5-7-----

# test_date = '16.04.2019 15:59'
# #print(type(test_date))
# date = test_date.split()[0].split('.')
# day, month, year = test_date.split()[0].split('.')
# print(day, month, year)

# #--------------------------------------------Try-Except--------------------------------------------

# try:
#     i = 1/0
# except ZeroDivisionError as e: print('zero division', e) #may be multiply blocks
# else: print('this wont print in this case')
# finally: print('this will be print anyway')

# try:
#     age = int(input('Enter your age'))
#     if age < 0 or age > 100:
#         raise ValueError('Pizdish')
#     else: print ('Your age is', age)
# except ValueError as e: print(e)
# #--------------------------------------------FOR WHILE--------------------------------------------
# incomes = [120, 38.5, 40.5, 80]
# total = 0
# for cash in incomes:
#     total += cash
# print(total)

# num_list = [98, 24, 23, 12, 3]
# p = 1
# for i in num_list:
#     p *= i
# print(p)

# range_lst = list(range(0, 101))
# print(range_lst)

# n = 4
# m = n
# result = 1
# for i in range(2, n+1):
#     m -= 1
#     result = result * i
#     #print(result)
# print(result)

# n = 5
# for i in range(1, n+1):
#     print('*'*i)
# num_list = [1, 10, 3, -5]
# num_list.sort()
# for i in range(len(num_list)):
#     print('Element {}: {}'.format(i, num_list[i]))


# num_list = [10, 4, 4, 21, 2, 0, -10]
# count_even = 0
# for i in num_list:
#     if i%2 == 0:
#         count_even += 1
#         print(i, 'is even')
# print(count_even)


# mixture_list = [True, 1, -10, 'hello', False, 'string_1', 123, 2.5, [1, 2], 'another'] 
# for elem in mixture_list:
#     if type(elem) == str:
#         print(elem, 'is string')


# word_list = ["My", "name", "is", "Sergei", "EOS", "I'm", "from", "Moscow", "EOS"]
# text = ''
# for word in word_list:
#     if word != 'EOS':
#         text += ' '
#         text += word
#     else: text += '.'
# text = text.strip()
# print(text)

# weight_limit = 400
# people = 67
# summary_w = 0
# count = 0
# while summary_w <= weight_limit:
#     summary_w += people
#     count += 1
# print('total count', count -1, 'owerweight:', summary_w - weight_limit)


# number = 1
# value = 151
# while number**2 < value:
#     print(number, 'still less')
#     number += 1
# print(number - 1, 'is closest with square:', (number-1)**2)

# test_var = 0
# for i in range(10):
#    test_var += i
#    print(test_var)

# num = 0 
# while True:
#     num += 1
#     if num 10:
#         break
#     print('New client #', num)

# secret_passwords = {
#     'Enot': 'ulybaka',
#     'Agent12': '1password1',
#     'MouseLulu': 'myshkanaruhka'
# }
# while True:
#     name = input('Insert login: ')
#     if name in secret_passwords:
#         pas = input('Insert password: ')
#         if pas == secret_passwords[name]:
#             print('Login complete')
#             break
#         else: print('Wrong password')
    
#     else: print('Wrong login')

# x = 1
# n = 156
# while x**2 % n != 0:
#     x += 1
#     print(x)
# print(x**2)

# x = 1
# cnt = 1
# val = 1000
# while x < val:
#     x = x * cnt
#     cnt += 1
# print(x)

# money = 8000
# percent = 0.08
# target_money = 15000
# year_count = 0
# while money < target_money:
#     money = money + (money * percent)
#     year_count += 1
# print(money, year_count)

# damdge = 174
# health = 3014
# seconds_num = 0
# while health > 0:
#     health -= damdge
#     seconds_num += 1
# print(health, seconds_num)

# 1 1 2 3 5 8 13 21 34
# fib_list = [1, 1, 2]
# print(fib_list)
# for i in range(10):
#     fib_list.append(fib_list[len(fib_list)-1] + fib_list[len(fib_list)-2])
# print(fib_list)
# FIBANACHI
# a = 1
# b = 1
# i = 2
# n = 10
# lst = [1, 1]
# while i < n:
#     c = a + b
#     i += 1
#     a = b
#     b = c
#     lst.append(c)
# print(lst)

#------Nested loops
# m_lst = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for i in range(len(m_lst)):
#     for j in range(len(m_lst[0])):
#         print(m_lst[i][j])

# hours = range(9, 24, 2)
# minutes = range(0, 60, 15)
# for hour in hours:
#     for minute in minutes:
#         if minute == 0: print(hour, ':0', minute)
#         else: print(hour, ':', minute)

# str_list = ['text', 'morning', 'notepad', 'television', 'ornament']
# cnt = 0
# cnt2 = 0
# for word in str_list:
#     cnt2 += word.count('e')
#     for letter in word:
#         if letter == 'e': cnt += 1
# print(cnt)
# print(cnt2)

# row = [9, 17, 2, 18, 1, 23]
# min = row[0]
# for i in range(1, len(row)):
#     if row[i] < min: min = row[i]
# print(min)

# random_matrix = [
#     [9, 2, 1],
#     [2, 5, 3],
#     [4, 8, 5]
# ]
# max_value_rows = []
# for i in range(0, len(random_matrix)):
#     max_val = random_matrix[i][0]
#     for j in range(0, len(random_matrix[i])):
#         if random_matrix[i][j] > max_val: max_val = random_matrix[i][j]
#     max_value_rows.append(max_val)
# print(max_value_rows)

# student_scores = [
#     [56, 90, 80],
#     [80, 86, 92],
#     [91, 76, 89],
#     [91, 42, 60],
#     [65, 30, 90]
# ]
# math = 0
# inform = 0
# rus = 0
# for i in range(0, len(student_scores)):
#     math += student_scores[i][0]
#     inform += student_scores[i][1]
#     rus += student_scores[i][2]
# print(math/len(student_scores))

# is_square = True
# test_matrix = [
#     [1, 2, 3],
#     [7, -1, 2],
#     [123, 2, -1],
#     [123, 5, 1]
# ]
# line = len(test_matrix[0])
# for row in test_matrix:
#     if len(row) != line or len(row) != len(test_matrix):
#         is_square = False
# print(is_square)

# temp = [[25, 27, 28, 26, 27, -26, -25, -2, 26], [21, 22, 28, 27, 28, 26, 25, 19, 26], [-19, 21, 25, -27, 28, 25, 21, 20, 26]]

# # После обработки
# ## temp = [[25, 27, 28, 26, 27, 26, 25, 2, 26], [21, 22, 28, 27, 28, 26, 25, 19, 26], [19, 21, 25, 27, 28, 25, 21, 20, 26]]
# for i in range(0, len(temp)):
#     for j in range(0, len(temp[0])):
#         if temp[i][j] < 0: temp[i][j] = temp[i][j] * (-1)
#         #print(day)    
# print(temp)

# customer_satisfaction = [
#     [0.87, 0.56, 0.77],
#     [0.22, 0.46, 0.56, 0.89, 0.95],
#     [0.45, 0.44, 0.68],
#     [0.73, 0.88, 0.95, 0.49]
# ]
# month_satisfaction = []

# for i in range(0, len(customer_satisfaction)):
#     month_sum = 0
#     for j in range(0, len(customer_satisfaction[i])):
#         month_sum += customer_satisfaction[i][j]
#     month_satisfaction.append(round(month_sum/(len(customer_satisfaction[i])), 2))
# print(month_satisfaction)

#####-----------------------enumerate()------------------

# user_dynamics = [-5, 2, 4, 8, 12, -7, 5]
# for i, v in enumerate(user_dynamics):
#     if v < 0:
#         print("Day {} dynamics: {}".format(i+1, v))

# str_list = ['Hello', 'my', 'name', 'is', 'Ezeikel', 'I', 'like', 'knitting']
# ## cut_str_list = [[0, 'Hel'], [1, 'my'], [2, 'nam'], [3, 'is'], [4, 'Eze'], [5, 'I'], [6, 'lik'], [7, 'kni']]
# cut_str_list = []
# for i, v in enumerate(str_list):
#     cut_str_list.append([i, v[0:3]])
# print(cut_str_list)

#####-----------------------break & continue------------------
# loot_lst = ['Sword', 'Dagger', 'Great Axe', 'Blunderbus', 'Hatchet']
# backpack = []
# for item in loot_lst:
#     if len(backpack) == 3:
#         print('Inventory is full!!')
#         break
#     backpack.append(item)
# print(backpack)


# n = 81
# # Создаём бесконечный цикл
# while True:
#     # Проверяем условие, что остаток от деления на 3 равен 0.
#     if n % 3 == 0:
#         # Если условие выполняется, новое число — результат целочисленного деления на 3.
#         n = n // 3 
#         # Проверяем условие, что в результате деления получили 1.
#         if n == 1: 
#             # Выводим утвердительное сообщение
#             print('n - is the power of the number 3!')
#             # Выходим из цикла
#             break 
#     else: 
#         # В противном случае выводим сообщение-опровержение
#         print('n - is not the power of the number 3!') 
#         # Выходим из цикла
#         break 
n = 333
origin = n
while True:
    if n % 2 == 0 and n != 1:
        n = n // 2
    elif n % 2 != 0 and n != 1:
        n = ((n * 3) + 1) // 2
    elif n == 1:
        print(n, origin)
        break
