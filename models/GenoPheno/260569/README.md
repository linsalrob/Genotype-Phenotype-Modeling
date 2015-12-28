# Growth of ED8 (260569 or 6666666.127367)

This strain can grow on 20 different conditions:

Strain | Media | Growth
--- | --- | ---
ED8 | MOPS_NoN_Glycine | +++
ED8 | MOPS_NoC_Propionate | +
ED8 | MOPS_NoC_L-Glutamine | +
ED8 | MOPS_NoC_Malic_Acid | +
ED8 | MOPS_NoC_Alpha-D-Glucose | ++
ED8 | MOPS_NoC_D-Xylose | ++
ED8 | MOPS_NoC_Cellobiose | +++
ED8 | MOPS_NoC_L-Sorbose | ++
ED8 | MOPS_NoC_D-Galactose | ++
ED8 | MOPS_NoC_Salicoside | +
ED8 | MOPS_NoC_Sucrose | ++
ED8 | MOPS_NoC_D-Fructose | ++
ED8 | MOPS_NoC_Erythritol | ++
ED8 | MOPS_NoC_D-Mannose | ++
ED8 | MOPS_NoC_Quinate | +++
ED8 | MOPS_NoC_Glycerol | ++
ED8 | MOPS_NoC_D-Glucose | ++
ED8 | MOPS_NoC_Adonitol | ++
ED8 | MOPS_NoC_L-Arabitol | ++
ED8 | MOPS_NoC_4-Hydroxy-Phenylacetate | +


We have 8 growth conditions where we have built models:

### MOPS_NoC_Adonitol.txt

Media | Number of reactions
--- | ---
close_reactions | 39
essential_reactions | 6
media_reactions | 5
orphan_compounds | 1
subsystem_reactions | 2

### MOPS_NoC_D-Fructose.txt

Media | Number of reactions
--- | ---
close_reactions | 49
essential_reactions | 6
media_reactions | 3
orphan_compounds | 1
subsystem_reactions | 2

### MOPS_NoC_D-Galactose.txt

Media | Number of reactions
--- | ---
close_reactions | 39
essential_reactions | 10
media_reactions | 3
orphan_compounds | 3
subsystem_reactions | 2

### MOPS_NoC_D-Mannose.txt

Media | Number of reactions
--- | ---
close_reactions | 38
essential_reactions | 5
media_reactions | 3
orphan_compounds | 1
subsystem_reactions | 2

### MOPS_NoC_D-Xylose.txt

Media | Number of reactions
--- | ---
close_reactions | 44
essential_reactions | 6
media_reactions | 5
orphan_compounds | 1
subsystem_reactions | 2

### MOPS_NoC_Glycerol.txt

Media | Number of reactions
--- | ---
close_reactions | 39
essential_reactions | 7
media_reactions | 4
orphan_compounds | 1
subsystem_reactions | 2

### MOPS_NoC_Propionate.txt

Media | Number of reactions
--- | ---
close_reactions | 36
essential_reactions | 5
media_reactions | 3
orphan_compounds | 3
subsystem_reactions | 2

### MOPS_NoC_Salicoside.txt

Media | Number of reactions
--- | ---
close_reactions | 42
essential_reactions | 7
media_reactions | 4
orphan_compounds | 3
subsystem_reactions | 2


## Essential reactions

Among the essential reactions, 5 reactions are in all 8 models, so we just add those immediately:

Reaction ID | Equation | Protein
--- | --- | ---
rxn00392 | (1) ATP[c] + (1) Riboflavin[c] <=> (1) ADP[c] + (1) FMN[c] + (1) H+[c] | Riboflavin kinase (EC 2.7.1.26); FMN adenylyltransferase (EC 2.7.7.2)
rxn01208 | (1) CO2[c] + (1) 4MOP[c] <=> (1) H+[c] + (1) 2-isopropyl-3-oxosuccinate[c] | No roles for this reaction
rxn05116 | (1) H+[c] + (1) 2-Amino-3-oxo-4-phosphonooxybutyrate[c] <=> (1) CO2[c] + (1) 3-Amino-2-oxopropyl phosphate[c] | No roles for this reaction
rxn05195 | (1) H2O[c] + (1) ATP[c] + (1) fe3[e] <=> (1) ADP[c] + (1) Phosphate[c] + (1) H+[c] + (1) fe3[c] | No roles for this reaction
rxn10473 | (1) Cl-[e] <=> (1) Cl-[c] | Chloride channel protein

Two of these (Cl- and fe3) should have been added in media import, but that was screwed up ([see elsewhere](../260567/README.md) but has been fixed.

## Orphan compunds

One of the orphan compound reactions (rxn30766) was in 6 models, and two (rxn08042 and rxn22768) are each in 3 models:

Reaction ID | Equation | Protein
--- | --- | ---
rxn30766 | (1) 5-Amino-6--5-phosphoribitylaminouracil[c] <=> (1) Phosphate[c] + (1) 4--1-D-Ribitylamino-5-aminouracil[c] | No roles for this reaction
rxn08042 | (1) N-Acetyl-D-glucosamine[c] <=> (1) N-Acetyl-D-glucosamine[e] | No roles for this reaction
rxn22768 | (1) H2O[c] <=> (1) Chitobiose[c] | No roles for this reaction

## Subsystem reactions

Only two reactions were added because of their presence in subsystems, but both were added to all 8 models:

Reaction ID | Equation | Protein
--- | --- | ---
rxn00346 | (1) L-Aspartate[c] + (1) H+[c] <=> (1) CO2[c] + (1) beta-Alanine[c] | Aspartate 1-decarboxylase (EC 4.1.1.11)
rxn01256 | (1) Chorismate[c] <=> (1) Prephenate[c] | Periplasmic chorismate mutase I precursor (EC 5.4.99.5); Chorismate mutase (EC 5.4.99.5); Chorismate mutase III (EC 5.4.99.5); Chorismate mutase II (EC 5.4.99.5)

## Close genomes

126 different reactions were added from the close genomes. Most of these are only in one model (which perhaps suggests that they are just needed in that specific environment?)

Number of reactions | Number of models added to
--- | ---
69 | 1
25 | 2
7 | 3
2 | 4
2 | 5
21 | 8

(i.e. 69 reactions were added to a single model, 25 reactions were added to two models, .... and 21 reactions were added to all 8 models).

As before, we add all of these, but under advisement that we should trim them to just the right number for optimal growth!

# Revised model

The revised model has 1,296 reactions. Again, we test all growth conditions. For all 20 models we only need to gap fill from the media.


