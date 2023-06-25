def minimum_index (arr):
    min = arr[0]
    index = 0
    for i in range(len(arr)):
        if (arr[i]<min):
            min = arr[i]
            index = i
    return index

def selection_sort (arr):
    sorted = []
    for i in range(len(arr)):
        min = minimum_index(arr)
        sorted.append(arr[min])
        arr.pop(min)
    
    return sorted

print(selection_sort([6,1,4,9,2,6,7,0,6,324,632,64,23,86,32,54,84,246,86,435, -1]))