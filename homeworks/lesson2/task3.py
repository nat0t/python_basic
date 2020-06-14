def get_season1(month):
    months = ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
    seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
    print(f"It's {seasons[months.index(month) // 3]} (with list).")

def get_season2(month):
    seasons = {'Winter': ('12', '1', '2'),
               'Spring': ('3', '4', '5'),
               'Summer': ('6', '7', '8'),
               'Autumn': ('9', '10', '11')
               }
    for key in seasons.keys():
        if month in seasons[key]:
            print(f"It's {key} (with dictionary).")
            break

months = ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
while True:
    month = input('Enter number of month: ')
    if month not in months:
        print('Entered incorrect month.')
        continue
    get_season1(month)
    get_season2(month)
    break