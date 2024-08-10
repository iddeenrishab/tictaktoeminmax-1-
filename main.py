
def constBoard(board):
  print("\nCurrent state of the board:\n\n")
  for i in range(9):
    if((i%3==0) and (i>0) ):
      print("\n")
    if(board[i]==-1):
      print("X ",end="   ")
    elif(board[i]==0):
      print("_ ",end="   ")
    elif(board[i]==1):
      print("O ",end="   ")




def user1Turn(board):
  pos=int(input("\nEnter X 's position[1-9] :"))
  if(board[pos-1]!=0):
    print(" \nIncorrect move .....!!!!!\n.........ENDING THE GAME..")
    exit(0)
  else:
    board[pos-1]=-1

def user2Turn(board):
  pos=int(input("\nEnter O 's position[1-9] :"))
  if(board[pos-1]!=0):
    print("\n Incorrect move .....!!!!!\n.........ENDING THE GAME..")
    exit(0)
  else:
    board[pos-1]=1




def analyseBoard(board):
  cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  for i in range (8):
    if((board[cb[i][0]]==board[cb[i][1]]) and (board[cb[i][1]]==board[cb[i][2]]) and (board[cb[i][0]]!=0)):
      return board[cb[i][0]]
  return 0

def computerTurn(board):
  pos=-1
  value=-2
  for i in range (9):
    if(board[i]==0):
      board[i]=1
      score=-minmax(board,-1)
      board[i]=0
      if(score>value):
        value=score
        pos=i
  board[pos]=1



def minmax(board,player):
    x=analyseBoard(board)
    pos=-1
    value=-2
    if(x!=0):
        return (x * player)
    for i in range (9):
        if(board[i]==0):
            board[i]=player
            score=-minmax(board,player*-1)
            board[i]=0
            if(value<score):
                value=score
                pos=i
    if(pos==-1):
        return 0
    return value





def main():
  choice=int(input("Enter 1 for single player or 2 for multi_player Game :"))
  board=[0,0,0,0,0,0,0,0,0]
  if(choice==1):
    print("Computer: 0    vs Player: X")
    player = int(input("Enter 1 to play First \nEnter 2 to play Second    :"))
    for i in range(9):
      if(analyseBoard(board)!=0):
        break;
      if((i+player)%2==0):
        computerTurn(board)
      else:
        constBoard(board)
        user1Turn(board)

  else:
    for i in range(9):
      if(analyseBoard(board)!=0):
        break
      if (i%2==0):
        constBoard(board)
        user1Turn(board)
      else:
        constBoard(board)
        user2Turn(board)
  constBoard(board)
  if(analyseBoard(board)==0):
    print("\nDRAW .....!!!")
  elif(analyseBoard(board)==-1):
    print("\nPLAYER 1 HAS WON ")
  elif(analyseBoard(board)==1):
    print("\nPlayer 2 has won")



main()
#certificate@devtown.in
