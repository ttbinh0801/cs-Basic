a= input()
def sokytu(a):
    daykitu={}
    for i in a :
        if i in daykitu:
            daykitu[i]=+ 1
        else :
            daykitu[i]=1
    return(daykitu)
print(sokytu(a))