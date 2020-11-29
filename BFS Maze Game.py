import queue

def print_maze(maze, start,path=""):
    row, col = start

    pos = set()
 
    for move in path:
        if move == "L":
            col -= 1

        elif move == "R":
            col += 1

        elif move == "U":
            row -= 1

        elif move == "D":
            row += 1
        pos.add((row, col))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


def create_maze():

    maze = []
    maze.append(["#","#","#","#","#","O","#","#"])
    maze.append(["#"," "," "," "," "," "," ","#"])
    maze.append(["#"," "," "," "," "," "," ","#"])
    maze.append(["#"," "," ","#"," "," "," ","#"])
    maze.append(["#","#"," ","#"," "," "," ","#"])
    maze.append(["#"," "," ","#"," "," "," ","#"])
    maze.append(["#"," "," ","#"," "," "," ","#"])
    maze.append(["#","X","#","#","#","#","#","#"])

    return maze


def is_valid_move(maze, start,move):

    row, col = start
     
    for m in move:
      
        if m == "L":
            col -= 1

        elif m == "R":
            col += 1

        elif m == "U":
             row -= 1

        elif m == "D":
            row += 1

        if not (0 <= row < len(maze) ) and (0 <= col < len(maze[0])):
            return False
        if maze[row][col] == "#":
            return False
        
        
    if(row,col) not in visited:
            visited.append((row,col))
            return True

    return False


def find_exit(maze,start,moves):
  
    row, col = start

    for m in moves:
      
        if m == "L":
          col -= 1

        elif m == "R":
          col += 1

        elif m == "U":
           row -= 1

        elif m == "D":
          row += 1
   
    if maze[row][col] == "X":
        print_maze(maze,start, moves)
        return True

    return False


#Algorithm
def bfs(maze,startposition):

  q = queue.Queue()

  #Initial move
  q.put("")
  moves = ""
  count = 0

  #Looping until find_exit return True
  while not find_exit(maze,startposition, moves):
    moves = q.get()
    count = count + 1

    for i in ["L","R","U","D"]:
      next = moves + i
      if is_valid_move(maze,startposition,next):
          q.put(next)

  print()
  print("Found exit using: "+ str(count) + " attempts")

print("Breadth first search algorithm")
print()
maze = create_maze()
visited = []

#Defining starting position
for r in range(len(maze)):
    for c in range(len(maze[r])):
           if maze[r][c] == "O":
               start = (r,c)
if start:
    bfs(maze,start)
