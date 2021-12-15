import math
import random

lowerbound = int(input("\n Enter the lower limit of range :"))

upperbound = int(input(" \n Enter the upper limit of range :"))

x = random.randint(lowerbound,upperbound)

print("\n You have "+str(round(math.log(upperbound - lowerbound + 1,2))) +" chances to complete the game ")

count = 0



while count < round(math.log(upperbound - lowerbound + 1,2)):
    count = count + 1

    guess = int(input("\n Guess the Number :"))
    
    if guess == x:
        print("\n YOu have successfully guessed the  number i.e ",x)
        break
    elif guess < lowerbound or guess > upperbound:
        print("\n Number is OUT OF RANGE !!")
   

    elif guess > x:
        print(" \n TRY AGAIN !!, you guess too 'HIGH' ..")
    elif guess < x:
        print(" \n TRY AGAIN !!, you guess too 'LOW' ..")

    print("######## you have ",round(math.log(upperbound - lowerbound + 1,2))-count, " chances left #########")
    

if count >= math.log(upperbound - lowerbound + 1,2):
    print("\n BETTER LUCK NEXT TIME !! The number was ",x)



