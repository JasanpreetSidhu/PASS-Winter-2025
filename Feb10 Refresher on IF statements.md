# Feb10 Refresher on IF statements

### 1. What is the error in the following code?
```python
num = 10
if num > 5:
    print("Greater than 5")
else:
    if num > 8:
        print("Greater than 8")
```
### 2. Find and Fix the error in this program:
```python
x = 15
if x > 10 or x < 20:
    print("Between 10 and 20")
else:
    print("Out of range")
```
### 3. Identify the issue in this code:
```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")
```
### 4. What will be the output of the following code? Is there an error?
```python
a, b, c = 5, 10, 15
if a > b and c > a:
    print("Condition met")
else:
    print("Condition not met")
```
### 5. What will be the output of the following code?
```python
x = 7
if x > 5:
    if x < 10:
        print("A")
    else:
        print("B")
else:
    print("C")
```
### 6. What is the result of this expression?
```python
>>> True and False or True
```
A) True  
B) False  
C) Error  
D) None  
