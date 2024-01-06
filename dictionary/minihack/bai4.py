banggia = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400
}
maytinh = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
print(5*banggia["ASUS"])

a = input('hãng:')
b = int(input('số lượng:'))
print(b*banggia[a])
maytinh[a]= maytinh[a]-b
print('Available products:')
for key , value in maytinh.items():
    print('- '+ key + ' : '+ str(value) )