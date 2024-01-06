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
print('Total value of available brands:')
tonggia= {
}
for a in banggia.keys():
    tonggia[a]= banggia[a]*maytinh[a]
for key , value in tonggia.items():
    print('- ' + key + ' : ' + str(value) )
d=sum(tonggia.values())
print(d)


