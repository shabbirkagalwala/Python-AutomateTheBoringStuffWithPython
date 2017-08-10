import random

number = random.randint(1,10)
print('I am thinking of a number between 1 and 20')

for i in range(1,7): #take a guess in 6 chances
	print('Take a guess')
	no = int(input())
	
	if no < number:
		print('Your guess is too low')
	elif no > number:
		print('Your guess is too high')
	else:
		break

if i == number:
	print('You guessed it right in ' + str(i) + ' guesses')
else:
	print('Nope, The number I was thinking of was ' + str(number))
		