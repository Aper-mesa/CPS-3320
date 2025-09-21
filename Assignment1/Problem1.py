number = int(input('Enter a number between 1 and 7:'))
if number < 1 or number > 7:
    print('Invalid input')
    exit()
match number:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    case 7:
        print('Sunday')
