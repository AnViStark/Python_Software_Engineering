request = int(input ('Введите номер кабинета: '))

dictionary = {
101: {'key': 1234, 'access': True},
102: {'key': 1337, 'access': True},
103: {'key': 8943, 'access': True},
104: {'key': 5555, 'access': False},
None: {'key': None, 'access': False},
}

value = dictionary.get(request)
if value is None:
    value = dictionary.get(None)

print(value.get("key"), value.get("access"))