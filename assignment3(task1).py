a=int(input("enter your no."))
def factorial(a):
    if a<2:
        return 1
    else:
        return a*factorial(a-1)
b=factorial(a)
print(b)