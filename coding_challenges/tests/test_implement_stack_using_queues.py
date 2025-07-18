
import pytest
from solutions.solution_147 import MyStack

@pytest.fixture
def my_stack():
    return MyStack()

# Test cases for push and pop operations
def test_push_pop_1(my_stack):
    my_stack.push(1)
    assert my_stack.pop() == 1

def test_push_pop_2(my_stack):
    my_stack.push(10)
    my_stack.push(20)
    assert my_stack.pop() == 20
    assert my_stack.pop() == 10

def test_push_pop_3(my_stack):
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    assert my_stack.pop() == 3
    assert my_stack.pop() == 2
    assert my_stack.pop() == 1


# Test cases for multiple pushes and pops with different values
def test_multiple_push_pop_1(my_stack):
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)
    my_stack.push(5)
    assert my_stack.pop() == 5
    assert my_stack.pop() == 4
    assert my_stack.pop() == 3

def test_multiple_push_pop_2(my_stack):
    my_stack.push(-1)
    my_stack.push(0)
    my_stack.push(1)
    my_stack.push(100)
    my_stack.push(-100)
    assert my_stack.pop() == -100
    assert my_stack.pop() == 100
    assert my_stack.pop() == 1


# Test cases for empty stack
def test_empty_stack(my_stack):
    assert my_stack.empty() == True

def test_empty_stack_after_pop(my_stack):
    my_stack.push(1)
    my_stack.pop()
    assert my_stack.empty() == True

# Test cases for top operation
def test_top_1(my_stack):
    my_stack.push(1)
    assert my_stack.top() == 1

def test_top_2(my_stack):
    my_stack.push(10)
    my_stack.push(20)
    assert my_stack.top() == 20
    my_stack.pop()
    assert my_stack.top() == 10

def test_top_empty(my_stack):
    with pytest.raises(IndexError):
        my_stack.top()

# Test cases with mixed operations
def test_mixed_operations_1(my_stack):
    my_stack.push(1)
    my_stack.push(2)
    assert my_stack.top() == 2
    my_stack.pop()
    my_stack.push(3)
    assert my_stack.top() == 3
    assert my_stack.pop() == 3
    assert my_stack.pop() == 1
    assert my_stack.empty() == True

def test_mixed_operations_2(my_stack):
    for i in range(1,11):
        my_stack.push(i)
    for i in range(10,0,-1):
        assert my_stack.top() == i
        my_stack.pop()
    assert my_stack.empty() == True

#Test cases with large number of elements.
def test_large_number_of_elements(my_stack):
    for i in range(1000):
        my_stack.push(i)
    for i in range(999,-1,-1):
        assert my_stack.pop() == i

#Edge cases
def test_zero(my_stack):
    my_stack.push(0)
    assert my_stack.pop() == 0

def test_negative_numbers(my_stack):
    my_stack.push(-1)
    my_stack.push(-10)
    assert my_stack.pop() == -10
    assert my_stack.pop() == -1


#Adding more test cases for robustness.
#These tests cover various scenarios including edge cases and large inputs.

for i in range(20): # 20 more tests with random inputs
    test_num = i
    test_list = [test_num + j for j in range(10)]  # Create a list of 10 numbers

    def test_random_push_pop(my_stack,test_list=test_list):
        for num in test_list:
            my_stack.push(num)
        for num in reversed(test_list):
            assert my_stack.pop() == num


    exec(f"def test_random_push_pop_{i}(my_stack): test_random_push_pop(my_stack)")
