def factorial(a):
    if(a==1 or a==0):
        return 1
    return a*factorial(a-1)
a=int(input("please entre the value that how many time you wangt to calute the facotrial of df number "))
for i in range(0,a):
    b=int(input("please entre the number"))
    print(factorial(b))
    