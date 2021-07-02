#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 17:04:20 2021

@author: berenice
"""

import csv
import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt

cols=[]
#create a dictionary from CSV file where Keys = years and Values = number of children
with open('toyIPUMS.csv') as f: 
    reader =csv.reader(f)
    for row in reader:
        if cols:
            for i, value in enumerate(row):
                cols[i].append(value)        
        else:
            cols=[[value] for value in row]
dictionary={c[0]:c[1:] for c in cols}
#print(dictionary)  
    
year=random.choice(list(dictionary.keys())) #pick random year for keys (aka years)
#print(year)

numberKids=random.choice(list(dictionary.values())) #pick random year for keys (aka number of children)
# NOTE: (I think) it picks a random value from all the values in the dictionary 
#print (childNum)

index= 1
parent1 = index 

graph = nx.MultiDiGraph() #set graph

curPer = 1

def family(graph, parent1, curGen, finalGenDepth):
    global curPer
    
    if(curGen >= finalGenDepth):
        return()
    
    print ("running fam, parent1:", parent1, "curPer:", curPer)
    print ("curGen", curGen)
    
    randomK= random.choice(numberKids)
    #edits to be made: 
        #choose random choice from year that corresponds to curGen
        #random choice dictionary name and year of curGen 
        #chosen year can be hard coded 
    
    kid=int(randomK) #random number of kids 
    print("kid #:",kid)
    
    parent2 = curPer +1
    curPer= curPer+1
    print("parent2/curPer:", curPer)
    
    for i in range(0, kid):
            child=curPer+1
            curPer = curPer + 1
            
            graph.add_edge(parent1, child)  #edge between parent1 and child (curPer)
            print ("p1 + kid:", parent1, child)
            
            graph.add_edge(parent2, child)
            print ("p2 + kid:", parent2, child)
            
            family(graph, child, curGen+1, finalGenDepth) #recursion: adds a new generation

    nx.draw(graph,with_labels=True, font_weight='bold')
    plt.show()
    graph.edges(data=True)
    return

family(graph, parent1, 0, 1)

nx.write_edgelist(graph, "FamEdgeList.txt") #save edge list
