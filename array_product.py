def array_of_products(array):
    """ Creates a new array equal to the length of the input array where each
        index is the product of all the other indexes.

        Inputs:
            array - array of integers

        Returns:
            array - an array of integers

        Time complexity = O(n^2)
        Space complexity = O(1)
    """

    new_array = []  # Create a placeholder for the new array.

    # count through each index
    for i in range(0,len(array)):
        hold = array.pop(0)  # pull out the first index

        total = 1  # This variable will hold the total of the product

        # Loop through each of the remaining indexs and get their product
        for element in array:
            total = total * element

        # Add the product to the new array
        new_array.append(total)

        # Put the first index back at the end of the original array
        array.append(hold)

    return new_array


