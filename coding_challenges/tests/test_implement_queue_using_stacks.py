
import pytest
from solutions.solution_146 import MyQueue

@pytest.fixture
def my_queue():
    return MyQueue()

# Test cases with various numbers of push and pop operations

def test_empty_queue(my_queue):
    assert my_queue.empty() == True

def test_push_one(my_queue):
    my_queue.push(1)
    assert my_queue.empty() == False
    assert my_queue.peek() == 1

def test_push_multiple(my_queue):
    my_queue.push(1)
    my_queue.push(2)
    my_queue.push(3)
    assert my_queue.peek() == 1

def test_pop_one(my_queue):
    my_queue.push(1)
    assert my_queue.pop() == 1
    assert my_queue.empty() == True

def test_pop_multiple(my_queue):
    my_queue.push(1)
    my_queue.push(2)
    my_queue.push(3)
    assert my_queue.pop() == 1
    assert my_queue.pop() == 2
    assert my_queue.pop() == 3
    assert my_queue.empty() == True

def test_peek_empty(my_queue):
    with pytest.raises(Exception):
        my_queue.peek()

def test_pop_empty(my_queue):
    with pytest.raises(Exception):
        my_queue.pop()


# Test cases with different data types

def test_push_string(my_queue):
    my_queue.push("hello")
    assert my_queue.peek() == "hello"

def test_push_boolean(my_queue):
    my_queue.push(True)
    assert my_queue.peek() == True

def test_push_float(my_queue):
    my_queue.push(3.14)
    assert my_queue.peek() == 3.14

def test_push_mixed_types(my_queue):
    my_queue.push(1)
    my_queue.push("hello")
    my_queue.push(True)
    assert my_queue.pop() == 1
    assert my_queue.pop() == "hello"
    assert my_queue.pop() == True


# Test cases with edge cases and large inputs

def test_large_input(my_queue):
    for i in range(1000):
        my_queue.push(i)
    for i in range(1000):
        assert my_queue.pop() == i

def test_push_pop_interleaved(my_queue):
    for i in range(100):
        my_queue.push(i)
        if i % 2 == 0:
            assert my_queue.pop() == i -1 if i > 0 else 0


def test_empty_after_many_operations(my_queue):
    for i in range(100):
        my_queue.push(i)
        my_queue.pop()
    assert my_queue.empty() == True

def test_push_null(my_queue):
    my_queue.push(None)
    assert my_queue.pop() is None


#More test cases to cover various scenarios (30 more cases)

for i in range(30):
    test_name = f"test_scenario_{i+1}"
    test_data = []
    num_ops = i % 10 + 1 # Varying number of operations
    for j in range(num_ops):
        op = j % 2 # 0: push, 1: pop
        val = j if op == 0 else None
        test_data.append((op, val))


    def test_function(my_queue):
        queue_data = []
        for op, val in test_data:
            if op == 0:
                my_queue.push(val)
                queue_data.append(val)
            else:
                if not queue_data:
                    with pytest.raises(Exception):
                        my_queue.pop()
                else:
                    assert my_queue.pop() == queue_data.pop(0)

    exec(f"def {test_name}(my_queue): test_function(my_queue)")
    globals()[test_name] = test_function
