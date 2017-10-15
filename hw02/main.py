def bsearch(data, target):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target < data[mid]:
            high = mid - 1
        elif target > data[mid]:
            low = mid + 1
        elif data[mid] == target:
            return mid
    else:
        return None


def main():
    data_lst = [1, 2, 3, 4, 5]
    target = int(input("请输入需查找的元素："))
    position = bsearch(data_lst, target)
    print("元素{0}的位置为：{1}".format(target, position))


main()
