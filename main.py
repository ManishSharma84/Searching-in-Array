def find(ary, siz, k):
    for i in range(siz):
        if ary[i] == key:
            return i

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = 1
d = len(arr)

index = find(arr, d, key)
if index == -1:
    print("Element not Fond")
else:
    print("Element fond at location " + str(index + 1))
