from random import randint
'''
www.csanimated.com/animation.php?t=Quicksort
'''


def sort(A, use_insertion=True):
    quicksort(A, 0, len(A)-1, use_insertion)


def quicksort(A, start_idx, end_idx, use_insertion):
    # list has 0 or 1 elements
    if start_idx >= end_idx:
        pass
    # if small list, use insertion_sort for speed
    elif use_insertion and end_idx - start_idx < 16:
        insertion_sort(A, start_idx, end_idx)
    # otherwise do quicksort
    else:
        p_idx = partition(A, start_idx, end_idx)
        quicksort(A, start_idx, p_idx - 1, use_insertion=use_insertion)
        quicksort(A, p_idx + 1, end_idx, use_insertion=use_insertion)


def partition(A, start_idx, end_idx):
        p_idx = randint(start_idx, end_idx)
        pivot = A[p_idx]
        swap(A, p_idx, end_idx)
        # values stored left of center_idx are less than pivot
        # values stored right of center_idx are greater than pivot
        center_idx = start_idx
        # search for values that are out of place
        for i in xrange(start_idx, end_idx):
            # swap values that are out of place to be left of
            # incremented center
            if A[i] <= pivot:
                swap(A, i, center_idx)
                center_idx += 1
        # put pivot in correct location
        swap(A, center_idx, end_idx)
        # return the new location of the pivot
        return center_idx


def swap(A, l_idx, r_idx):
    A[l_idx], A[r_idx] = A[r_idx], A[l_idx]


def insertion_sort(list, lo, hi):
    """
    performs insertion sort on list in place
    source: http://en.wikipedia.org/wiki/Insertion_sort
    """
    # print "doing insertion sort with lo={} and hi={}".format(lo, hi)
    for i in xrange(lo, hi + 1):
        x = list[i]
        j = i
        while j > 0 and list[j-1] > x:
            list[j] = list[j-1]
            j -= 1
        list[j] = x


if __name__ == '__main__':
    import sys
    import matplotlib.pyplot as plt
    import timeit
    repetitions = 100

    long_random_list_test = """
        l = [random.randint(-99999,99999) for i in xrange(0, 1000)]
        quick_sort.sort(l, use_insertion=False)
        """
    long_random_time = timeit.timeit(
        long_random_list_test,
        setup="import quick_sort, random",
        number=repetitions
    )
    print "1000 item random int list with {} repetitions takes time {} without" \
        "insertion sort helping".format(repetitions, long_random_time)

    long_random_list_test = """
        l = [random.randint(-99999,99999) for i in xrange(0, 1000)]
        quick_sort.sort(l)
        """
    long_random_time = timeit.timeit(
        long_random_list_test,
        setup="import quick_sort, random",
        number=repetitions
    )
    print "1000 item random int list with {} repetitions takes time {} with " \
        "insertion sort helping".format(repetitions, long_random_time)

    descend_case = """
        l = [i for i in xrange({}, 0, -1)]
        quick_sort.sort(l)
        """

    ascend_case = """
        l = [i for i in xrange(0, {})]
        quick_sort.sort(l)
        """

    descend_results = []
    ascend_results = []
    message = "{:.2%} of test list sizes done\r"
    min_list_size = 500
    max_list_size = 25000
    increment = 500
    for size in xrange(min_list_size, max_list_size+1, increment):
        descend_time = timeit.timeit(
            descend_case.format(size),
            setup="import quick_sort",
            number=repetitions
        )
        descend_results.append((size, descend_time))

        ascend_time = timeit.timeit(
            ascend_case.format(size),
            setup="import quick_sort",
            number=repetitions
        )
        ascend_results.append((size, ascend_time))
        sys.stdout.write(message.format(size / float(max_list_size)))
        sys.stdout.flush()

    plt.hold(True)
    for i in range(len(descend_results)):
        n_descend, time_descend = descend_results[i]
        n_ascend, time_ascend = ascend_results[i]
        plt.plot(n_descend, time_descend, 'bo')
        plt.plot(n_ascend, time_ascend, 'ro')
    plt.show()
