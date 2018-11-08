"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def addToK(arr, k):
    l = len(arr)
    for num1 in arr[:l-1]:
        for num2 in arr[1:]:
            if num1 + num2 == k:
                return("%d + %d  = %d"%(num1, num2, k))
    return('No two numbers add up to %d'%(k))


def addToK_onePass(arr, k):
    # Create a set and populate it with vales k - arr[i]. if arr[i] in set return values
    s = {1}
    s.pop()

    for num in arr:
        if num in s:
            return("%d + %d  = %d"%(k - num, num, k))
        s.add(k-num)
    return('No two numbers add up to %d'%(k))


if __name__ == '__main__':
    arr = [10, 14, 3, 17]
    k = 17
    result = addToK_onePass(arr, k)
    print(result)