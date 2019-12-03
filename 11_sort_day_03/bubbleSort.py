"""
    Bubble sort

    Author: Mengjiao
"""

from typing import List

def bubble_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return

    for i in range(length):
        made_swap = False   # 数据交换标志位
        for j in range(length - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]    # 数据交换
                made_swap = True    # 有数据交换
        if not made_swap:   # 没有数据交换
            break


def insertion_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return

    for i in range(1, length):
        value = a[i]
        j = i - 1
        while j >= 0 and a[j] > value:  # 查找位置
            a[j + 1] = a[j]    #数据移动
            j -= 1
        a[j + 1] = value    #插入数值

array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
insertion_sort(array)
print(array)