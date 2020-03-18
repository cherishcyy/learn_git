# -*- coding: utf-8 -*-
"""使用迭代查找一个list中最小和最大值，并返回一个tuple"""


def findMinAndMax(lst):
    lst = [1, 2, 3, 4, 5, 5, 9]
    mi = ma = lst[0]
    for i in range(1, len(lst)):
        if lst[i] >= ma:
            ma = lst[i]
    for i in range(1, len(lst)):
        if lst[i] <= mi:
            mi = (lst[i])
    return mi, ma

print(findMinAndMax([1,2,3]))
