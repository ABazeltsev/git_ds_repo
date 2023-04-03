#-----Function for DF.APPLY() test
def get_street_type(address):
    exclude_list = ['N', 'S', 'W', 'E']
    address_list = address.split(' ')
    street_type = address_list[-1]
    if street_type in exclude_list:
        street_type = address_list[-2]
    return street_type
#-----Function for DF.APPLY() test

#-----Function for 11.4.2
def get_weekend(weekday):
    weekend = [5, 6]
    if weekday not in weekend: return 0
    return 1
#-----Function for 11.4.2


#-----Function for 11.4.4
def get_experience(arg):
    month_key_words = ['месяц', 'месяцев', 'месяца']
    year_key_words = ['год', 'лет', 'года']
    args_splited = arg.split(' ')
    month = 0
    year = 0
    for i in range(len(args_splited)):
        if args_splited[i] in month_key_words:
            month = args_splited[i-1]
        if args_splited[i] in year_key_words:
            year = args_splited[i-1]
    return int(year)*12 + int(month)    
#-----Function for 11.4.4


#-----Function for 11.6.12
def get_daytime(time):
    if 0 <= time <= 6:
        return 'night'
    elif 6 < time <= 12:
        return 'morning'
    elif 12 < time <= 18:
        return 'day'
    elif 18 < time <= 23:
        return 'evening'
#-----Function for 11.6.12
