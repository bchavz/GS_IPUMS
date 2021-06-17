# GS_IPUMS

Genealogical Searching - IPUMS Family Simulator 

#### Input:
CSV file containing years (1850-2000) and number of children. 

#### Family Recursive Function:
The goal is to simulate multigenerational families using data from IPUMS CSV file. 

Function takes graph, parent1, current generation (curGen) and final generation (finalGD) as arguments. The graph is a NetworkX MultiDiGraph (a directed graph that is able to store multi-edges), the directionality of the graph prevents the possibility of a child becoming a parent to their own parent(s) as generations are added. 

nx.write_edgelist saves edges as .txt file to later be used in the SLiMulation pipeline.

#### Files: 

1. toyIPUMS - smaller CSV dataset that contains 50 number of children for every year. 
2. IPUMS_data - full dataset 

  Data from 1850-1990 contain either 1% or 5% CENSUS sample. Data from 2000-2019 contains data samples from ACS (American Community Survey).  

