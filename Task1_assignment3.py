#function using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
#call the function
print("---------------------function using recursion---------------")
num=int(input("enter a number:"))
print("factorial of", num ,"is",factorial(num))
print("------------------------------------------------------------")
#function using loop
def factorial2(m):
    fact=1
    for i in range(1,m+1):
        fact *=i
    return fact

#call the function
print("---------------------function using loop--------------------")
nu=int(input("enter a number:"))
print("factorial of", nu ,"is",factorial2(nu))
