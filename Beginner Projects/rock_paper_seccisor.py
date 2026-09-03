import random
print("=====Rock,Paper,Seccisor=====")
user_score=0
computer_score=0
while True:
        choice=["rock","paper","seccisor"]
        user=input("\n Enter Your Choice In Rock, Paper, Seccisor ").lower()
        
        if user not in choice:
            print("\n Sorry ! Please Enter Rock, Paper, Seccisor ")
            continue
        computer=random.choice(choice)

        print(f"\n User Choice is = {user}")
        print(f"\n Computer Choice is = {computer}")

        if user==computer:
              print("\n The Game Is a Tie !")
        
        elif((user=="rock" and computer=="seccisor")or
             (user=="paper" and computer=="rock")or
             (user=="seccisor" and computer=="paper")):
            
            print("You Win !")
            user_score+=1

        else:
              print("\n Computer Win !")
              computer_score+=1

        print("\n ------ Score ------")
        print(f"\n User Score is : {user_score}")
        print(f"\n Computer Score is : {computer_score}")

        play_again=input("\n Enter Your Choice To Play Again(Yes/No)").lower()
 
        if play_again != "yes":

            print("\n Final Score is :")
            print("\n You :",user_score)
            print("\n Computer :",computer_score)
            print("\n Thanks For Playing Game :")

            break
    

