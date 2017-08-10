WeekDays = []

while len(WeekDays) < 7:
    print('Enter Week Day ' + str(len(WeekDays) + 1) + ' OR enter exit to quit:')
    
    name = input()
    if name == 'exit':
        break
    #This is one way of adding/concat to list
    #WeekDays = WeekDays + [name] 
    
    if WeekDays == []:
    	WeekDays.insert(0,name)
    else:
    	WeekDays.append(name)
    
print('The weekdays are:')
for name in range(len(WeekDays)):
    print('Weekday ' + str(name + 1) + ' is '+ str(WeekDays[name]) )