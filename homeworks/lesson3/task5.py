'''Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
специальный символ, выполнение программы завершается. Если специальный символ
введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
'''
def summator(numbers: str) -> float:
    """
    Function returns sum of numbers from string-argument.
    :param numbers:
    :return:
    """
    try:
        return sum(map(float, numbers.split()))
    except ValueError:
        print("It's not numbers.")

if __name__ == '__main__':
    result = 0
    numbers = ''
    print('Enter some numbers separated by spaces (if you want to finish typing, enter "!q"):')
    while not '!q' in numbers:
        numbers = input()
        stop = numbers.find('!q')
        try:
            if stop != -1:
                result += summator(numbers[:stop])
                print(result)
            else:
                result += summator(numbers)
                print(result)
        except TypeError:
            print("It's not numbers.")
            break