import random

print('Who will pay the bill?')

friends = ['Kauan', 'Guilherme', 'Nicolas', 'Pablo', 'Livia']

#1
who_pay = random.randint(0, 4)
print(friends[who_pay])

#2nd
print(random.choice(friends))