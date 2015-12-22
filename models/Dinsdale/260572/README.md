# ED139 model (260572 or 6666666.12737)

We have 27 models that we have tested for this genome. 

As we have done [before](../260569/README.md) and [before](../260567/README.md) we will only consider reactions that need to be added to the majority of models.

## Essential reactions

Four essential reactions were added to all models, one was added to 25/27 models. So we add all of those. Again, fe3 and cl- should have been added by media.

Reaction ID | Equation | Protein
--- | --- | ---
rxn05195 | (1) H2O[c] + (1) ATP[c] + (1) fe3[e] <=> (1) ADP[c] + (1) Phosphate[c] + (1) H+[c] + (1) fe3[c] | No roles for this reaction
rxn00392 | (1) ATP[c] + (1) Riboflavin[c] <=> (1) ADP[c] + (1) FMN[c] + (1) H+[c] | Riboflavin kinase (EC 2.7.1.26); FMN adenylyltransferase (EC 2.7.7.2)
rxn01208 | (1) CO2[c] + (1) 4MOP[c] <=> (1) H+[c] + (1) 2-isopropyl-3-oxosuccinate[c] | No roles for this reaction
rxn05116 | (1) H+[c] + (1) 2-Amino-3-oxo-4-phosphonooxybutyrate[c] <=> (1) CO2[c] + (1) 3-Amino-2-oxopropyl phosphate[c] | No roles for this reaction
rxn10473 | (1) Cl-[e] <=> (1) Cl-[c] | Chloride channel protein


## Orphan reactions

One reaction was added to 16/27 reactions:

Reaction ID | Equation | Role associated with reaction
--- | --- | ---
rxn31834 | (1) H2O[c] + (1) 5-Amino-6--5-phosphoribitylaminouracil[c] <=> (1) Phosphate[c] + (1) 4--1-D-Ribitylamino-5-aminouracil[c] | No roles for this reaction

## Close reactions

400 reactions were added in total. 

Number of reactions | Number of models added to
--- | ---
147 | 1
127 | 2
57 | 3
20 | 4
9 | 5
5 | 6
1 | 7
1 | 8
2 | 9
1 | 10
1 | 13
5 | 14
2 | 17
1 | 23
4 | 26
17 | 27

In this case, I'm only going to add reactions that are in >= 13 models (i.e. half) and we'll have to gapfill the rest if necessary.

# Revised model

The initial model had 1,028 reactions. The revised model has 1,065 reactions.

In most of the models, gap filling just based on the media did not result in growth. We had to gap fill based on close genomes too.
