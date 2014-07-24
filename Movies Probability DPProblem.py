import sys

# Given a sequence of Movies Ratings of two people, what is the probability that 
# Alice picks "split" amount of movies and has more than or equal to 
# twice the cumulative rating of Bob, who also picks "split" amount of movies. 

def main():
    size, split, maxnum = map(int, raw_input().split())
    Alice = map(int, raw_input().split())
    Bob = map(int, raw_input().split())
    
    # Create a matrix of size where the length is the highest possible cumulative number
    # and the height is the amount of different ratings possible for Dynamic Programming
    matrixA = [[0 for rows in xrange(split* maxnum + 1)] for col in xrange(split)]
    matrixB = [[0 for rows in xrange(split* maxnum + 1)] for col in xrange(split)]
    matrixA = rec(size, split, matrixA, Alice)
    matrixB = rec(size, split, matrixB, Bob)
    compare(matrixA[split-1], matrixB[split-1])

# Compare the two matrices and using basic probability, figure out the probability
def compare(listA, listB):
    listA = [x*1/float(sum(listA)) for x in listA]
    listB = [x*1/float(sum(listB)) for x in listB]
    p = 0
    for i in xrange(len(listA)):
        for j in xrange(len(listB)):
            if (2*i >= j):
                p = p + listA[i]*listB[j]
    print ("%.8f" % p)           

# Recursively go through and do dynamic programming, checking if f(n+1) = f(n) + previous 
# values, using the integer knapsack problem as a model
def rec(size, split, matrixA, Alice):
    for n in xrange(size):
        for j in range(split - 2, -1, -1):
            for i in xrange(len(matrixA[j])):
                if (matrixA[j][i] != 0):
                   matrixA[j+1][i + Alice[n]] += matrixA[j][i]
        matrixA[0][Alice[n]] += 1
    return matrixA  
main()