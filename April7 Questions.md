# Pre-Lab: Working With Larger Amounts of Data

In this prelab, you will be building small programs to work with more data than just single inputs that we've been getting from our users by the input function.

For all the problems: do not write any input statements unless specifically requested. Each problem will explain what data you have available, and any helper functions that might be available for you to use (e.g., functions you don't have to write, but can just use and assume they work).

You may use the following link to access the syntax sheet: [Syntax Sheet](#)

## Question 1

### Create a small Python program to process a list of integers and then report whether or not they belong to a Pythagorean Triple.

In order to accomplish this, you will need to read 3 integers from the list and then determine if they are a valid solution to the equation \(a^2 + b^2 = c^2\). As an example, the values 3, 4, 5 satisfy this equation because \(9 + 16 = 25\). Make sure that you test all arrangements of the numbers, and that they pass the test if any one of the possibilities works. 3, 4, 5 works, but 4, 5, 3 and 3, 5, 4 do not, but as long as one works, we're satisfied. For each triple, output the values and a message with the results.

Assume that a list already exists called `numbers`, that its length is a multiple of 3, and that all values are random integers. Write a function called `is_triple()` with three arguments and a return value. Call it from the main routine that is processing the entire list of numbers. Use the practices instructed in class for deciding what to put inside the function and what to put in the main routine.

#### Sample Output:

```
3, 4, 5 are a Pythagorean Triple
3, 5, 4 are a Pythagorean Triple
1, 2, 4 are not a Pythagorean Triple
```

## Question 2

### Consider the game Tic-Tac-Toe where we can represent a board as a 2-dimensional list of one character strings.

A board is a 3x3 collection of the characters "X", "O", or " " representing one of the player's choices or a space for an empty location. In the game, X goes first, followed by O. Play alternates until the game is won. The game is won when a player places 3 of its symbols in a straight line - a row, a column, or a diagonal.

Write a function that accepts a Tic-Tac-Toe board as input and reports whether the board represents a won game or not, or if the board is invalid. A board is invalid if it has more O's than X's, if it has more than one more X's than O's (i.e., 3 X's and 1 O is invalid but 2 X's and 1 O is valid), or if both players have won.

If it is a won game, return the string of the winning player. If it is invalid, throw a value error with the code `raise ValueError("Invalid board state")`. If it is not a won game, return Boolean `False`.

No main function is required. Loops are not required for full marks but will shorten the solutions.

## Question 3

### You are given a list of intercepted strings containing fragments of a hidden message.

Each string looks like random letters, but the message can be revealed by slicing and combining specific parts.

Write a Python function that takes a list of strings and creates a new list, where each new string is formed by taking the first half of one string, and adding the second half of the next string. Use each pair of adjacent strings in the list to form one new string. If a string has an odd number of characters, round down if it is for the first half and up if it is for the second half.

Append each result to a new list and return that list.

#### Example:

```python
words = ["goonie", "ad", "jab", "blob", "leaves", "returning", "pythium", "archon"]
```

Your program should return:

```python
['good', 'job', 'learning', 'python']
```
