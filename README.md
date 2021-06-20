# Genealogical Searching - IPUMS Family Simulator


Written by Berenice Chavez Rojas.

Rohlfs Lab - Department of Biology at SFSU.  

**Input:**
CSV file containing years (1850-2000) and number of children. 
 ** give more detail on rows and columns, labels
 ** example file -> toydata

** Output: **
 ** explain what output will be:
	-pedigree
	- text file with parent - child relationship (explain what rows and columns are) -> example file

** General Info: **
This program uses NetworkX, a Python packages that helps create, manipulate and analyze complex graphs and networks. A recursive function is used to add generation to a family pedigree. 
	uses networkx and incorporate recursive function

** Family Recursive Function: **
The goal is to simulate multigenerational families using data from IPUMS CSV file.
 *what is the data 
	*based on sib sizes from historical data  

Function takes graph, parent1, current generation (curGen) and final generation (finalGD) as arguments. The graph is a NetworkX MultiDiGraph (a directed graph that is able to store multi-edges), the directionality of the graph prevents the possibility of a child becoming a parent to their own parent(s) as generations are added. 

Recursion is used to add a new generation to the family by increasing curGen by 1. 

nx.write_edgelist saves edges as a text file to later be used in the SLiMulation pipeline.

** how to run **
  #how does the user run the data (command line, specific #of child, etc) 


** Files: **
Data Files
1. toyIPUMS - smaller CSV dataset that contains 50 number of children for every year. 
2. IPUMS_data - full dataset 
   - Data from 1850-1990 contain either 1% or 5% sample from CENSUS data.  
   - Data from 2000-2019 contains data samples from ACS (American Community Survey).  

Python Files 
