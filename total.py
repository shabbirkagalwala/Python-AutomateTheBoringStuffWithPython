total = 0
for i in range(101):
	total = i + total
print(str(total) + ' is the total of the first 100 numbers using for loop')
print('')

total = 0
i = 0
while i < 101:
	total = i + total
	i = i + 1
print(str(total) + ' is the total of the first 100 numbers using while loop')
print('')

print('Enter your name: ')
name = input()
print('')
x = 1
while x < 6:
	print('Your name is ' + name +  '(' + str(x) + ')')
	x = x + 1
print('We just printed your name 5 times using while loop')
print('')

for y in range(5):
	print('Your name is ' + name +  '(' + str(y) + ')')
	y = y + 1
print('We just printed your name 5 times using for loop')
print('')

for y in range(5,0,-1):
	print('Your name is ' + name +  '(' + str(y) + ')')
	y = y + 1
print('We just printed your name 5 times using for loop and range() arguments')
print('')