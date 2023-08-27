

def range_sort_points_by_axis(pointlist, k, lower, upper):
    if upper - lower <= 32:
        insertion_sort_by_axis(pointlist, k)
    else:
        mid = ((upper - lower) // 2) + lower

        range_sort_points_by_axis(pointlist, k, lower, mid)
        range_sort_points_by_axis(pointlist, k, mid, upper)

        tmp = merge_by_axis(pointlist, k, lower, mid, upper)

        for i in range(len(tmp)):
            pointlist[lower + i] = tmp[i]

def insertion_sort_by_axis(array, k):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1][k] > array[j][k]:
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1

def merge_by_axis(array, k, lower, mid, upper):
    tmp = []

    i = lower
    j = mid

    while i < mid and j < upper:
        if array[i][k] <= array[j][k]:
            tmp.append(array[i])
            i += 1
        elif array[j][k] < array[i][k]:
            tmp.append(array[j])
            j += 1

    if i == mid:
        while j < upper:
            tmp.append(array[j])
            j += 1
    else:
        while i < mid:
            tmp.append(array[i])
            i += 1

    return tmp

def range_timsort(array, lower, upper):
    # mutates the given array
    if upper - lower <= 32:
        insertion_sort(array)
    else:
        mid = ((upper - lower) // 2) + lower

        range_timsort(array, lower, mid)
        range_timsort(array, mid, upper)

        tmp = merge_arrays(array, lower, mid, upper)

        for i in range(len(tmp)):
            array[lower + i] = tmp[i]


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1


def merge_sort(array):
    merge_sort_aux(array, 0, len(array))

def merge_sort_aux(array, lower, upper):
    # lower is inclusive, upper is exclusive

    # base case -> do nothing and return
    # recursive case
    if upper > lower + 1:
        mid = ((upper - lower) // 2) + lower

        merge_sort_aux(array, lower, mid)  # array mutated in child functions
        merge_sort_aux(array, mid, upper)

        tmp = merge_arrays(array, lower, mid, upper)

        for i in range(len(tmp)):
            array[lower+i] = tmp[i]



def merge_arrays(array, lower, mid, upper):
    # seaprated elements in array
    # put new elements in tmp
    tmp = []

    i = lower
    j = mid

    while i < mid and j < upper:
        if array[i] <= array[j]:
            tmp.append(array[i])
            i += 1
        elif array[j] < array[i]:
            tmp.append(array[j])
            j += 1

    if i == mid:
        while j < upper:
            tmp.append(array[j])
            j += 1
    else:
        while i < mid:
            tmp.append(array[i])
            i += 1

    return tmp

lst = [5, 9, 3, 4]
lst2 = [0, 2, 0, 9]
lst3 = [6, 5, 8, 3, 4, 8, 9, 3, 4]



# print(merge_arrays(lst2, 0, 2, len(lst)))
# merge_sort(lst)
# range_timsort(lst3, 0, len(lst3))
# print(lst3)