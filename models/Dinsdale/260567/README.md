# Growth of ED4 (260567 or 6666666.127365)

Because this is the first in the list, these are my notes on figuring out what is going on!

This strain grows on the following media

Strain | Media | Growth
--- | --- | ---
ED4 | MOPS_NoC_Alpha-D-Glucose | ++
ED4 | MOPS_NoC_L-Glutamine | +
ED4 | MOPS_NoC_D-Galactose | ++
ED4 | MOPS_NoC_Sucrose | +
ED4 | MOPS_NoC_D-Fructose | +
ED4 | MOPS_NoC_Salicoside | +
ED4 | MOPS_NoC_Quinate | ++
ED4 | MOPS_NoC_D-Mannose | +
ED4 | MOPS_NoC_Glycerol | ++
ED4 | MOPS_NoC_D-Glucose | ++
ED4 | MOPS_NoC_D-Glutamic_Acid | +

The base reaction list has 1,190 reactions. The growing models on the three media we have tested to date have:

Media | Number of reactions
--- | ---
MOPS_NoC_D-Glutamic_Acid | 1237
MOPS_NoC_Glycerol | 1270
MOPS_NoC_L-Glutamine | 1232

i.e. we are adding 40-60 reactions per model.

The reactions (beside the initial list) break down as:

MOPS_NoC_D-Glutamic_Acid

Source | Number of reactions
--- | --- 
close_reactions | 35
essential_reactions | 5
media_reactions | 3
orphan_compounds | 2
subsystem_reactions | 3

MOPS_NoC_Glycerol

Source | Number of reactions
--- | --- 
close_reactions | 66
essential_reactions | 6
media_reactions | 4
orphan_compounds | 1
subsystem_reactions | 4

MOPS_NoC_L-Glutamine

Source | Number of reactions
--- | --- 
close_reactions | 30
essential_reactions | 5
media_reactions | 3
orphan_compounds | 1
subsystem_reactions | 4
