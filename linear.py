# linear search
arr=[1,13,56,89,34,56,89,45,67,45,23,56]
def linearsearch(arr,ele):
    for index,value in enumerate(arr):
        if ele==value:
            return index +1
    return -1   

output=linearsearch(arr,43)
print(output)

output=linearsearch(arr,56)
print(output)



