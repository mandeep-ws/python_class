#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.


x = ([ i if i % 3 == 0 and i % 5 == 0 else i if i % 3 == 0 else i if i % 5 == 0 else 0 for i in range(1,100)])
print(x)
