
# Python Functions - Multiple Choice Questions

## 1. What will be the output of the following code?
   ```python
   def greet():
       return "Hello, World!"
   
   print(greet)
   ```
   a) Hello, World!  
   b) greet  
   c) <function greet at some_memory_location>  
   d) Error  

   **Answer:** c

## 2. What is the error in the following function definition?
   ```python
   def add_numbers(a, b)
       return a + b
   ```
   a) SyntaxError: Missing parentheses in call  
   b) IndentationError  
   c) SyntaxError: Expected ':'  
   d) No error  

   **Answer:** c

## 3. What will be the output of the following code?
   ```python
   def test(x, y=5):
       return x * y
   
   print(test(2))
   ```
   a) 2  
   b) 10  
   c) Error: Missing argument  
   d) None of the above  

   **Answer:** b

## 4. What will be the output of the following function?
   ```python
   def my_func(a, b):
       print(a, b)
   
   my_func(b=2, a=3)
   ```
   a) 3 2  
   b) 2 3  
   c) Error: Positional argument missing  
   d) None of the above  

   **Answer:** a

## 5. What will be the output of the following code?
   ```python
   def square(num):
       return num * num
   
   print(square())
   ```
   a) 0  
   b) Error: Missing argument  
   c) None  
   d) 1  

   **Answer:** b

## 6. What will be the output of the following code?
   ```python
   def func(x=[]):
       x.append(1)
       return x
   
   print(func())
   print(func())
   ```
   a) [1] [1]  
   b) [1] [1, 1]  
   c) [1, 1] [1]  
   d) Error  

   **Answer:** b

## 7. Identify the error in the following function call:
   ```python
   def multiply(a, b):
       return a * b
   
   print(multiply(2))
   ```
   a) TypeError: Missing required argument  
   b) SyntaxError  
   c) NameError  
   d) No error  

   **Answer:** a

## 8. What will be the output of the following function?
   ```python
   def test():
       return "Hello"
       return "World"
   
   print(test())
   ```
   a) Hello  
   b) World  
   c) Error  
   d) None  

   **Answer:** a

## 9. What will be the output of the following code?
   ```python
   def modify(x):
       x = x + 1
       return x
   
   y = 10
   modify(y)
   print(y)
   ```
   a) 10  
   b) 11  
   c) Error  
   d) None  

   **Answer:** a

## 10. What is the error in the following function?
   ```python
   def example(a, b, *args, c):
       print(a, b, args, c)
   ```
   a) No error  
   b) SyntaxError: *args must be at the end  
   c) TypeError  
   d) SyntaxError: c must be after *args  

   **Answer:** d
