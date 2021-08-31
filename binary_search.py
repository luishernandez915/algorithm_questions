def binarySearch(arr, target):#remember that this only works on sorted arrays
    left = 0 #left pointer.First element in array
    right = len(arr)-1 #right pointer. Last element in array

    while(left <= right):
        mid = (left+right)//2  # 0 5 => ((0)(+)(5)/2)) = 2

        if(arr[mid] == target):#return element if == target
            return mid
        elif(arr[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1,2,3,4,5,6]
target = 6

result = binarySearch(arr, target)

if result != -1:
    print("Element is present at index ", result)
else:
    print("Element is not present in the array")
