number_1 = [1, 2]
number_2 = [3, 4]
numbers= number_1+number_2
numbers.sort()
length= len(numbers)
index_median= length // 2 
median = (numbers[index_median] + numbers[index_median-1] )/2
print(median)

