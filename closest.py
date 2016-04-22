# This is just to generate a sample.
import random
sample = random.sample(range(1000), 100)


def closest(array):
    """ Given 100 random integers, returns the two closest indexs
        (in position) with values that total 100.

        Inputs:
            array - Array of integers

        Returns:
            List - a list containing:
                   [distance between indexes, first index, second index]

        Time complexity:  O(n^2) (although the second loop diminishes
                                  over time)
        Space complexity: O(1)
    """

    results = []
    for index in range(0, len(array)):
        for sub_index in range(index + 1, len(array)):
            if array[index] + array[sub_index] == 100:
                distance = abs(index - sub_index)
                results.append([distance, index, sub_index])
    if len(results) == 0:
        print "No two integers add up to 100"
    else:
        first, second = sorted(results)[0][1], sorted(results)[0][2]
        print ("Index {} and {} are the two closest indexes "
               "with values that total 100").format(first, second)
        return sorted(results)[0]


# closest(sample)
