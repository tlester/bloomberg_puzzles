# Determine the square root of a number

# The easy way:

def square_easy(n):
    """ Simply use the sqrt method from the math module to calculate
        the square root of a number.

        Args:
            n - Int or float, the number we will try to find the square
            root of.

        Returns:
            float - The sqare root of n.

        Time & Space complexity.  Not sure...
    """

    import math

    return math.sqrt(n)


# The harder way:

def square_hard(n):
    """ Find the square root of a number using a binary search'ish approach.

        Inputs:
            n - Float or Int.

        Returns:
            Square root of n

        Time complexity = O(log n)
        Space complexity = O(1)
    """

    if n == 0:
        return 0
    if n == 1:
        return 1

    first = 0
    last = n

    while first <= last:
        middle = (first + last) / 2.0
        close = ((middle*middle)/n)

        # Just in case we nail it
        if middle * middle == n:
            return middle

        # Check to see if we are nearly matched
        if abs(1-close) < .00000000000005:  # Should get us close enough!
            return middle

        # if the answer is in the bottom half
        elif middle * middle > n:
            last = middle

        # if the answer is in the top half
        else:
            first = middle

