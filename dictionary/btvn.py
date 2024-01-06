register_account={}
while True :
    print('1.sign up')
    print('2.sign in')
    choice= int(input('lựa chon:'))
    if choice==1 :
        firstname = input('tên :')
        lastname = input('tên đệm')
        email = input('email:')
        password = input('pass:')
        register_account['firstname']= firstname
        register_account['lastname']= lastname
        register_account['email']= email
        register_account['password']= password
        print('đky thành công')
    