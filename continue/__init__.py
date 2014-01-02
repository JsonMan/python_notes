while True :
    s = raw_input('enter something') 
    
    if s == 'quit' :
        break
    if len(s) < 3 :
        continue
    
    print 'input is of sufficient length'
    