# The biggest number on the list

list = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]

max = 0

for number in list:
    if number > max:
        max = number

print(f'The biggest number is: {max}')
