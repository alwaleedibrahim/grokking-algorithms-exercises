list = []
for i in range(0, 1000):
    list.append(i)
item = int(input("Enter a number in range 0 to 1000: " ))

def binary_search (list, item) :
    low = 0
    high = len(list) -1
    steps = 0

    while (low <= high):
        steps += 1
        mid = int((high + low) / 2)

        if (item < list[mid]) : 
            high = mid - 1
        elif (item > list[mid]):
            low = mid + 1
        else :
            return [mid, steps]

    return [None, steps] 

result = binary_search(list, item)
print("Item index is " + str(result[0]) + "\nfound in " + str(result[1]) + " steps" )