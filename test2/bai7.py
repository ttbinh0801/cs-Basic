a = int(input('input a month:'))
if ( a>7 and a%2==0 ) or ( a<7 and a%2!=0):
    print ('this month has 31 days')
elif ( a==2 ):
    print ('this month has 28 or 29 days')  
else :
    print ('this month has 30 days')  
