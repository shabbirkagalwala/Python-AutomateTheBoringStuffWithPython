import random

def MagicBall(answer):
	if answer == 1:
		return 'It is certain'
	elif answer == 2:
		return 'It is decidedly so'
	elif answer == 3:
		return 'Yes'
	elif answer == 4:
		return 'Reply hazy try again'
	elif answer == 5:
		return 'Try again later'
	elif answer == 6:
		return 'Concentrate and ask again'
	elif answer == 7:
		return 'My reply is no'
	elif answer == 8:
		return 'Outlook not so good'
	elif answer == 9:
		return 'Very Doubtful'

print(MagicBall(random.randint(1,9)))