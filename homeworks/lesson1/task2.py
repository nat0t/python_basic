def get_time1(time_):
    minutes, seconds = divmod(int(time_), 60)
    hours, minutes = divmod(minutes, 60)
    print(f'You entered {hours:<02}:{minutes:<02}:{seconds:<02}')

def get_time2(time_):
    # Format "d days, hh:mm:ss"
    import datetime
    time_in_sec = str(datetime.timedelta(seconds=int(time_)))
    print(f'Entered time (module datetime used): {time_in_sec}')

while True:
    time_ = input('Please input time in seconds: ')
    # Without processing float type
    if not time_.isdigit():
        print('Entered time is incorrect.')
        continue
    get_time1(time_)
    get_time2(time_)
    break