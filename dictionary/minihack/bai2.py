maytinh = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
maytinh["TOSHIBA"]=10
print(maytinh)

a=input('hãng:')
b=input('số lượng:')
maytinh[a]=b 
print(maytinh)

maytinh['MACBOOK']=60
maytinh['DELL']=2
print(maytinh)

a= maytinh['ASUS']+ maytinh['DELL']+maytinh['HP']+maytinh['MACBOOK']
print(a)
