banggia={
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400
}
print(max(banggia.values()))
print(min(banggia.values()))

a = input()
if ((a in banggia.keys()) == True):
    print(banggia[a])
else:
    print('không có sản phẩm')



        
    