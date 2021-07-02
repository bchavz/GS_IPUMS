# Genealogical Searching - IPUMS Family Simulator

###### Written by Berenice Chavez Rojas
###### Rohlfs Lab - Department of Biology at SFSU  

## Input:
CSV file containing years (1850-2000) and number of children. The first row of the data set contains the years, while the columns under each year contain the number of children per family. The file toyIPUMS.csv is a smaller example of the larger data set. 

## Output: 
A graph containing all of the family members in a multigenerational family will be visualized. 
Additionally, a text file that contains the edge list data will be created with the following line of code:  
```
nx.write_edgelist(graph, "edgeList.txt")
```
The edge list text file will contain the parent - child relationship in the following format:  
```
1 3 {}
1 25 {}
```
fam_2kids.txt is a sample edge list file

## General Info: 
This program uses NetworkX, a Python packages that helps create, manipulate and analyze complex graphs and networks. A recursive function is used to add generation to a family pedigree. 

The csv data file is composed of data obtained from IPUMS (Integrated Public Use Microdata Series). IPUMS is a database that provides Census and American Community Survey household composition data. The CSV file is based on the number of kids per family found between the years 1850 - 2000. 
	
## Recursive Function:  
The goal is to simulate multigenerational families using data from IPUMS CSV file.

Function takes graph, parent, current generation (curGen) and final generation (finalGD) as arguments. The graph is a NetworkX MultiDiGraph (a directed graph that is able to store multi-edges), the directionality of the graph prevents the possibility of a child becoming a parent to their own parent(s) as generations are added. 

Recursion is used to add a new generation to the family by increasing curGen by 1. 

Edge list information is saved as a text file that can later be used in the SLiMulation pipeline.

## How to Run 
To run NetworkX library must be imported. If library is not found, use: 
```
pip install networkx
```
The setNum_GS.py file does not use the CSV file, thus the number of kids each parent has must be indicated in the code (kid= )

The user can indicate the current and final generation depth. In the following line the family graph has a final generation depth of 4. 
```
family(graph, parent1, 0, 4)
```

## Files: 
Data Files
1. toyIPUMS - smaller CSV dataset that contains 50 number of children for every year. 
2. IPUMS_data - full dataset 
   - Data from 1850-1990 contain either 1% or 5% sample from CENSUS data.  
   - Data from 2000-2019 contains data samples from ACS (American Community Survey).  

Python Files 
1. setNum_GS.py - number of kids per every two parents is hard coded
2. GS_CreatingFamilies.py - number of kids is random; the program uses CSV data containing IPUMS data 
