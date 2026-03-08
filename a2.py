def Odd_Occuring_number(arr):
    res = 0 

    for element in arr:
        res = res ^ element

    return res

arr = []

n = int(input('Enter number of elements: '))

while(n):
    element = int(input('Enter element: '))
    arr.append(element)
    n = n-1

print('\n The odd occuring number is: ', Odd_Occuring_number(arr))