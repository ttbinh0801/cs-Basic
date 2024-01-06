# Hãy viết một chương trình Python để kiểm tra xem một số nguyên x có phải là số nguyên tố không?
n=  int(input('nhập n:'))
f = 2
import math
while f <= math.sqrt(n) :
    if n % f == 0 :
        print (' n không là số nt')
        break
    f+= 1 
if f > math.sqrt(n) :
    print ('n là số nt')


     

        
