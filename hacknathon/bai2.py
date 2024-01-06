def heso(a,b,c):
    import math
    if a == 0 :
        if b != 0 :
            x = -c/b 
            print(f'x= {x}')
        else :
            print('pt co vo so no')
    else :
        delta = b**2-4*a*c
        if delta >0 :
            x1= (-b+math.sqrt(delta))/2*a
            x2= (-b-math.sqrt(delta))/2*a
            print(f'x1= {x1}, x2= {x2}')
        if delta == 0 :
            x= -b/2*a
            print(f'x= {x}')
        if delta <0 :
            print ('không tồn tại nghiệm thoả mãn')
heso(0,2,1)