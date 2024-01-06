a = input('nhập chuỗi ký tự:')
def sokytu(a):
    chuoikytu = {}
    for i in a:
        if i in chuoikytu:
            chuoikytu[i] += 1
        else:
            chuoikytu[i] = 1
    return chuoikytu
print(sokytu(a))

# b= enumerate(a.split())
# c={}
# for i in b :
#     if 


