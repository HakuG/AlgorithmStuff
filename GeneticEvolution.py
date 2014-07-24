# -*- coding: utf-8 -*-
"""
Created on Thu Jul 03 15:59:44 2014

@author: Harnek Gulati
"""

# CAN = 2
# NOTHING = 0
# WAll = 1
import random
import bisect
import math

size = 10
population = 200
numcans = 50
mrate= .05
generations = 1
wallPoint = 5
canPoint = 10
numSim = 100


# Create Tiles that the Robots go over
class Tile:
    def __init__(self):
        self.item = 0
        self.StrategyValue = 0

		
# Randomly choose a value based on on its weight value
def weighted_choice_b(weights):
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random.random() * running_total
    return bisect.bisect_right(totals, rnd)


	
def main():
    # Create Robots and Maze
	Robots = [[random.randint(1,6) for x in xrange(243)] for y in xrange(population)]  
    Maze = [[Tile() for x in xrange(size + 2)] for y in xrange(size +2)]
    
	# Add Walls
	for i in xrange(size +2):
        for x in xrange(size +2):
            if i == 0 or i == size + 1 or x == 0 or x == size + 1:
                Maze[i][x].item = 1
    # Simulate the Interactions
	for gen in xrange(generations):
        Robots = SimulateActions(gen, population, Robots,Maze)
#

# The numbers defining the direction
#    0 
# 1  2  3
#    4


# Clear the cans in the maze to remake it
def clearCans(Maze):
    for val in Maze:
        for val2 in val:
            if val2.item == 2:
                val2.item = 0


# Return the strategy value based on the position given			
def ScanAround(maze,i,j):
    return maze[i][j+1].item * 1 + maze[i-1][j].item * 3 + maze[i][j].item * 3 * 3 + maze[i+1][j].item * 3 * 3 * 3 + maze[i][j-1].item * 3 * 3 * 3 * 3
        
# Process the StrategyValue of the maze.
def processStrategyValues(maze, size):
    for x in xrange(1,size):
        for y in xrange(1,size):
            maze[x][y].StrategyValue = ScanAround(maze,x,y)


# Mutate the "genetic code" based on the mutation rate			
def Mutate(Robots, mrate):
    for val in xrange(len(Robots)):
        for val2 in xrange(val):
            if (random.random() <= mrate):
                Robots[val][val2] = random.randint(1,6)
    return Robots
      
# Create two children based on two parents that are chosen with 
# a weighted decision
def Sex(averpoints, Robots, numRobot):    
    i = 0.
    newPopulation = list()
    averpoints2 = list()
	
	# Weights are based on ranking, so create an array of integers that
	# increase based on i. To make more efficient, just make this once and
	# make it a global array. But in case you want to make it based on points
	# instead of rankings, keep it this way.
    for val in averpoints:
        averpoints2.append((i*i))
        i = i + 1
	# Create two children that have genetic codes of their parents	
    for x in xrange(population/2):    
        Mom = weighted_choice_b(averpoints2)
        Dad = weighted_choice_b(averpoints2)
        print(averpoints[Mom], math.sqrt(averpoints2[Mom]))
        print(averpoints[Dad], math.sqrt(averpoints2[Dad]))
        point = random.randint(0,242)
        newPopulation.append(Robots[averpoints[Mom][1]][:point] + Robots[averpoints[Dad][1]][point:])
        newPopulation.append(Robots[averpoints[Dad][1]][:point] + Robots[averpoints[Mom][1]][point:])
    # Mutate the new population
	newPopulation = Mutate(newPopulation, mrate)
    return newPopulation

	
# Add Cans to the Maze Randomly	
def AddCansToMaze(maze, numcans, size):
    x = 0
    while (x < numcans):
        i = random.randint(1, size)
        j = random.randint(1, size)      
        if maze[i][j].item == 0:
            x = x + 1
            maze[i][j].item = 2
            
            
    
# 1: North
# 2: East
# 3: West
# 4: South
# 5: Random
# 6: Pick up Can
 
# Do actions based on the genetic code.  
def SimulateActions(gen, numrob, Robots, Maze):    
    averages = list()  
    totalaverage = 0.    
    i = 0
    for robot in Robots:    
        average = 0
        for x in xrange(numSim):
            average = average + SimulateOne(robot,Maze)
        totalaverage = totalaverage + average/numSim    
        averages.append((average/numSim, i))
        i = i + 1
    print(gen, totalaverage/numrob)
    averages = sorted(averages, key = lambda tup: tup[0])
    Robots = Sex(averages, Robots, numrob)
    return Robots
    
# Simulate one round of the maze
def SimulateOne(actions, Maze):
    AddCansToMaze(Maze, numcans, size)  
    processStrategyValues(Maze, size)  
    
	# Drop him at the top left side of the maze.
    xpos = 1
    ypos = 1
    x = 0
    points = 0
    while (x < numSim):
		currentAction = actions[Maze[xpos][ypos].StrategyValue]
        if (currentAction == 1):
            if (Maze[xpos][ypos +1].item == 1):
                points = points - wallPoint
            else:
                ypos = ypos + 1
                
        elif (currentAction == 2):
            if (Maze[xpos + 1][ypos].item == 1):
                points = points - wallPoint
            else:
                xpos = xpos + 1
                
        elif (currentAction == 3):
            if (Maze[xpos - 1][ypos].item == 1):
                points = points - wallPoint
            else:
                xpos = xpos - 1
                
        elif (currentAction == 4):
            if (Maze[xpos][ypos - 1].item == 1):
                points = points - wallPoint
            else:
                ypos = ypos - 1
             
        elif (currentAction == 5):
            y = random.randint(1,4)
            if (y == 1):
                if (Maze[xpos][ypos + 1].item == 1):
                    points = points - wallPoint
                else:
                    ypos = ypos + 1
            if (y == 2):
                if (Maze[xpos + 1][ypos].item == 1):
                    points = points - wallPoint
                else:
                    xpos = xpos + 1
            if (y == 3):
                if (Maze[xpos - 1][ypos].item == 1):
                    points = points - wallPoint
                else:
                    xpos = xpos - 1
            if (y == 4):
                if (Maze[xpos][ypos - 1].item == 1):
                    points = points - wallPoint
                else:
                    ypos = ypos - 1
                
        elif (currentAction == 6):
            if (Maze[xpos][ypos].item == 0):
                points = points - 1
            elif (Maze[xpos][ypos].item == 2):
                points = points + canPoint
                Maze[xpos][ypos].item = 0
                Maze[xpos][ypos].StrategyValue = ScanAround(Maze, xpos, ypos)
        x = x + 1        
    clearCans(Maze)
    return points                
            
        
            
main()  