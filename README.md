# kernel-Blau-Isingmodel
Data cleaning and code for the KBI model in the article "Inference and Influence of Large-Scale Social Networks Using Snapshot Population Behaviour without Network Data". Collected datasets in here are publily available, you can find the url in the readme file. The codes is written in Pypy (a Python interpreter)---you can use python just changing 'import _numpypy as np' by 'import numpy as np'. 

Program >parsedata.py parses de original files to generate clean files:

ME16-12_sociodemographics.dat	:2012 and 2016 Mayoral Elections data at ward level (608wards) together with socio-demographic data

EUwards.dat	:EUreferendum data at ward level (only 280wards are given at ward level)

ME16-12EUBoroughs.dat	:2012 and 2016 Mayoral Elections and EUreferendum outcomes at Borough level

The KBIcode.py program generates spin configuration from a parameter set (paramters are randomly generated acording to uniform priors) and computes "distance measures" (Eq.7 in the manuscript) from the generated spins configuration to the original electoral outcomes in Greater London for 2012 and 2016 Mayoral Elections and 2016 EU referendum. The output file 'parameters.dat' includes: distances for the three elections and for different spatial aggregation (608wards, 280wards, 18Boroughs, 280wards+18Boroughs) and model paramters. Outcome file 'paramters.dat' includes outcomes where the generated network has a average dregree smaller than 6 (the algorithm is less efficient generating spin cofigurations with very large average degree, but this can be modified in line 200 in the KBIcode.py code). The ABC posteriors can be produced a porteriory by seting and ABC thershold \epsilon (algorithm1 in the article) given that all spins configurations are independent. This program is created to be distributed in a High-performance computing (HPC).
