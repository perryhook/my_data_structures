"""
adapted from 'The Object of Data Abstraction and Structures Using Java'
"""


def merge_sort(a):
    do_merge_sort(a, 0, len(a)-1)


def do_merge_sort(a, lo, hi):
    if lo < hi:
        mid = (lo + hi) / 2
        do_merge_sort(a, lo, mid)
        do_merge_sort(a, mid+1, hi)
        merge(a, lo, hi)


def merge(a, lo, hi):
    mid = (lo + hi) / 2
    l_idx = lo
    r_idx = mid+1
    tmp = []
    tmp_idx = 0
    while (l_idx <= mid) and (r_idx <= hi):
        if a[l_idx] < a[r_idx]:
            tmp.append(a[l_idx])
            l_idx += 1
        else:
            tmp.append(a[r_idx])
            r_idx += 1
        tmp_idx += 1

    # copy remaining values from left list into tmp
    for j in xrange(l_idx, mid+1):
        tmp.append(a[j])
        tmp_idx += 1

    # copy remaining values from right list into tmp
    for j in xrange(r_idx, hi+1):
        tmp.append(a[j])
        tmp_idx += 1

    # copy tmp back into a
    for j in xrange(lo, hi+1):
        a[j] = tmp[j-lo]
