#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 17:04:20 2021

@author: berenice
"""

#import csv
#import numpy as np
#import random
import networkx as nx
import matplotlib.pyplot as plt

index= 1
parent1 = index 

graph = nx.MultiDiGraph() #set graph

curPer = 1

def family(graph, parent1, curGen, finalGD):
    global curPer
    
    if(curGen >= finalGD):
        return()
    
    print ("running fam, parent1:", parent1, "curPer:", curPer)
    print ("curGen", curGen)
    
    kid=2 # 2 kids per set of parents 
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
            
            family(graph, child, curGen+1, finalGD) #recursion; adds a new generation

    nx.draw(graph,with_labels=True, font_weight='bold')
    plt.show()
    graph.edges(data=True)
    return

family(graph, parent1, 0, 4)

#save edge list
nx.write_edgelist(graph, "fam_jun17.txt")
