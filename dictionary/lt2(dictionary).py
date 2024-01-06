register= {
    "first name":"bình",
    "last name":"trần thanh",
    'email': "binh@gmail.com",
    "password":"123"
}
# for key in register.keys() :
#     print(key)
# for value in register.values():
#     print(value)
# for items in register.items():
#     print(items)
# print(register["password"])
# register['password']='456'
# print(register)
# in hết các key trong 1 dict : print(register.key()

languages= {
    'c++':200,
    'python':390,
    'java':589,
    'javascript':590,
}
a=languages.values()
max_values = max(a)
for key, value in languages.items():
    if value == max_values:
        print(key)


save_money= 400
laptop ={
    'dell laptop':200,
    'macbook air laptop':589,
    'iphone 8':390,
    'lenovo laptop':590,
    "samsung":99,
}
for key , value in laptop.items():
    if value <= save_money :
        print(key)




# Tuple()
students =('a','b','c','d')
print(students)
print(students[0])
# print(students.pop()) khong cho phép thay đổi giá trị
print(len(students))

# file handling , modules , functions , làm 6 bài 
