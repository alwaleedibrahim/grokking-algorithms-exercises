arr = [0,12,43,6,3,61,4,3]

def recursive_len (arr):
    if (len(arr)==0):
        return 0
    else:
        return 1 + recursive_len(arr[1:])
    
print(recursive_len(arr))