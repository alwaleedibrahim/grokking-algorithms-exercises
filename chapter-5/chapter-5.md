# Grokking Algorithms - Chapter 5

## Exercise 4.1 

Which of these hash functions are consistent?
## Exercise 5.1 
- `f(x) = 1`  Returns “1” for all input
    - Consistent. The same input will produce the same output every time.

## Exercise 5.2 
- `f(x) = rand()`  Returns a random number every time
    - Inconsistent

## Exercise 5.3 
- `f(x) = next_empty_slot() ` Returns the index of the next empty slot in the hash table
    - Inconsistent. The next empty slot is diffrent every time.

## Exercise 5.4 
- `f(x) = len(x) ` Uses the length of the string as the index
    - Consistent. The length of the input is the same every time the function is executed.
