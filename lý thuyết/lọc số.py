
def tích(list_items):
    list_numbers=[]
    for k in list_items :
        if isinstance(k, int ):
            list_numbers.append(k)
    if 0 in list_numbers  :
        return 0
    else:
        u=1
        for i in list_numbers:
            u*=i
        return u
a= tích([0,1,2,3,'a'])
print(a)



    
    
        
        


