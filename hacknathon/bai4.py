list_monan = []
while True :
    a= input ('please choose a dish:')
    if a not in list_monan:
        list_monan.append(a)
        print('great choice , anything else'.capitalize())
    else:
        print('you choose this already'.capitalize())
    b=input('great choice , anything else:')
    if b == 'n':
        print('well done , your order : ')
        for i in list_monan:
            print(f'-{i}')
        break


        
    
    