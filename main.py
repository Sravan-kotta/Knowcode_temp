from speciestrack import species
from speciestrack import endangered_species
from ete3 import NCBITaxa
import requests

list = species(latitude = 21.32,longitude = 89.00,radius = 100)
print(list)
for i in list:
    x = i.split(" ")
    if len(x) == 1:
        ncbi = NCBITaxa()
        desc = ncbi.get_descendant_taxa(x[0])
        species = ncbi.translate_to_names(desc)[1]
        x = species.split(" ")
    gen = x[0]
    spe = x[1]
    
        
    y = endangered_species(gen, spe)
    print(i)
    print(y)