import sys
import heapq

# Given a set of intervals, what is smallest number of sequences that use
# all the intervals without overlapping sequences?

def main():
   
    # Obtain size and tuple start and ends
    size = map(int, raw_input().split())
    tuple1 = map(int, raw_input().split())
    tuple2 = map(int, raw_input().split())
    
    # Create tuple array
    tuples = [0 for rows in xrange(size[0])]
    
    # Form the array that has the tuples
    for num in xrange(size[0]):
        tuples[num] = (tuple1[num], tuple2[num])
    # Sort the tuple by starting element    
    stuples = sorted(tuples, key = lambda tup: tup[0])
    
    # Create a heap that will hold the maxes of each possible interval, with the
    # minimum of the maxes at the top of the heap
    x = []
    heapq.heappush(x, float("inf"))
    y = 0
    
    # For each value in stuples, check if the first value is greater than the 
    # minimum of all the maxes, in which case add b, the end value, as the the new max.
    # The push will automatically sort it and change it so the new minimum is at the 
    # top of the heap in log (n) time. 
    # If the first value of a is not bigger than the second value of b, then it must create
    # a new sequence of intervals, and hence y is added and a new value is added to the heap.
    for val in stuples:
        (a,b) = val
        minmax = heapq.heappop(x)   
        if (a >= minmax):
            heapq.heappush(x, b)
        else:
            y = y + 1
            heapq.heappush(x, b)
            heapq.heappush(x, minmax)
    print(y)
main()    