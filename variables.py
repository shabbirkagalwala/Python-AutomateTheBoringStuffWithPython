def spam():
	global email 						#tells python we are using the global variable email
	email = 'Change Global Variable' 	#assigns value to the empty global variable
	junk() 								#calls the junk functions
	print(email)

def junk():
	email = 'This is junk local variable' #this is local to this function
	print(email)
	
email = '' 								#global variable is empty
spam()
print(email)
