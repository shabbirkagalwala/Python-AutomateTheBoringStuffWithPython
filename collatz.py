import sys

number = input('Enter a number :')

try:
    number = int(number)
except:
    sys.exit('Enter an integer only')
    

def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1
    print(int(number))
        
while number != 1:
   number = collatz(number)
   print(number)