# Models for the Genotype Phenotype project

These models are all built for the SDSU genotype phenotype project, and cover the genomes that we are sequencing. 

We have [predicted growth](growth_predictions.md) of 14 different strains on 97 different media (1,225 predictions in total) and we have used these to build models of the different genomes. 

I have taken a look at a few different gap filling tries:

 - [x] [ED139](260572/README.md)
 - [x] [ED4](260567/README.md)
 - [x] [ED144](260573/README.md)
 - [x] [ED8](260569/README.md)
 
 Based on these models, my rule of thumb approach is:
 
 1. Include all instances of essential reactions, orphan reactions, subsystem reactions, and close genome reactions where more than half the models require that reaction for gap filling.
 2. Generate a new model with these reactions.
 3. Gap fill that model on all media on which the bacteria can grow.
 
 This results in a model that usually doesn't grow on any media, but needs the media reactions, occasionally a few reactions from the close genomes, and very occasionally an additional orphan reaction for growth.
 
 Gap filling these models tends to be very quick, just a few minutes as we resolve which additional reaction(s) are required.
 
 We can do all of that with one bash command:
 
```
NUM=$(ls *.txt | wc -l); export NUM=$((NUM/2))
for i in essential orphan subsystem close; 
    do grep -h $i  *txt | cut -f 1 | sort | uniq -c | perl -ne 's/^\s+(\d+)\s+//; print if ($1 > $ENV{NUM})'; 
done
```


