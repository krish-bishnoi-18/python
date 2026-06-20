a,b=map(int , input("please entre the numebr od atrts in first and last row it ").split())
if a%2!=0 and b%2!=0 :
   for i in range(a,b+1):
     print(" "*(b-i),"*"*(2*i-1))
     i=i+1