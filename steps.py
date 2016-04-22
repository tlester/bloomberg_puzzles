# Time Complexity = O(n^2)
# Space Complexity = O(1)

def steps(n):
    """ Recursively looks at every combination of 1 step and 2 steps up
        the ladder.   Adds the two combination for a total number of combos.

        Time complexity:  O(n^0)
        Space complexity: O(1)

        Args:
            n = Int, total number of steps
        Returns:
            Int, total combinations one can take to make it up the ladder
    """

    if n == 1:
        return 1
    if n == 2:
        return 2
    return steps(n-1) + steps(n-2)

# print steps(5)

