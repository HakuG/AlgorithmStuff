import sys

# Given a maze of Monsters and Walls find the shortest path to the end without losing
# lives

class Queue:
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def put(self, item):
        self.items.insert(0,item)

    def get(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class MazeComponent:
    def __init__(self, row, height, lives):
       
        self.visited = False
        self.distance = 0
        self.row = row
        self.column = height
        self.lives = lives;
    def visit (self):
        visited = True

def main():
    height, width, lives = map(int, raw_input().split())
    MatrixBegin = [[0 for rows in xrange(width)] for col in xrange(height)]
    MatrixEnd = [[[0 for life in xrange(lives)] for rows in xrange(width)] for col in xrange(height)]
    S = (0, 0)
    E = (0, 0)
    for row in range(height):
        MatrixBegin[row] = map(str, raw_input().split())
        for column in range(width):
            for life in range(lives):
                MatrixEnd[row][column][life] = MazeComponent(row, column, life)
                if MatrixBegin[row][column] == 'S':
                    S = (row,column)
                elif MatrixBegin[row][column] == 'E':
                    E = (row, column)
                    MatrixEnd[row][column][life].distance = -1
                elif MatrixBegin[row][column] == 'X':
                    MatrixEnd[row][column][life].visited = True;
    q = Queue()
    MatrixEnd[S[0]][S[1]][lives -1].distance = 0
    q.put(MatrixEnd[S[0]][S[1]][lives - 1])
    
    #Check all possible values
    while q.empty() == False:
         u = q.get()
         #print (u.row, u.column, u.lives, u.distance)
         if (u.row + 1 <= height - 1 and MatrixEnd[u.row + 1][u.column][u.lives].visited == False):
            MatrixEnd[u.row + 1][u.column][u.lives].visited = True
            if (MatrixBegin[u.row + 1][u.column] == 'M'):
                if (u.lives - 1 >= 0):
                    MatrixEnd[u.row + 1][u.column][u.lives - 1].visited = True
                    MatrixEnd[u.row + 1][u.column][u.lives - 1].distance = MatrixEnd[u.row][u.column][u.lives].distance + 1
                    q.put(MatrixEnd[u.row + 1][u.column][u.lives - 1])
                    #print("Found Monster when processing at ", u.row, u.column, " with ", u.lives)
            else:
                MatrixEnd[u.row + 1][u.column][u.lives].distance = MatrixEnd[u.row][u.column][u.lives].distance + 1
                q.put(MatrixEnd[u.row + 1][u.column][u.lives])
                      
         if (u.row - 1 >= 0 and MatrixEnd[u.row - 1][u.column][u.lives].visited == False):
            MatrixEnd[u.row - 1][u.column][u.lives].visited = True
            if (MatrixBegin[u.row - 1][u.column] == 'M'):
                if (u.lives - 1 >= 0):
                    MatrixEnd[u.row - 1][u.column][u.lives - 1].visited = True
                    MatrixEnd[u.row - 1][u.column][u.lives - 1].distance = MatrixEnd[u.row][u.column][u.lives].distance + 1
                    q.put(MatrixEnd[u.row - 1][u.column][u.lives - 1])
                    #print("Found Monster when processing at ", u.row, u.column, " with ", u.lives)
            else:
                MatrixEnd[u.row - 1][u.column][u.lives].distance = MatrixEnd[u.row][u.column][u.lives].distance + 1
                q.put(MatrixEnd[u.row - 1][u.column][u.lives])
         if (u.column + 1 <= width -1 and MatrixEnd[u.row][u.column + 1][u.lives].visited == False):
            MatrixEnd[u.row][u.column + 1][u.lives].visited = True
            if (MatrixBegin[u.row][u.column + 1] == 'M'):
                if (u.lives - 1 >= 0):
                    MatrixEnd[u.row][u.column + 1][u.lives - 1].visited = True
                    MatrixEnd[u.row][u.column + 1][u.lives - 1].distance = MatrixEnd[u.row][u.column][u.lives].distance + 1
                    q.put(MatrixEnd[u.row][u.column + 1][u.lives - 1])
                    #print("Found Monster when processing at ", u.row, u.column, " with ", u.lives)
            else:
                MatrixEnd[u.row][u.column + 1][u.lives].distance = MatrixEnd[u.row][u.column][u.lives].distance + 1
                q.put(MatrixEnd[u.row][u.column + 1][u.lives])
           
         if (u.column - 1 >= 0 and MatrixEnd[u.row][u.column - 1][u.lives].visited == False):
            MatrixEnd[u.row][u.column - 1][u.lives].visited = True
            if (MatrixBegin[u.row][u.column - 1] == 'M'):
                if (u.lives - 1 >= 0):
                    MatrixEnd[u.row][u.column - 1][u.lives - 1].visited = True
                    MatrixEnd[u.row][u.column - 1][u.lives - 1].distance = MatrixEnd[u.row][u.column][u.lives].distance + 1
                    q.put(MatrixEnd[u.row][u.column - 1][u.lives - 1])
                    #print("Found Monster when processing at ", u.row, u.column, " with ", u.lives)
            else:
                MatrixEnd[u.row][u.column - 1][u.lives].distance = MatrixEnd[u.row][u.column][u.lives].distance + 1
                q.put(MatrixEnd[u.row][u.column - 1][u.lives])
    maxi = -1;
    for life in range (lives):      
        if (MatrixEnd[E[0]][E[1]][life].distance > maxi):
            maxi = MatrixEnd[E[0]][E[1]][life].distance
    print(maxi)
main();