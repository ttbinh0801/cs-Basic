def dãy(a,b,c):
    list_num=[a,b,c]
    list_num.sort(reverse=True)
    print(list_num[0])
dãy(7,5,6) 

# cách 2:
def max(a,b,c):
    maxnum=a 
    if b > maxnum:
        maxnum=b
    elif c > maxnum:
        maxnum=c 
    return maxnum
print (max(4,8,5))
    
    