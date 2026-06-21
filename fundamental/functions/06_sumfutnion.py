def sum(a):
    if a==0 :
        return 0 
    return a+sum(a-1)
for i in range(5):
   a=int(input("please entre thr numebr "))
   print(sum(a))