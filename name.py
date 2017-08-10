import sys

name = '' 
print('You can exit this loop by typing "exit" any time')
while True:
	print('What is your name?')
	name = input()
	if name == 'exit':
		sys.exit()
	elif name == 'your name':
		i = 0
		while i < 4:
			i = i + 1
			print('')
			print('Enter your password ' + name)
			password = input()
			if password == 'Swordfish!':
				break
			elif password == 'exit':
				sys.exit()
			elif i == 3:
				print('Wrong password entered too many times! \n')
				break
			else:
				print('Wrong password')
				print('')
	else:
		print('That is not your name')
		print('')
		continue		
print('Access Granted!')