#bool numExists( int array[], int array_len, int num )


def numExists(array, num):
    """ Checks to see if a number esists in a sorted array.

        Inputs:
            array - A sorted array of numbers

        Returns:
            Boolean - True if number exists

        Time complexity:  O(log n)
        Space complexity: O(1)
    """

    # Set up variables for binary search
    first = 0
    last = len(array) - 1
    found = False

    # Execute binary search
    while first <= last and found is False:
        guess = (first + last) // 2

        # Set found to True if we find the number
        if array[guess] == num:
            found = True

        # Otherwise narrow the search
        elif num < array[guess]:
            last = guess - 1
        else:
            first = guess + 1

    return found
