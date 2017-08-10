def divide(denominator):
		return numerator / int(denominator)
	

print('Enter Numerator:')
numerator = int(input())
print('Enter Denominator:')
try:
	print(divide(input()))
except ZeroDivisionError:
	print('Error: Invalid Argument.')
	
