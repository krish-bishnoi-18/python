def great(a,b,c):
    if a>b and a>c :
        print(a,"is the greats the number you entred")
    elif b>a and b>c :
        print(b,"is the grreast you have entre ")
    else :
        print(c,"is the greeatest ")
for i in range(5):
    a,b,c=map(int,input("please entre the number").split())
    great(a,b,c)
    