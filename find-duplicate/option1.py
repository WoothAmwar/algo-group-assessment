# OPTION 1 - FIND DUPLICATE
# DO NOT SHARE

from typing import List
# unittest used for unit testing, not in the findDuplicate function
import unittest


# Implement a function to identify a duplicate integer in an unsorted array
# of integers. Talk about time/space complexity for each method you implement.

# `input` contains exactly N+1 numbers
# `input` elements are integers in the domain [1, N]
# `input` contains all integers in the domain [1, N] at least once
# `findDuplicate` returns an `int`: the duplicate integer
def findDuplicate(input: List[int]) -> int:
    """
    Description of my two solutions.

    
    Method 1 has a time complexity of O(N^2) as it traverses the list  at most N times, thus N^2, and space complexity
      of O(1) since it doesn't use any data structures aside from the input list.
    Method 2 has a time complexity of O(N) as it only traverses the list once and searching within a set has a time 
      complexity of O(1) as it behaves like a hashmap. This method has a space complexity of O(N) as it implements a set
      to save every value the algorithm looks at, which can be at most N items, thus O(N).
    """
    # METHOD 1 - O(N^2) time complexity, O(1) space complexity
    for curr_num_idx in range(len(input)):
        for all_other_num_idx in range(curr_num_idx+1, len(input)):
            if input[curr_num_idx] == input[all_other_num_idx]:
                return input[curr_num_idx]
    # METHOD 2 - O(N) time complexity, O(N) space complexity
    found_num = set()
    for curr_num in input:
        if curr_num in found_num:
            return curr_num
        found_num.add(curr_num)
    return -1


class TestClass(unittest.TestCase):
    """
    Used for testing the findDuplicate function
    """
    def test_unsorted(self):
        input_list = [10,2,3,7,8,71,39,6,1,5, 1]
        duplicate_num = findDuplicate(input_list)    
        self.assertEqual(duplicate_num, 1, "Unsorted Duplicate function does not work")
    def test_sorted(self):
        input_list = [0,1,2,3,4,5,6,7,8,9,10, 5]
        duplicate_num = findDuplicate(input_list)    
        self.assertEqual(duplicate_num, 5, "Sorted Duplicate function does not work")


def main():
    sorted_input_list = [0,1,2,3,4,5,6,7,8,9,10, 5]
    unsorted_input_list = [10,2,3,7,8,71,39,6,1,5, 1]
    print("Should be 5:", findDuplicate(sorted_input_list))
    print("Should be 1:", findDuplicate(unsorted_input_list))


if __name__ == "__main__":
    # main() should be called to see print statements in terminal
    # unittest.main() should be called to see the results of the unit tests, which was what was provided in the repo
    # main()
    unittest.main()
