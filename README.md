# Genotype-Phenotype-Modeling
Modeling growth of bacterial genomes and connecting genotype to phenotype

# Installation

1. Make sure that you do a recursive clone of the git repository.

```
git clone --recursive ***
```
2. Set your pythonpath to include PyFBA

```
export PYTHONPATH=$PYTHONPATH:PyFBA
```

3. Run your code

```
python scripts/assigned_functions_to_reactions.py -a models/260567/6666666.127365.assigned_functions
```


or to run everything in batch:

```
for a in $(ls models/*/*assigned_functions); 
    do
	r=$(echo $a | perl -npe 's#(models/\d+/[\d\.]+).assigned_functions#$1#'); 
	python scripts/assigned_functions_to_reactions.py -a $a > $r.reactions; 
done
```
