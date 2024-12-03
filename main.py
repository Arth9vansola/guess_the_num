from random import randint

n = randint(1,100)
a=-1
guess=1

while(a!=n):
    a = int(input("guess the number between  1 to 100:\n"))
    if(a>n):
        print("please lower number")
        guess+=1
    elif(a<n):
        print("please higher number")
        guess+=1 

print(f"you guessed the correct number {n} in {guess} attempts")        