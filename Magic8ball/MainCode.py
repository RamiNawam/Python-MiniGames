import random as rd
import time

def magic_8_ball():
  f=open("responses.txt","r")
  responses=f.readlines()
  f.close()
  input("You may ask your question\n")
  print('Thinking.',end='')
  time.sleep(1)
  print (".",end='')
  time.sleep(1)
  print (".",end='')
  time.sleep(1)
  print(".")
  time.sleep(rd.randint(1,2))
  print("The magic 8 ball says:",rd.choice(responses))
  repeat=input("Do you have more questions(y/n)\n")
  repeat=repeat.lower()
  if repeat=="y":
    magic_8_ball()
  elif repeat == "n":
    print("Thank you, come back later")
  else:
    print ("invalid input")
magic_8_ball()