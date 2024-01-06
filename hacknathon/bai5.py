bangia={
    'Iphone12': 28000000,
    'Samsung N10':16000000,
    'Oppo 93': 7500000,
    'Vsmart': 7400000,
    'Vivo': 4200000
}
def dt(tenhang):
    print(bangia[tenhang])
def tien(so):
    print('phone that can fit your budget:')
    for key,value in bangia.items():
        if so >= value :
            print(f'-{key} : {value}')
dt('Vivo')
tien(23814317403434)
