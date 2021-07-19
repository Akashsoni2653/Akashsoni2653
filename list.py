list_1 =[1,2,3,4,2,6,3,5,4,1,5,9,8,5,5,6,6,4,1,2]
list_1.sort()
print(list_1)
list_2 = list_1.copy()
list_2.reverse()
print(list_2)
print("###################################################")
#code to remove duplicates from the list
original_number = []
for numbers in list_1:
    if numbers not in original_number:
        original_number.append(numbers)
print(original_number)
