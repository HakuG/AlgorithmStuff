import sys
import bisect

# Given a list of coupled intervals, find the most cover. 
# For example, (1, 2) and (3, 4) is one set and (2,3) and (4,5) would fit in that set.
# However, (1, 5) (6, 8) would be a cover by itself. 


def main():
    numinter = map(int, raw_input().split())[0]
    a = map(int,raw_input().split())      
    b = map(int,raw_input().split())
    c = map(int,raw_input().split())
    d = map(int,raw_input().split())
    
    # Arr contains (first val, second val) (third val, fourth val)
    
    arr = zip (a,b,c,d)
    
    # Sort according to last value
    arr.sort(key = lambda x : x[3])
    
    # Create weights array in order to create a weighted interval
    weights = [0 for i in xrange(numinter)]
    weights[0] = 1
    
    x = [list() for i in xrange(numinter)]
    
    # For every interval, the weight of the interval is defined by the
    # number of intervals that can fit inside of it. Go through and check 
    # how many arrays can fit inside of it using Weighted Interval Scheduling       
    for j in xrange(numinter):
        pseudoweight = list()
        for i in xrange(j): 
            if (arr[i][0] >= arr[j][1] and arr[i][3] <= arr[j][2]):
                x[j].append(arr[i])
                pseudoweight.append(weights[i])     
        weights[j] = WIS(x[j], pseudoweight) + 1   
    # Do a quick weighted interval scheduling over the entire array with all
    # the weights completely filled out. s
    total = WIS(arr, weights)
    print (total)

# Creates a prev array that takes the ith value and points to the 
# interval that fits right before it
def prev(arr):
    start = [i[0] for i in arr]
    end = [i[3] for i in arr]
    p = []
    for j in xrange(len(arr)):
        i = bisect.bisect_right(end, start[j]) - 1
        p.append(i)
    return p      

# Quick weighted interval scheduling that returns the best way to schedule
# events such that to maximize the cumulative weight    
def WIS(S, weights):
    if (len (weights) == 0):
        return 0;
    prevarr = prev(S)
    l = [0 for i in xrange(len(weights) + 1)]
    l[-1] = 0
    l[0] = weights[0]
    for j in xrange(1, len(S)):
        l[j] = max(weights[j] + l[prevarr[j]], l[j-1])    
    return l[len(S)-1]   
main()                             