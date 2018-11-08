def missing_number_from_1_to_100(arr):
    """ Running time: n """

    if len(arr)!=99:
        print('Invalid array size.')
        return -1
    
    sum = 0
    for num in arr:
        if num < 1 or num > 100:
            print('Some of the numbers do not fit the requirement')
            return -2
        sum += num
    
    return(100 - sum%4950)

def number_appears_twice(arr):
    """ Running time: n """

    # Assuming there are no numbers < 0 in arr
    numbers = {-1}
    for num in arr:
        if num in numbers:
            return num
        numbers.add(num)
    return -1

def is_possible(ransom_string, magazine_string):
    """ Running time: n + m """

    if len(magazine_string) < len(ransom_string):
        return False

    ransom_dict = {}

    for char in ransom_string:
        if char not in ransom_dict:
            ransom_dict[char] = 0
        ransom_dict[char] += 1

    for char in magazine_string:
        if char in ransom_dict:
            ransom_dict[char] -= 1
    
    for char in ransom_dict:
        if ransom_dict[char] > 0:
            return False
    return True
    

if __name__ == '__main__':
    
    # task 1
    # negative number means input values do not meet the requirements
    # missing number 67
    a = [i for i in range(1,67)]
    b = [i for i in range(68,101)]
    c = [i for i in range(1,101)]
    b.extend(a)
    print('Missing number -> %d'%(missing_number_from_1_to_100(b)))

    # task 2
    # negative number means input values do not meet the requirements
    a = [0, 1, 2, 5, 3, 4, 5]
    print('Repeating number -> %d'%(number_appears_twice(a)))

    # task 3
    rs_true = 'hello'
    ms_true = 'hieroglyphology'
    print('Should be true -> ' + str(is_possible(rs_true, ms_true)))

    rs_false = 'hello'
    ms_false = 'brainstorm'
    print('Should be false -> ' + str(is_possible(rs_false, ms_false)))
