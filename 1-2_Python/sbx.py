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

cluster1 = {"item1", "item2", "item3", "item4"}
cluster2 = {"item2", "item3", "item5", "item7"}
print('cl1: ', cluster1)
print('union cl: ', cluster1.union(cluster2))
cluster3 = cluster1.union(cluster2)
print('cl3: ', cluster3)
intcl = cluster1.intersection(cluster2)
print('intersection: ', intcl)
