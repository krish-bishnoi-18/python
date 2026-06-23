import random 
score = random.randint(0,100)
with open("game.txt") as file :
    highscore=file.read()
    print(f"your score is {score}")
if str(score)>highscore:
    with open("game.txt","w") as file :
        file.write(str(score))
print(highscore)
