## 归并排序

如果要排序一个数组，先把数组从中间分成前后两部分A和B，然后对A、B两部分分别排序，再将排好序的A、B合并在一起。对于A和B进行排序时，仍然采用归并排序的思想，将A分成C和D，对C和D进行排序进而合并成排好序的A。B亦然。因此，归并排序的主要思想是分治思想，而分治算法一般都是用递归实现的。图解如下：

![avatar](https://static001.geekbang.org/resource/image/db/2b/db7f892d3355ef74da9cd64aa926dc2b.jpg)

### 代码实现

```python
def merge_sort(a: List[int]):
    _merge_sort_between(a, 0, len(a) - 1)
```

定义归并排序算法，需要排序的数组a是int型的List。

```python
def _merge_sort_between(a: List[int], low: int, high: int):
    if low < high:
        mid = low + (high - low) // 2
        _merge_sort_between(a, low, mid)
        _merge_sort_between(a, mid + 1, high)
        _merge(a, low, mid, high)
```
   1. 定义递归调用函数。函数参数为需要排序的int型数组，数组的首位索引low和数组的末位索引high。
   2. 如果数组的首位索引low小于末位索引high，那么该数组就可被划分为A、B两部分，并对A、B两部分分别进行内部排序。
   3. 数组划分位置的索引为mid，其中“ // 2 ” 为下整除。即若为奇数，则中位数被划分到后一部分数据中。
   4. 对于划分好的数据A和B，若满足划分条件，则继续划分为更小的子数组。
   5. 将排好序的数据用_merge函数进行合并。

```python
def _merge(a: List[int], low: int, mid: int, high: int):
    # a[low:mid], a[mid+1:high] are sorted.
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if a[i] < a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j +=1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(a[start:end + 1])
    a[low:high + 1] = tmp
```
1. 定义merge函数，参数为需要排序的int数组a，首位索引low，中位索引mid，末位索引high。此时原始数组a已被划分成两部分：数组a1[low:mid]和数组a2[mid+1:high]，且这两个数组内部已排好序。
2. 用i,j分别代表a1和a2的首位索引，并进行比较，将较小的数写入临时数组tmp中，并将索引移至该子数组(a1/a2)的下一位。
3. 未参与比较的数组元素采用切片的方式，直接加入已排好的数组中。
4. 将排好序的储存在临时数组tmp的数据，copy到原始数组中。

merge思想如图所示：
![avatar](https://static001.geekbang.org/resource/image/95/2f/95897ade4f7ad5d10af057b1d144a22f.jpg)

### 相关问题

1. 归并排序是稳定的排序算法。
    在合并过程中，如果A、B两个子数组之间有值相同的元素，可以先把A中的元素放入tmp数组中，这样就保证了值相同元素，在合并前后的先后顺序不变。
2. 归并排序的时间复杂度是O(nlogn)。
3. 归并排序的空间复杂度是O(n)。