from random import randint
'''
www.csanimated.com/animation.php?2t=Quicksort
'''


def sort(A):
    quicksort(A, 0, len(A)-1)


def quicksort(A, lo, hi):
    # if small list, use insertion_sort for speed
    if hi - lo < 16:
        insertion_sort(A, lo, hi)
    # 2 item list
    elif hi-lo == 1:
        if A[hi] < A[lo]:
            swap(A, lo, hi)
    # otherwise do quicksort
    elif hi-lo > 1:
        p_idx = partition(A, lo, hi)
        quicksort(A, lo, p_idx - 1)
        quicksort(A, p_idx + 1, hi)


def partition(A, lo, hi):
        p_idx = randint(lo, hi)
        pivot = A[p_idx]
        swap(A, lo, p_idx)
        l_idx = lo + 1
        r_idx = hi
        while l_idx < r_idx:
            while l_idx <= r_idx and A[l_idx] <= pivot:
                l_idx += 1
            while A[r_idx] > pivot:
                r_idx -= 1
            if l_idx < r_idx:
                swap(A, l_idx, r_idx)
        swap(A, lo, l_idx - 1)
        return l_idx - 1


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
        quick_sort2.sort(l)
        """
    long_random_time = timeit.timeit(
        long_random_list_test,
        setup="import quick_sort2, random",
        number=repetitions
    )
    print "1000 item random int list with {} repetitions takes time {} with " \
        "insertion sort helping".format(repetitions, long_random_time)

    descend_case = """
        l = [i for i in xrange({}, 0, -1)]
        quick_sort2.sort(l)
        """

    ascend_case = """
        l = [i for i in xrange(0, {})]
        quick_sort2.sort(l)
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
            setup="import quick_sort2",
            number=repetitions
        )
        descend_results.append((size, descend_time))

        ascend_time = timeit.timeit(
            ascend_case.format(size),
            setup="import quick_sort2",
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
