a = input().split(",")

a = [int(i) for i in a]

def factors(x):
    b = []
    for i in range(1,x):
        if x % i == 0:
            b.append(i)
    if len(b) ==3:
      return True
    else:
      return False
c=[]
    
for i in a:
    if factors(i)==True:
        c.append(i)
        
print(sum(c))