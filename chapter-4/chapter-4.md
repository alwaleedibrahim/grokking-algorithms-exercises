# Grokking Algorithms - Chapter 4

## Exercise 4.1 
- Write out the code for the earlier sum function.
```py
def recursive_sum (arr):
    if (arr == []):
        return 0
    else:
        return arr[0] + recursive_sum(arr[1:])
```
## Exercise 4.2 
- Write a recursive function to count the number of items in a list.
```py
def recursive_len (arr):
    if (arr==[]):
        return 0
    else:
        return 1 + recursive_len(arr[1:])
```
## Exercise 4.3 
- Find the maximum number in a list.
```py
def recursive_max (arr):
   if (len(arr) == 0):
        print("Max is None")
        return None
   elif(len(arr)==1):
        print("Max of single element "+ str(arr[0]))
        return arr[0]
   elif(len(arr)==2):
        print("Max of " + str(arr[0]) + " and " + str(arr[1]))
        if (arr[0]>arr[1]):
            print("is "+ str(arr[0]))
            return arr[0]
        else:
            print("is "+ str(arr[1]))
            return arr[1]
   else:
       print("Calculating max of the first two " + str(arr[0:2]))
       max_of_the_first_two = recursive_max(arr[0:2])
       print("Calculating max of the rest " + str(arr[2:]))
       max_of_the_rest = recursive_max(arr[2:])
       return  recursive_max([max_of_the_first_two, max_of_the_rest])
```
## Exercise 4.4 
- Remember binary search from chapter 1? It’s a divide-and-conquer 
algorithm, too. Can you come up with the base case and recursive 
case for binary search

    - Answer: Base case is that the middle item is the one we are searching for. recusrvie case is either the middle item is too high or too low. in this case we remove half of the element and reduce the problem to the other half.

    - Here is what is the code looks like:
```py
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
```

## How long would each of these operations take in Big O notation?
## Exercise 4.5 
- Printing the value of each element in an array. 
    - O(n)
## Exercise 4.6 
- Doubling the value of each element in an array.
    - O(n)
## Exercise 4.7 
- Doubling the value of just the first element in an array.
    - O(1)
## Exercise 4.8 
- Creating a multiplication table with all the elements in the array. So if your array is [2, 3, 7, 8, 10], you first multiply every element by 2, then multiply every element by 3, then by 7, and so on. 
    - O(n^2)