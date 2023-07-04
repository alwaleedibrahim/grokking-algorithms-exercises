# Grokking Algorithms - Chapter 1

## Exercise 1.1 
- Suppose you have a sorted list of 128 names, and you’re searching through it using binary search. What’s the maximum number of steps it would take? 

    - log(128)/log(2) = 7 steps

- Suppose you double the size of the list. What’s the maximum number of steps now?

    - 8 steps, since we take one more step to divide the list into half.

## Give the run time for each of these scenarios in terms of Big O:
## Exercise 1.3 
- You have a name, and you want to find the person’s phone number in the phone book.
    - Using binary search it will take O(log n) time
## Exercise 1.4 
- You have a phone number, and you want to find the person’s name in the phone book. (Hint: You’ll have to search through the whole book!)
    - O(n)
## Exercise 1.5 
- You want to read the numbers of every person in the phone book.
    - O(n)
## Exercise 1.6 
- You want to read the numbers of just the As. (This is a tricky one! It involves concepts that are covered more in chapter 4. Read the answer—you may be surprised!)
    - My initial answer for this question before reading chapter 4 is O(n), because the number of As is dependent on the number of the whole phone book. So as the size of the book grows up, the As also grow up making run time of this scenario O(n)