"""Given an array of integers, find the first missing positive integer,
in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def firstMissingPositiveInteger(arr):
    """ Given array of integers returns first missing positive integer.
        -- in case of error returns 1
        - given no positive integers in array returns 1
        - given [1,2,3,4] returns 5
        - given [4, 8, 9, 15, 22] returns 1
    """
    missing_value = 1
    try:
        for i in range(len(arr)):
            if arr[i] > 0:
                if arr[i] == missing_value:
                    missing_value += 1
    
    except IndexError as err:
        print('IndexError --> {0}'.format(err))
        raise
    except ValueError as err:
        print('ValueError --> {0}'.format(err))
        raise

    finally:
        return missing_value
    


    
