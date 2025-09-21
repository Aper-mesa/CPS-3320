print('Enter positive numbers, and enter a negative number to stop: ')
number = 0
while True:
    if (temp := int(input())) < 0:
        break
    number += temp
print(number)
