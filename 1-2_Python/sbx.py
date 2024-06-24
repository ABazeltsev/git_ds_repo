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

damdge = 174
health = 3014
seconds_num = 0
while health > 0:
    health -= damdge
    seconds_num += 1
print(health, seconds_num)