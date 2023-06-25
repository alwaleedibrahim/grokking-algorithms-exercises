def factorial (number):
    if (number==0):
        return 1
    elif (number==1):
        return 1
    else: 
        return number * factorial(number-1)
    
input_num = int(input("Enter a number to find its factorial: "))
print(factorial(input_num))