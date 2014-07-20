from random import randint
'''
www.csanimated.com/animation.php?t=Quicksort
'''


def sort(A):
    quicksort(A, 0, len(A)-1)


def quicksort(A, start_idx, end_idx):
    # list has 0 or 1 elements
    if start_idx >= end_idx:
        pass
    # if small list, use insertion_sort for speed
    elif end_idx - start_idx < 16:
        insertion_sort(A, start_idx, end_idx)
    # otherwise do quicksort
    else:
        p_idx = partition(A, start_idx, end_idx)
        quicksort(A, start_idx, p_idx - 1)
        quicksort(A, p_idx + 1, end_idx)


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
    print "doing insertion sort with lo={} and hi={}".format(lo, hi)
    for i in xrange(lo, hi + 1):
        x = list[i]
        j = i
        while j > 0 and list[j-1] > x:
            list[j] = list[j-1]
            j -= 1
        list[j] = x
