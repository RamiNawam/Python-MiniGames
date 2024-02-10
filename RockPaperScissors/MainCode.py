import random
def game(r):
  print ("welcome to the game")
  print ("=======================================\n")
  print ("game rules:\n1) Rock vs paper --> paper wins\n2) paper vs scissors -->scissors wins\n3) scissors vs rock--> rock wins")
  print ("")
  for i in range (r):
    print ("choose from the following")
    print ("1-->rock\n2-->scissors\n3-->paper")
    player=int(input())
    if player==1:
      print ("you chose rock")
    elif player==2:
      print ("you chose scissors")
    elif player==3:
      print ("you chose paper")
    else :
      print ("invalid input")
      break
    computer=random.randint(1,3)
    if computer==1:
      print ("the computer has chosen rock")
    elif computer==2:
      print ("the computer has chosen scissors")
    else :
      print ("the computer has chosen paper")
    if player==computer:
      print ("this round ended in a draw")
    elif (computer==1 and player==2) or (computer==3 and player==1) or (computer==2 and player==3):
      print ("the computer won this round")
    else :
      print ("you have won")
    
game(1)
