number = 23
running = True

while running :
    guess = int(raw_input('enter an integer'))
    
    if guess == 1 :
        continue
    
    if guess == number :
        print 'equal'
    elif guess < number :
        print 'less'
    else :
        print 'greater'
        
    if guess == 0 :
        break
else :
    print 'the while loop is over'
   
        
        
print 'while loop over'