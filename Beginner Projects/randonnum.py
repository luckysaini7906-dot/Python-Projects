import random
secrate_number=random.randint(1,100)
print("Secrate Number Genrater Game")
print("Please Guess Number Between 1 to 100 :")
attamps=0
while True:
    guess=int(input("Enter Your Guess Any Number :"))
    attamps+=1
    if guess<secrate_number:
        print("Too Low ! Please Try Again")
    elif guess>secrate_number:
        print("Too High ! Please Try Again")
    else:
        print(f"Congratulations You Find Random Number In ",attamps)