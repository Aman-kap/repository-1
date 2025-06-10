import random
import time

print("THE 7 GAME:")
time.sleep(0.25)
print("2 dies will be rolled")
print('pick either above or below 7 and see if you win...')


won = 0
lost = 0
draw = 0

def values(first, second):
    print(f'the first dice has rolled a {first}')
    print(f"the second dice has rolled a {second}")

class dice:
  def roll(self):
      first = random.randint(1,6)
      second = random.randint(1,6)
      total = first + second
      return (first , second, total)

house_dice = dice()


while True:
    while True:
     choice = input("(A)above or (B)below 7: ").lower()
     if choice == "a" or choice ==  "b":
        break
     else:
         print("invaild input, only type 'A' or 'B'")

    first, second, total = house_dice.roll()
    time.sleep(0.35)


    if choice == "a" and total > 7:
        print(f"total is {total} you have won!!")
        won = won  + 1
    elif choice == "b" and total < 7:
        print(f"total is {total} you have won!!")
        won = won + 1
    elif total == 7:
        print(f"total is {total}, its a draw")
        draw = draw + 1
    elif choice == "a" and total < 7:
        print(f"total is {total} you have lost")
        lost = lost + 1
    elif choice == "b" and total > 7:
        print(f"total is {total} you have lost")
        lost = lost + 1

    print(f"""
WON : {won}
LOST : {lost}
DREW : {draw}""")

    play_again = input("do you want to play again? Y/N: ").lower()
    time.sleep(0.35)
    if play_again == "n":
         print("it was a fun time, make sure to play again ;)")
         break
