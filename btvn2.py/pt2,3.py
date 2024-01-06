# def heso(a,b,c):
#     import math
#     delta= b**2-4*a*c 
#     if delta >0 :
#         x1= (-b+math.sqrt(delta))/2*a
#         x2= (-b-math.sqrt(delta))/2*a
#         print(f'x1= {x1}, x2= {x2}')
#     if delta == 0 :
#         x= -b/2*a
#         print(f'x= {x}')
#     if delta <0 :
#         print ('không tồn tại nghiệm thoả mãn')
# heso(-3,54,67)


def heso(a,b,c,d):
    import math
    delta = b**2-3*a*c
    k =(9*a*b*c-2*b**3-27*a**2*d)/2*(math.sqrt(abs(delta)**3))
    if delta >0:
        if abs(k) >1:
            x = ((math.sqrt(delta)*abs(k))/3*a*k)*((abs(k)+math.sqrt(k**2-1))**1/3)+((abs(k)-math.sqrt(k**2-1))**1/3)-b/3*a
            print(f'x= {x}')
        else :
            x1= (2*math.sqrt(delta)*math.cos(math.acos(k)/3)-b)*3*a
            x2 = (2*math.sqrt(delta)*math.cos((math.acos(k)/3)-math.pi*(2/3))-b)*3*a
            x3 = (2*math.sqrt(delta)*math.cos((math.acos(k)/3)+math.pi*(2/3))-b)*3*a
            print(f'x1= {x1}, x2= {x2}, x3={x3}')
    if delta == 0:
        x= (-b+(b**3-27*a**2*d)**1/3)/3*a
        print(f'x= {x}')
    if delta <0:
        x = (math.sqrt(abs(delta))/3*a)*((k+math.sqrt(k**2+1))**1/3)+((k-math.sqrt(k**2+1))**1/3)-b/3*a
        print(f'x= {x}')
heso(1,-6,11,-6)

import math
g= math.cos(math.degrees(math.pi/3))
print (g)