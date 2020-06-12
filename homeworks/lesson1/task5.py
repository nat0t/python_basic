while True:
    revenue = input('Enter revenue please: ')
    costs = input('Enter costs please: ')
    # Without float values
    if not revenue.isdigit() or not costs.isdigit():
        print('You entered not incorrect amount of money.')
        continue
    margin = int(revenue) - int(costs)
    if margin < 0:
        print('Your company is unprofitable.')
    elif margin == 0:
        print('Your company is not profitable.')
    else:
        print('Your company is profitable.')
        rentability = (margin / int(revenue)) * 100
        print(f"Your company's rentability is {rentability:.2f}%")
        while True:
            num_worker = input('Enter the number of employees in your company: ')
            if not num_worker.isdigit():
                print('Entered number is incorrect.')
                continue
            margin_per_person = margin / int(num_worker)
            print(f'Margin per person in your company is {margin_per_person:.2f}')
            break
    break