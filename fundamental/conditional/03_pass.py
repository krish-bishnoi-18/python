a,b,c=map(int,input("please entre the number of per subj").split())
d=a+b+c
if a>=33 and b>=33 and c>=33 :
    if d>120 :
     print("cong your are pass")
     print("your marks are ",a,b,c)
    else :
       print("oo no your failed as per total marks  criteria")
       print("your marks are ",a,b,c)
else :
   print("your are failed as per you cant even cross 33 percent in one subj")
   print("your marks are ",a,b,c)
   if a<33 or b<33 or c<33 :
    if a<33 and b>33 and c> 33:
      print("you are failed in subj a with marks ",a)
    elif b <33 and a>33 and c>33:
      print("you are failed in a subj b with marks ",b)
    elif c<33 and a>33 and b>33 :
      print("you are faile din sub c with marks ",c)
    elif a<33 and b <33 and c>33:
      print("you are failed in sub a and b with marks ",a,b)
    elif b<33 and c <33 and a>33 :
      print("you are failed in sub b and c with marks ",b,c)
    elif c<33 and a<33 and b>33 :
      print("you are failed in sub c and a with marks ",c,a)
    else :
      print("you are failed in all the subjs a,b,c woth marks ",a,b,c)

     
      
