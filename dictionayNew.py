info = {'name': 'Afif',
        'age': 25,
        'city': 'Dhaka'}
print(info)
dicto = dict(num1='value1', key2='value2')
print(dict)
name = info['name']
print(name)
print(dicto.get('key', 'ERROR: Key does not exist and value not found'))

for key in info:
    print(key, info[key]) # Prints key and value
print(info.keys() )