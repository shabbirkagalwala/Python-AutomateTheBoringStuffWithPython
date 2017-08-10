print('Please enter your username:')
name = input()
if name == ('user1' or 'user2'):
	print('Please enter your password ' + name)
	password = input()
	if password == 'xyz':
		print('Access Granted')
	elif password == 'abc':
		print('Access Granted')
else:
	print('User not found!')
