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

## MOPS_NoC_D-Glutamic_Acid

Source | Number of reactions
--- | --- 
close_reactions | 35
essential_reactions | 5
media_reactions | 3
orphan_compounds | 2
subsystem_reactions | 3

## MOPS_NoC_Glycerol

Source | Number of reactions
--- | --- 
close_reactions | 66
essential_reactions | 6
media_reactions | 4
orphan_compounds | 1
subsystem_reactions | 4

## MOPS_NoC_L-Glutamine

Source | Number of reactions
--- | --- 
close_reactions | 30
essential_reactions | 5
media_reactions | 3
orphan_compounds | 1
subsystem_reactions | 4


# A unified model

We can probably include the essential_reactions and orphan_compound reactions in our revised model essentially as-is. They are probably going to be required. We need to figure out (of course), which reactions are required and why, but that is for a slightly later date.

## Essential reactions

There are 6 essential reactions that we have included in these models:

Reaction ID | Equation | Role associated with reaction
--- | --- | ---
rxn05319 | (1) H2O[e] <=> (1) H2O[c] | No roles for this reaction
rxn00392 | (1) ATP[c] + (1) Riboflavin[c] <=> (1) ADP[c] + (1) FMN[c] + (1) H+[c] | Riboflavin kinase (EC 2.7.1.26); FMN adenylyltransferase (EC 2.7.7.2)
rxn01208 | (1) CO2[c] + (1) 4MOP[c] <=> (1) H+[c] + (1) 2-isopropyl-3-oxosuccinate[c] | No roles for this reaction
rxn05116 | (1) H+[c] + (1) 2-Amino-3-oxo-4-phosphonooxybutyrate[c] <=> (1) CO2[c] + (1) 3-Amino-2-oxopropyl phosphate[c] | No roles for this reaction
rxn05195 | (1) H2O[c] + (1) ATP[c] + (1) fe3[e] <=> (1) ADP[c] + (1) Phosphate[c] + (1) H+[c] + (1) fe3[c] | No roles for this reaction
rxn10473 | (1) Cl-[e] <=> (1) Cl-[c] | Chloride channel protein


Five of the six are added to all models, and only rxn05319 is added to a single model. We added all six to the model. We should always add rxn05319!

This suggests that we should check media before we check essentials, and all media should add H2O[e] to the media!

## Orphan compounds

We add one reaction for orphan compounds (rxn30766) to all three models and one reaction (rxn07614) to a single model. The two reactions we added are:

Reaction ID | Equation | Role associated with reaction
--- | --- | ---
rxn30766 | (1) 5-Amino-6--5-phosphoribitylaminouracil[c] <=> (1) Phosphate[c] + (1) 4--1-D-Ribitylamino-5-aminouracil[c] | No roles for this reaction
rxn07614 | (1) H2O[c] <=> (1) Glucuronate[c] | No roles for this reaction

**Note:** The second reaction creates Glucuronate ... i.e. we are cheating! This should not be allowed!

We only add the first reaction to our model.

## Subsystem reactions

Reaction ID | Equation | Role associated with reaction
--- | --- | ---
rxn00548 | (1) Phosphate[c] + (1) D-fructose-6-phosphate[c] <=> (1) H2O[c] + (1) Acetylphosphate[c] + (1) D-Erythrose4-phosphate[c] | Fructose-6-phosphate phosphoketolase (EC 4.1.2.22)
rxn05216 | (1) L-Glutamine[e] + (1) Na+[e] <=> (1) L-Glutamine[c] + (1) Na+[c] | Sodium/glutamine symporter glnT
rxn00501 | (1) NAD[c] + (1) CoA[c] + (1) 3-Oxopropanoate[c] <=> (1) NADH[c] + (1) CO2[c] + (1) Acetyl-CoA[c] | Methylmalonate-semialdehyde dehydrogenase (EC 1.2.1.27); Methylmalonate-semialdehyde dehydrogenase [inositol] (EC 1.2.1.27)
rxn00656 | (1) L-Alanine[c] + (1) 3-Oxopropanoate[c] <=> (1) Pyruvate[c] + (1) beta-Alanine[c] | Omega-amino acid--pyruvate aminotransferase (EC 2.6.1.18)
rxn01256 | (1) Chorismate[c] <=> (1) Prephenate[c] | Periplasmic chorismate mutase I precursor (EC 5.4.99.5); Chorismate mutase (EC 5.4.99.5); Chorismate mutase III (EC 5.4.99.5); Chorismate mutase II (EC 5.4.99.5)

**Note:** This revealed a bug in the way the media was being parsed: why wasn't L-Glutamine being imported as a media suggestion? I fixed that error, we should not currently add it as a subsystem reaction, but we should add it as a media import reaction!

We add the three reactions that are added to every model to our model: rxn00501, rxn00656, rxn01256

## Close genomes

There are 54 reactions added to one of the three models because of close genomes, 7 reactions added to two of three models, and 21 reactions to all three models from the close genomes.

- [ ] TODO: check all the conditions and see whether adding reactions in 1, 2, or 3 close genomes is most accurate. (For now, we added reactions in all three genomes)

# Revised model

Our revised model now has 1,282 reactions in it. We can repeat the gap filling on the 11 conditions where things should grow because we now have a better model (so the gap filling should be a lot quicker!).

In nine out of eleven models we get growth by just gap filling the media. In the two other cases (MOPS_NoC_Quinate and MOPS_NoC_Salicoside) we had to go to the orphan compounds to get growth.

This makes the model resolution go very quickly - the orphan compounds were only a single reaction so they get resolved in a single step.

