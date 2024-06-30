#!/usr/bin/env python3

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # make an empty dictionary to store the result
    result = {}
    # repeat keys and values simultaneously
    for key, value in zip(keys, values):
        # Add key-value pairs to the dictionary
        result[key] = value
    return result

def shared_values(dict1, dict2):
    # obtain values from dictionaries and convert them to sets
    set1 = set(dict1.values())
    set2 = set(dict2.values())
    # Find the intersection of the two sets
    common_values = set1.intersection(set2)
    return common_values

if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)
