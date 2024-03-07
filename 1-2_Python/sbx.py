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


dish_time_dict = {
    'Рамен с говядиной': 15,
    'Суши': 18,
    'Лагман с курицей': 20,
    'Лагман с говядиной': 24,
    'Плов с курицей': 28
}
street_time_dict  = {
    'Дзержинский': 39,
    'Солнечный': 40,
    'Заводской': 27,
    'Гагаринский': 43,
    'Кировский': 37,
    'Октябрьский': 34
}
dish, street = 'Плов с курицей', 'Солнечный'
if street not in street_time_dict: print('No express in your area')
elif dish not in dish_time_dict: print('Wrong dish')
else:
    t_dish = dish_time_dict.get(dish)
    t_street = street_time_dict.get(street)
    delay = t_dish + t_street - 60
    if delay < 0: print('Coureer will get in time')
    else: print('Coureer will late on', delay, 'minutes')