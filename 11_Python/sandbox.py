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