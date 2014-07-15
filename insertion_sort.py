def sort(list):
    """
    performs insertion sort on list in place
    source: http://en.wikipedia.org/wiki/Insertion_sort
    """

    for i in xrange(1, len(list)):
        x = list[i]
        j = i
        while j > 0 and list[j-1] > x:
            list[j] = list[j-1]
            j -= 1
        list[j] = x


if __name__ == '__main__':
    import timeit
    repetitions = 100

    long_random_list_test = """
        l = [random.randint(-99999,99999) for i in xrange(0, 1000)]
        insertion_sort.sort(l)
        """
    long_random_time = timeit.timeit(
        long_random_list_test,
        setup="import insertion_sort, random",
        number=repetitions
    )
    print "1000 item random int list with {} repetions takes time {}".format(
        repetitions, long_random_time)

    long_des_case_test = """
        l = [i for i in xrange(1000, 0, -1)]
        insertion_sort.sort(l)
        """
    long_des_case_time = timeit.timeit(
        long_des_case_test,
        setup="import insertion_sort",
        number=repetitions
    )
    print \
        "1000 item decending int list with {} repetions takes time {}".format(
            repetitions, long_des_case_time)

    long_asc_case_test = """
        l = [i for i in xrange(0, 1000)]
        insertion_sort.sort(l)
        """
    long_asc_case_time = timeit.timeit(
        long_asc_case_test,
        setup="import insertion_sort",
        number=repetitions
    )
    print \
        "1000 item ascending int list with {} repetions takes time {}".format(
            repetitions, long_asc_case_time)
