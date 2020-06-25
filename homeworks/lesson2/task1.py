my_list = [1, 5.69, complex(9,4),
           'hello world', [1,2,3], (1,2,3), set('abc'),
           {'name': 'Johan', 'age': 23, 'car': 'Toyota'},
           True, b'123j', bytearray(b'text'), None
           ]
print(f'{"Variable":^45} | {"Type":^15}')
for i in range(70):
    print('-', end='')
print()
for item in my_list:
    print(f'{str(item):<45} | {str(type(item)):<15}')