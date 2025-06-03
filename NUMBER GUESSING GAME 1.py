import time
import random
print("GUESS THE NUMBER...")
time.sleep(1)
print("The number is between 1-9,")
print("guess the number in 3 chances...goodluck")
print('________________________________________________________________________________________________________________________________________________-')

secret_number = random.randint(1,9)
guess_limit= 3
guess_counted =0
while guess_limit>guess_counted:
   guess=int(input("Guess:"))
   guess_counted = guess_counted + 1
   if guess==secret_number:
      print("YOU WIN...")
      break
   else:
     attempts_left = guess_limit - guess_counted
     if attempts_left > 0:
      print(f"wrong answer, you have {attempts_left} attempts left")
      time.sleep(0.5)

else:
   print("NO MORE GUESSES LEFT, YOU FAILED...")
   print(f"{secret_number} was the CORRECT NUMBER")
