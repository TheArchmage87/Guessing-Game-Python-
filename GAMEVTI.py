from random import *
while True:
  input("Press [Enter] to begin new game.")
  x=randrange(1,100)
  z=0
  while z==0:
    y=input("What is your guess?")
    y=int(y)
    if x==y:
      print("You won.")
      z=1
    elif x>y:
      print("Too small.")
    elif x<y:
      print("Too big.")