my_list = []
item = None
while True:
    item = input('Enter the list item (if you want to finish typing, enter "!q"): ')
    if item == '!q':
        break
    my_list.append(item)
print(f'Source list:\n{my_list}')

items = len(my_list) - 1
for index in range(0, items, 2):
    if index == len(my_list) - 1:
        break
    my_list[index], my_list[index+1] = my_list[index+1], my_list[index]
print(f'Processed list:\n{my_list}')