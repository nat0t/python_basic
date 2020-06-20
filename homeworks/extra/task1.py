'''
Вавилонцы решили построить удивительную башню —
расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
Она устроена следующим образом — на первом этаже одна комната,
затем идет два этажа, на каждом из которых по две комнаты,
затем идёт три этажа, на каждом из которых по три комнаты и так далее:
         ...
     12  13  14
     9   10  11
     6   7   8
       4   5
       2   3
         1
Эту башню решили оборудовать лифтом --- и вот задача:
нужно научиться по номеру комнаты определять,
на каком этаже она находится и какая она по счету слева на этом этаже.
Входные данные: В первой строчке задан номер комнаты N целое цисло, от 1 до  бесконечности.
Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
Пример:
Вход: 13
Выход: 6 2
Вход: 11
Выход: 5 3
'''
import time
def babylon_tower1(room: str) -> tuple:
    """
    Function takes room number and returns floor and flat number on the floor
    in Babylon tower.
    :param room:
    :return:
    """
    if room.isdigit() and int(room) != 0:
        room = int(room)
        floor = 1
        block = 1
        position = 0
        # Search number of room block (1x1, 2x2, 3x3 rooms, etc.).
        while room > position + block ** 2:
            position += block ** 2
            floor += block
            block += 1
        # Search number of floor in the current block.
        while room > position + block:
            position += block
            floor += 1
        # Search number of flat on current floor.
        flat = 1
        while room > position + flat:
            flat += 1
        position += flat - 1

        return floor, flat
    else:
        print('Incorrect number.')

def babylon_tower2(room: str) -> tuple:
    #last floor in block
    l_floor = 0
    #last room in block
    l_room = 0
    room = int(room)
    for block in range(room):
        if room > l_room:
            l_floor += block
            l_room += block ** 2
        else:
            break
    floor = l_floor - (l_room - room) // (block - 1)
    offset = block - (l_room - room) % (block - 1) - 1
    return floor, offset

room = input('Enter number of room: ')
start = time.time()
print(babylon_tower1(room))
print(f'Time of variant 1: {time.time() - start}')

start = time.time()
print(babylon_tower2(room))
print(f'Time of variant 2: {time.time() - start}')