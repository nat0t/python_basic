import sys

try:
    hours, rate, bonus = map(float, sys.argv[1:4])
    if hours < 0 or rate < 0 or bonus < 0:
        print(f'Incorrect parameters are entered. '
              f'Parameters must be not negative numbers.')
    else:
        salary = hours * rate + bonus
        print(f'Your salary is {salary} roubles.')
except ValueError:
    print(f'Incorrect parameters are entered. '
          f'Enter your hours of work, rate and bonus as parameters.')
except TypeError:
    print(f'Incorrect parameters are entered. '
          f'Enter your hours of work, rate and bonus as parameters.')