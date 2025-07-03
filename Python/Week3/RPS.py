def RPS():
    print("Welcome to Rock Paper Scissors!")
    player1 = input("Player 1, Please enter your name: ")
    player2 = input("Player 2, Please enter your name: ")

    p1_Choice = input(f"{player1}, choose between Rock, paper, & Scissors: ").lower
    p2_Choice = input(f"{player2}, choose between Rock, paper, & Scissors: ").lower

    if p1_Choice == p2_Choice:
      print ("its a draw!")
    if  p1_Choice == "rock" and p2_Choice == "scissors":
     print(f"Rock beats scissors, {player1} wins!")
     
    elif p1_Choice == "paper" and p2_Choice == "rock":
     print(f"paper beats rock, {player1} wins!")

    elif p1_Choice == "scissors" and p2_Choice == "paper":
     print(f"scissors beats paper, {player1} wins!")
    
    if  p2_Choice == "rock" and p1_Choice == "scissors":
     print(f"Rock beats scissors, {player2} wins!")

    elif p2_Choice == "paper" and p1_Choice == "rock":
     print(f"paper beats rock, {player2} wins!")

    elif p2_Choice == "scissors" and p1_Choice == "paper":
     print(f"scissors beats paper, {player2} wins!")

    def IsValidMove(playerMove):
      validMoves = ["rock", "paper", "scissors"]
      if playerMove in validMoves:
             return True
      else:
        return False
      
RPS()