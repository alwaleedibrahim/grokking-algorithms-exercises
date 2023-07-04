arr = [0,1,2,3,4,5,6,7,8,9]

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
   
print(recursive_max(arr))