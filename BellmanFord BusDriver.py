import sys

# Given a list of towns, the towns it can reach, the amount of money burned going from city 
# to city, and the approximate amount of money achieved when reaching the town, what is the
# path that will maximize the amount of money a bus driver will receive. 

def main():

    # Obtain information
    towns, edges = map(int, raw_input().split())
    townweight = map(int, raw_input().split())
    
    # Change weight of edges by adding the money of the cities to the negative of the 
    # amount of money burned by going from one city to another. Add this to an adjacency list
    weight = list()
    for value in xrange(edges):
        (start, end, weight) = map(int, raw_input().split())
        weight.append((start - 1, end - 1, townweight[end - 1] - weight))
    
    # Set up the starting and other towns to prepare to use BellmanFord.    
    distance = [0 for rows in xrange(towns)]
    for town in xrange(towns):
       if town == 0:
        distance[town] = townweight[0]
       else:
        distance[town] = float("-inf")   
         
    BellmanFord(weight, distance)     
    
# Returns the maximum weight as we use Bellman Ford to find the shortest distance, but
# using maximums instead of minimums to find the highest value.
def BellmanFord (weights, distances):

   # Fill up the distances array. "distance" will only increase if there exists a way to go
   # to the town another way that increases the "distance" or "money received" at that time.
   for val in xrange(len(distances) - 1):
       for edge in weights:
           (start, end, weight) = edge
           if distances[start] + weight > distances[end]:
               distances[end] = distances[start] + weight

   # Check if the end value changes, or if there exists a negative loop that the bus driver 
   # could take to make an infinite amount of money given enough time 
   prev = distances[len(distances) -1]
   
   found = False
   
   #Check if there even is a way to get to the last town
   if (prev == float("-inf")):
    print("none")
    return
    
   # Run Bellman Ford one more time to check if any values change
   # If they do, then there exists a loop somewhere.
   for edge in weights:
       if distances[edge[0]] + edge[2] > distances[edge[1]]:
        distances[edge[1]] = distances[edge[0]] + edge[2]
        found = True
        break
   
   # If there is a loop, check if the loop leads to the end
   # town. If it does not reach the end town, check if the end town changes 
   # its value. If it doesn't change value, then the loop is net zero. 
   # If it does reach the end town, print out infinity.    
   if found:
        if DFS(weights, foundedge[1], distances) == False:
            if prev != distances[len(distances) -1]:
                print("infinity")   
                return
        else:
            print("infinity")  
            return    
   print(prev)

# Just a quick DFS
def DFS (weights, v, distances):
    visited = [False for rows in xrange(len(distances))]
    s = list()
    s.append(v)
    while (len(s) > 0):
        vec = s.pop() 
        if visited[vec] == False:
            visited[vec] = True
            for edge in weights:
                (x,y,z) = edge
                if x == vec:
                    s.append(y)
                    if y == len(distances) - 1:
                        return True
    return False
main()