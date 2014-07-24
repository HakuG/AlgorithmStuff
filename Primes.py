# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 13:46:35 2014

@author: Harnek Gulati
"""

# The problem was to take a list of integers in an array and obtain the 
# maximum number of pairs whose sum is a prime number. We use Max Flow
# in order to solve this problem. 

def main():
    m, n = map(int, raw_input().split())
    primes = get_primes(2*m)
    Inters = map(int, raw_input().split())
    odd = list()
    even = list()
    Adj = [list() for x in xrange(m + 2)]
    capacity = dict()
	
	# Create a dually paired list, evens on the left side, 
	# odds on the right. 
    for val in Inters:
        if val % 2 == 1:
            odd.append(val)
        else:
            even.append(val)
    # Connect odds to the source
	for val in odd:
        Adj[-1].append(val)
        capacity[translate(-1, val)] = 1
    # Connect evens to the sink
	for val in even:
        Adj[val].append(-2)
        capacity[translate(val, -2)] = 1
    for valod in odd:
        for valev in even:
            if (valod + valev) in primes:
                Adj[valod].append(valev)
                Adj[valev].append(valod)
                capacity[translate(valod, valev)] = 1
                capacity[translate(valev, valod)] = 0
    flow = 0
	# Run the maxFlow
    while True:
        paths = dfs_paths(Adj, capacity, -1, -2)
        if (len(paths)) == 0:
            break
        
        
        c = list();
        for i in xrange(0, len(paths) -1):
            x = capacity[translate(paths[i], paths[i+1])]
            c.append(x)        
        minimum = min(c)
        flow = flow + minimum
        dummy = 0
        for i in xrange(0, len(paths) -1):
            capacity[translate(paths[i],paths[i+1])] -= minimum
            if (paths[i] != -1 or paths[i]!= -2) or (paths[i+1] != -1 or paths[i+1] != -2):
                dummy = 0             
            else:
                capacity[translate(paths[i+1], paths[i])] += minimum
    print(flow)            
    
# Get all the prime numbers up until a specific value    
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

# Basically hashing    
def translate(a, d):
    return str(a).zfill(4) + str(d).zfill(4)    
# Check if there even exists a prime number by doing a DFS    
def startingcheck_dfs(g, start, path = []):  
    path= path+[start]
    for node in g[start]:
        if not node in path:
            path = startingcheck_dfs (g, node, path)
    return path

# Same DFS, but with a start and a goal, using capacities as a 
# way to see if the capacity can go back. 
def dfs_paths(graph, cap, start, goal):    
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex]:
            if next not in path and cap[translate(vertex, next)] > 0:                
                if (next == goal):    
                    return path + [next]
                else:
                    stack.append((next, path + [next]))
    return [] 
main()