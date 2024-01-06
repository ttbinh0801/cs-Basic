# Cho một danh sách values = [10, 20, 30, 40, 50] và một số nguyên target. Hãy kiểm tra xem target có tồn tại trong danh sách values không, và in ra kết quả .  
values = [10, 20, 30, 40, 50]
target = int(input('nhập số:'))
if target in values:
    print(target,'tồn tại trong danh sách')
else: 
    print('danh sách k tồn tại',target)