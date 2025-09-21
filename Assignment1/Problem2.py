speed = int(input('Enter the speed of car: '))
hour = int(input('Enter the hour of car: '))
print('Hour\t\tDistance Traveled')
for i in range(hour):
    print(str(i + 1) + "\t\t\t" + str((i + 1) * speed))
