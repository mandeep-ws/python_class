#The Fibonacci Sequence is the series of numbers:

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# 0 + 0 , 0 +1 , 1 + 1, 1 + 2 , 2 + 3 , 3 + 5 

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fibonacci(n): 
    a = 0
    b = 1
    z = []
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c
            z.append(b)
        print(sum([i for i in z if i % 2 == 0]))
        return b
        
print(fibonacci(40))



def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
  
# Driver Program 
  
print(Fibonacci(10)) 