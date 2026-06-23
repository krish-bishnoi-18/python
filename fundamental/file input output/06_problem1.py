file= open("krish.txt")
insidefile=file.read()
print(insidefile)
if "krish" in insidefile:
    print("yeah this file contain word krish")