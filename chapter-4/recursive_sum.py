arr = [1,4,7,1,8,3,94,7,3,7,7,3,6,3,6,5]

def recursive_sum (arr):
    if (len(arr)==1):
        return arr[0]
    elif (len(arr)== 0):
        return 0
    else:
        return arr[0] + recursive_sum(arr[1:])

print(recursive_sum(arr))