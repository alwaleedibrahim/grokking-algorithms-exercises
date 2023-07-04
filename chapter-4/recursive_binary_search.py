list = []
for i in range(0, 1000):
    list.append(i)
item = int(input("Enter a number in range 0 to 1000: " ))

def recursive_binary_search (list, item):
    low = 0
    high = len(list) -1
    mid = int((low + high) / 2)
    if (mid >= low and mid <= high):
        if (item < list[mid]):
            high = mid
            return recursive_binary_search(list[0:high], item)
        elif (item > list[mid]):
            low = mid + 1
            return low + recursive_binary_search(list[low:], item)
        else:
            return mid
    else:
        return None
    
result = recursive_binary_search(list, item)
print("Item index is " + str(result))