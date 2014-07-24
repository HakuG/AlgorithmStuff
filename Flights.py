# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\User Name\.spyder2\.temp.py
"""
# Given a list of cities with certain connections, and 
# flights given certain times it takes to get from one 
# city to another, what is the time where it gets
# a certain amount of people from the east coast
# to the west coast.

# We take this as a Max Flow Problem in order to work with it
def main():
    citynum, ecity, wcity, connum = map(int, raw_input().split())
    eastcities = map(int, raw_input().split())
    eastcitpop = map(int, raw_input().split())
    westcities = map(int, raw_input().split())
	
	# Create an Information List that holds the capacity and hour of a connection
    InformationList = [[(0,0) for x in xrange(citynum)] for x in xrange(citynum)]
    
	# Set up an adjacency list, origins, destinations, capacities, and hours
	AdjacencyList = [list() for x in xrange(citynum +2)]
    origins = [0 for x in xrange(connum)]
    destinations = [0 for x in xrange(connum)]
    capacities = [0 for x in xrange(connum)]
    hours = [0 for x in xrange(connum)]
    AdjacencyList[citynum] = eastcities
	# Fill up arrays and set up origin and destination
	for x in xrange(connum):
        origin, destination, capacity, hour = map(int, raw_input().split())
        origins[x] = origin
        destinations[x] = destination
        capacities[x] = capacity
        hours[x] = hour
        InformationList[origin][destination] = (capacity, hour)
        AdjacencyList[origin].append(destination)
    check = False
    
	#Set up the first cities
    for i in westcities:
        AdjacencyList[i].append(citynum + 1)
    for val in eastcities:
        if (citynum +1) not in startingcheck_dfs(AdjacencyList, val):   
            check = True
            break
    # If there is not a way to get to the east cities from the westcities
	# return -1.
	if (check == True):
        print -1
        return
    
	# Create a time graph for 25. 
	for t in range(1, 25):
        if (createGraph(t, hours, citynum, connum, eastcities, westcities, capacities, eastcitpop, origins, destinations)):
            print (t-1)
            break

# Create a graph, creating a new node for every hour that goes by.			
def createGraph(t, times, citynum, flights, eastcities, westcities, capacities, eastcitypop, origin, destinations):    
    graph = [[list() for j in range(t)] for i in range(citynum + 1)]
    cap = dict()
    superstart = (citynum, 0)
    supersink = (citynum, t - 1)
    
    for i in range(flights):
        for j in range(t - times[i]):
            a = origin[i]
            b = destinations[i]
            c = times[i]
            d = capacities[i]
            graph[a][j].append((b, j + c))
            graph[b][j+c].append((a, j))
            cap[translate(a, j, b, j+c)] = d
            cap[translate(b, j + c, a, j)] = 0
    for i in range(citynum):
        for j in range(t - 1):
            graph[i][j].append((i, j+1))
            graph[i][j+1].append((i,j))
            cap[translate(i, j, i, j + 1)] = 9999 
            cap[translate(i, j+1, i, j)] = 0
    for i in range(len(eastcities)):
        graph[citynum][0].append((eastcities[i], 0))
        cap[translate(citynum, 0, eastcities[i], 0)] = eastcitypop[i]
    
    for i in range(len(westcities)):
        graph[westcities[i]][t-1].append((citynum, t-1))
        cap[translate(westcities[i], t-1, citynum, t-1)] = 9999
    
    flow = 0
	# Run Fold-Fulkerson
    while True:
        paths = dfs_paths(graph, cap, superstart, supersink)
        if (len(paths)) == 0:
            break
        
        
        c = list();

        for i in xrange(0, len(paths) -1):
            x = cap[translate(paths[i][0], paths[i][1], paths[i+1][0], paths[i+1][1])]
            c.append(x)        
        minimum = min(c)
        flow = flow + minimum    
        for i in xrange(0, len(paths) -1):
            a = paths[i][0]
            b = paths[i][1]
            c = paths[i+1][0]            
            d = paths[i+1][1]
            cap[translate(a,b,c,d)] -= minimum
            if (a != citynum and c != citynum):
                cap[translate(c,d,a,b)] += minimum
    if (flow == sum(eastcitypop)):
        return True
    else:
        return False
    
# Hash Table
def translate(a, b, c, d):
    return str(a).zfill(3) + str(b).zfill(3) + str(c).zfill(3) + str(d).zfill(3)    
 
# Check if there exists a path 
def startingcheck_dfs(g, start, path = []):  
    path= path+[start]
    for node in g[start]:
        if not node in path:
            path = startingcheck_dfs (g, node, path)
    return path

# Create that path. 
def dfs_paths(graph, cap, start, goal):    
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex[0]][vertex[1]]:
            if (next[0], next[1]) not in path and cap[translate(vertex[0], vertex[1], next[0], next[1])] > 0:                
                if (next == goal):    
                    return path + [next]
                else:
                    stack.append((next, path + [next]))
    return [] 
main()

