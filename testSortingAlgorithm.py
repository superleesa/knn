from Timsort import range_timsort
from random import randint

def t_range_timsort():
    test_array = []
    for _ in range(300):
        randnum = randint(0, 500)
        test_array.append(randnum)

    actual = sorted(test_array)
    range_timsort(test_array, 0, len(test_array))
    calculated = test_array

    if actual == calculated:
        return True
    else:
        return False

def test_sort(num):
    for _ in range(num):
        print(t_range_timsort())

# print(t_range_timsort())
test_sort(100)
