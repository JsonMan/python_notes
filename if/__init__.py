number = 23
guess = int(raw_input('enter an integer'))

if guess == number :
    print 'guess == number'
elif guess < number :
    print 'guess < number'
else :
    print ' guess > number'


print 'guess = ', guess ,' number = ', number, 'done if'



if True :
    print 'yes ,it is true'
    
if False :
    print ' never print'
else :
    print ' print here'