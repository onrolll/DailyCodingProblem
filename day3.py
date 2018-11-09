from functools import reduce
"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division? 
"""

def valuesMultipliedAtI(arr):
    return_arr = []
    # n calls to _valueAtI with n-1 multiplications each --> O(n^2) running time
    # space complexity --> O(n)
    # auxilliary space --> O(1)
    for i in range(len(arr)):
        return_arr.append(_valueAtI(arr, i))
    return return_arr
    

def _valueAtI(arr, i):
    result = 1
    for j in range(i): result *= arr[j]
    for k in range(i+1, len(arr)): result *=arr[k]
    return result

def withDivision(arr):
    # running time --> O(n)
    # space complexity --> O(n)
    # auxilliary space --> O(1)
    multiplier = lambda x,y: x * y
    multiplied_arr = reduce(multiplier, arr) # n calls to * 
    return_arr = []
    for num in arr: # n calls to /
        return_arr.append(int(multiplied_arr / num))
    return return_arr

def improvedWithoutDivision(arr):
    # running time --> O(n)
    # space complexity --> O(n)
    # auxilliary space --> O(1)

    product = [1 for i in range(len(arr))]

    temp = 1
    # product for values to the left of i
    for i in range(len(arr)):
        product[i] = temp 
        temp *= arr[i]

    temp = 1 # reset temp for product on the right
    # product for values to the right of i
    for i in range(len(arr) -1, -1, -1):
        product[i] *= temp
        temp *= arr[i]

    return product

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    arr = improvedWithoutDivision(arr)
    print(arr)

    