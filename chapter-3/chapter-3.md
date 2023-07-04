# Grokking Algorithms - Chapter 2

## Exercise 3.1 
- Suppose I show you a call stack like this. What information can you give me, just based on this call stack? 

|FUNCTIONS         |PARAMETERS|
|--------------|---|
| Greet2       | NAME: MAGGIE |
| Greet        | NAME: MAGGIE |

- 
    - Answer: 
        - Greet function was called and was passed the name Maggie to it 
        - Greet function is partially completed
        - Greet2 function is called inside Greet function
        - Greet2 function will be completed first, then Greet will be coninued

## Exercise 3.2 
- Suppose you accidentally write a recursive function that runs forever. As you saw, your computer allocates memory on the stack for each function call. What happens to the stack when your recursive function runs forever?

    - Answer: the stack gets full. The term for this condition is stack overflow.

