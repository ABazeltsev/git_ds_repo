def get_street_type(adress):
    exclude_list = ['N', 'S', 'W', 'E']
    adress_list = adress.split(' ')
    street_type = adress_list[-1]
    if street_type in exclude_list: street_type = adress_list[-2]
    return street_type

#test for commit
a = "test string"