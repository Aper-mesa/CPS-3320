import random

print('how many numbers you want?')
count = int(input())
with open('random_numbers.txt', 'w') as f:
    for i in range(count):
        f.write(str(random.randint(1, 500)) + '\n')
print('file has been created')
