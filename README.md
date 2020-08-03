# kernel-Blau-Isingmodel
Data cleaning and code for the KBI model in the article "Inference and Influence of Large-Scale Social Networks Using Snapshot Population Behaviour without Network Data". Collected datasets in here are publicly available, urls can be found in 'details.txt' file. The codes are written in Pypy (a Python interpreter)---you can use python just changing 'import _numpypy as np' by 'import numpy as np'. 

Program >parsedata.py parses de original files to generate clean files: (i) ME16-12_sociodemographics.dat --2012 and 2016 Mayoral Elections data at ward level (608wards) together with socio-demographic data--, (ii) EUwards.dat --EUreferendum data at ward level (only 280wards are given at ward level)--, and (iii) ME16-12EUBoroughs.dat --2012 and 2016 Mayoral Elections and EUreferendum outcomes at Borough level (see details.txt)

The KBIcode.py program generates spin configuration from a parameter set (parameters are randomly generated according to uniform priors) and computes "distance measures" (Eq.2 in the article) from the generated spins configuration to the original electoral outcomes in Greater London for 2012 and 2016 Mayoral Elections and 2016 EU referendum. The output file 'parameters.dat' includes: distances for the three elections and for different spatial aggregation (608wards, 280wards, 18Boroughs, 280wards+18Boroughs) and parameter set. Outcome file 'parameters.dat' includes outcomes where the generated network has a average degree smaller than 6 (the algorithm is less efficient generating spin configurations with very large average degree, but this can be modified in line 200 in the KBIcode.py code). Also, for each parameter set the program generates three files with the corresponding spin configurations ME16config_x.dat ME12config_x.dat and EUrconfig_x.dat, where 'x' is ID of parameter set. The ABC posteriors can be produced a posteriory by setting an ABC threshold \epsilon (algorithm1 in the article) given that all spins configurations are independent. This program is created to be distributed in a High-performance computing (HPC).
