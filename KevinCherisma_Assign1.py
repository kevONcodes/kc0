#Kevin Cherisma
#5/29/2023
#Assignment 1
#To see how well we know python 

#1 (1.1)
#This function takes the vaules entered and finds out if n is a value of m.
def multipe(n,m):
  if n % m == 0:
    return True 
  else:
    return False

print(multipe(17,4))

#2 (1.2)
#This function takes k and decides if its even or odd by showing true for even and false for odd.
def is_even(k):
  while k > 2:
    k -= 2
  if k == 2:
    return True
  else:
    return False

print(is_even(8))

#3 (1.3)
#This function find the maximum and minimum
data = [2,90,55,2,1,27,7]

def minmax(data):
  mx = data[0]
  mn = data[0]
  for a in data:
    if a > mx:
      mx = a
  for a in data:
    if a < mn:
      mn = a 
  print(f"maximum is {mx}, minimum is {mn}")

minmax(data)

#4 (1.4)
#This function adds the sum of the squares of all the numbers less than n
def sum_of_sqs(n):
    sum = 0
    while n > 0:
        n -= 1 
        sum += n**2
    if n < 0:
      raise TypeError("Negative number entered")
    return sum

print(sum_of_sqs(5))

#5 (1.5)
#This function does the same but on one line of code
def sumofsqs(n):
  return sum(k ** 2 for k in range(1, n))
  
print(sumofsqs(5)) 

#6 (1.6)
#this function adds the sum of squares of all the odd numbers less than n
def sum_of_odd(n):
    sum = 0
    while n > 0:
      n -= 1 
      if n % 2 != 0:
        sum += n**2 
    if n < 0:
      raise TypeError("Negative number entered")
    return sum
  
print(sum_of_odd(5))

#7 (1.7) 
#This function does the same but on one line of code
def sumofodd(n):
  return sum(k ** 2 for k in range(1, n, 2))
  
print(sumofodd(5))

#8 (1.9)
#this function print a list with specific parameters to get the result 50, 60, 70, 80
l = list(range(50, 90, 10))
print(l)
