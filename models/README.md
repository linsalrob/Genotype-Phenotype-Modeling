# Models for various projects!

I have built some models for different projects, and this also shows us where we stand with PyFBA and the modeling. 

All of this is working on anthill, but you will need to install glpk and gmp from source. I'm working on getting it
installed widely.

## Genotype-phenotype models

I have models for 13 different organisms that we have sequences for, and the success rate is mixed!

Genome ID | TP | TN | FP | FN
--- | --- | --- | --- | --- 
260567 | 11 | 20 | 65 | 0
260569 | 20 | 20 | 56 | 0
260572 | 25 | 13 | 54 | 4
260573 | 50 | 0 | 46 | 0
260574 | 42 | 0 | 54 | 0
260575 | 43 | 0 | 53 | 0
260576 | 12 | 19 | 65 | 0
260578 | 43 | 0 | 53 | 0
260581 | 24 | 0 | 72 | 0
278833 | 0 | 70 | 0 | 2
278834 | 8 | 19 | 69 | 0
278835 | 48 | 0 | 48 | 0
278836 | 20 | 15 | 60 | 1

Notice how the false positive rate is way too high - we are predicting growth in conditions where it should not occur. 
I suspect that this reflects an over-ambitious gap filling, especially in the import reaction side of things. 

I wrote PyFBA.gapgeneration.test_reactions.py which will identify which reactions are essential for growth and which 
are not. This uses an algorithm that in the best case would be theta(log n) but in reality is somewhere between O(n) and 
omega(log n) where n is the number of essential reactions. 

For one model (260572) I ran this for all gap-filled reactions (including those for which the model should not grow), 
and most reactions are *not* essential, and most of those that *are* essential are essential in every model:

### Reactions that are/are not essential

 * Essential reactions: 141
 * Redundant reactions: 1,206
 * Total reactions: 




I haven't figured out a way to trim out the over-exuberant gap filling yet. That remains to be done!
