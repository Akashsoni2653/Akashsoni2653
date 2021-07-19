matrix = [
    [1,2,3,],
    [4,5,6,],
    [7,8,9,],
]
#inserting
matrix[0].insert(0,200)
for rows in matrix:
    for items in rows:
        print(items)
#changing value
print("changing value")
matrix[0][2]=25
print(matrix[0][2])
# clearing the list
matrix[0].clear()
for rows in matrix:
    for items in rows:
        print(items)
#removing am item from the end of a list
matrix[1].pop()
for rows in matrix:
    for items in rows:
        print(items)
# checking for the existance of an item in a list
print("3 in matrix")
