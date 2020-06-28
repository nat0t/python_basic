'''Создать класс TrafficLight (светофор) и определить у него один
атрибут color (цвет) и метод running (запуск). Атрибут реализовать как
приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться
только в указанном порядке (красный, желтый, зеленый). Проверить работу
примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его
нарушении выводить соответствующее сообщение и завершать скрипт.
'''

class TrafficLight():
    __color = ('Red', 'Yellow', 'Green')

    def running(self):
        import time
        # import os
        count = 0
        max_count = 6
        while count < max_count:
            print(f'{TrafficLight.__color[count % 3]} color is on...')
            if count % 3 == 0:
                # os.system('color 4')
                time.sleep(7)
            elif count % 3 == 1:
                # os.system('color 6')
                time.sleep(2)
            elif count % 3 == 2:
                # os.system('color 2')
                time.sleep(5)
            count += 1

if __name__ == '__main__':
    traffic_light = TrafficLight()
    traffic_light.running()