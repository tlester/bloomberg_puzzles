/*  Recursively looks at every combination of 1 step and 2 steps up
        the ladder.   Adds the two combination for a total number of combos.

        Time complexity:  O(n^0)
        Space complexity: O(1)

        Args:
            n = Int, total number of steps
        Returns:
            Int, total combinations one can take to make it up the ladder
*/

function steps(n) {
    if (n === 1) {
        return 1;
    } else if (n === 2) {
        return 2;
    }
    return steps(n-1) + steps(n-2);
};


// console.log(steps(5));
