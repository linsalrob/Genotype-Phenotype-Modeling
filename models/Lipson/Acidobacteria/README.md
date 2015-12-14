#Acidobacteria and related genomes

These are some genomes for work with David Lipson at SDSU. We are testing Acidobacteria and related genomes models.

The genomes we want to test are:

Genome | SEED ID
--- | ---
Acidobacteria bacterium KBS 146 | 639030.3
Acidobacteriaceae bacterium KBS 83 | 1267533.3
Acidobacteriaceae bacterium KBS 89 | 1267534.3
Acidobacteriaceae bacterium KBS 96 | 1267535.3
Acidobacteriaceae bacterium TAA166 | 278963.3
Acidobacteriaceae bacterium URHE0068 | 1380348.5
Acidobacterium sp. MP5ACTX8 | 682795.3
Acidobacterium sp. MP5ACTX9 | 696844.4
Acidobacterium sp. PMMR2 | 1382359.3
Acidobacterium sp. SP1PR4 | 401053.3
Terriglobus roseus DSM 18391 | 926566.3
Solibacter usitatus Ellin6076 | 234267.13
Bryobacter aggregatus MPL3 | 1340493.3
Edaphobacter aggregans DSM 19364 | 1121860.3
Burkholderia multivorans ATCC 17616 | 395019.8
Burkholderia cenocepacia AU 1054 | 331271.8
Burkholderia cepacia ATCC 2541601 | 983594.7
Burkholderia fungorum NBRC 102489 | 1218077.4
Pseudomonas fluorescens Pf-5 | 220664.5
Pseudomonas fluorescens Pf0-1 | 205922.5
Pseudomonas putida F1 | 351746.6
Pseudomonas corrugata CFBP 5454 | 1316927.4

We have grabbed the assigned functions file from these genomes, and we are going to use the union of those files to be all the assigned functions we need. Then we are going to try Rob's gapfilling approaches on them to see how many grow.

We collect all the functions to get a list of what is there:

```
perl models/Acidobacteria/count_functions.pl models/Acidobacteria/*/assigned_functions > models/Acidobacteria/functions.txt
```


We can run all the pickling and model creation and testing at once:

```
for i in models/Acidobacteria/*; do
	if [ -e $i/assigned_functions ]; then
		o=$(echo $i | sed -e 's/^.*bacteria\///');
		echo $i $o;
		python flux_balance_analysis/pickle_fba.py -a $i/assigned_functions -m media/ArgonneLB.txt -p $o.p;
		python flux_balance_scripts/gap_fill_probability.py  -p $o.p -g models/Acidobacteria/functions.txt;
	fi;
done
```


