
import pytest
from solutions.solution_127 import binary_search

# Test cases for binary_search function

test_cases = [
    ([2, 5, 7, 8, 11, 12], 13, -1),  # Target not in array
    ([2, 5, 7, 8, 11, 12], 12, 5),  # Target at the end
    ([2, 5, 7, 8, 11, 12], 2, 0),  # Target at the beginning
    ([2, 5, 7, 8, 11, 12], 8, 3),  # Target in the middle
    ([2, 5, 7, 8, 11, 12], 7, 2),  # Target in the middle
    ([2, 5, 7, 8, 11, 12], 5, 1),  # Target in the middle
    ([], 5, -1),  # Empty array
    ([5], 5, 0),  # Array with one element
    ([5], 6, -1),  # Array with one element, target not found
    ([1, 2, 3, 4, 5, 6], 4, 3), # even length array
    ([1, 2, 3, 4, 5, 6], 7, -1), # even length array, target not present
    ([1, 2, 3, 4, 5], 3, 2), # odd length array
    ([1, 2, 3, 4, 5], 6, -1), # odd length array, target not present
    ([-5, -2, 0, 3, 5, 7], 0, 2), # array with negative and positive numbers
    ([-5, -2, 0, 3, 5, 7], -6, -1), # array with negative and positive numbers, target not present
    ([-5, -2, 0, 3, 5, 7], 7, 5), # array with negative and positive numbers, target at end
    ([-5, -2, 0, 3, 5, 7], -5, 0), # array with negative and positive numbers, target at beginning
    ([1,1,1,1,1,1], 1, 0), # array with duplicate elements
    ([1,1,1,1,1,1], 2, -1), # array with duplicate elements, target not present
    ([1,2,3,4,5,6,7,8,9,10], 5, 4), #larger array
    ([1,2,3,4,5,6,7,8,9,10], 11, -1), #larger array, target not present
    ([1,2,3,4,5,6,7,8,9,10], 1, 0), #larger array, target at beginning
    ([1,2,3,4,5,6,7,8,9,10], 10, 9), #larger array, target at end
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 5, 5), #reverse sorted array
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 11, -1), #reverse sorted array, target not present

]


@pytest.mark.parametrize("arr, target, expected", test_cases)
def test_binary_search(arr, target, expected):
    assert binary_search(arr, target) == expected


# Additional test cases to cover edge cases and boundary conditions.

test_cases_edge = [
    ([1, 2, 3, 4, 5], 0, -1),  #Target less than minimum
    ([1, 2, 3, 4, 5], 6, -1),  #Target greater than maximum
    ([-10,-5,0,5,10], -10, 0), #negative numbers
    ([-10,-5,0,5,10], 10, 4), #negative and positive numbers
    ([1,1,1,1,1,1,1,1,1,1],1,0), #all same element
    ([1,1,1,1,1,1,1,1,1,2],2,9), #mostly same element
    ([2,1,1,1,1,1,1,1,1,1], 2, 0), #mostly same element, target at start
    ([1,1,1,1,1,1,1,1,1,2], 3, -1), # mostly same element, target not present

    #Large arrays
    (list(range(1000)), 500, 500),
    (list(range(1000)), 1001, -1),
    (list(range(1000)), -1, -1),
    (list(range(1000)), 0, 0),
    (list(range(1000)), 999, 999),

    #more edge cases
    ([], 0, -1),
    ([0], 0, 0),
    ([0,1], 0, 0),
    ([0,1], 1, 1),
    ([0,1], 2, -1)

]


@pytest.mark.parametrize("arr, target, expected", test_cases_edge)
def test_binary_search_edge(arr, target, expected):
    assert binary_search(arr, target) == expected
