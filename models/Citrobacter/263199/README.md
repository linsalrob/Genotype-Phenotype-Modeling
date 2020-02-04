# A revised Citrobacter model based on the RAST annotation

We built a revised citrobacter model based on the RAST annotation. This is in models/pickles/Citrobacter.67826.8.p

We start with the assigned_functions in [67826.8.assigned_functions](67826.8.assigned_functions) and connect those 
roles to reactions.

We start with creating a pickle of the model:

```
python flux_balance_analysis/pickle_fba.py -a models/Citrobacter/263199/67826.8.assigned_functions -g 67826.8 -m media/ArgonneLB.txt -p Citrobacter.67826.8.p
```

This doesn't grow and so we need some [gapfilling](../gapfilling/README.md) or 
[more gapfilling](../flux_balance_gapfilling/README.md).

We added the following set of reactions that are required for growth on *all* minimal media conditions.

```
'rxn00293', 'rxn03164', 'rxn08333', 'rxn00392', 'rxn03638', 'rxn10094', 
'rxn03395', 'rxn03397', 'rxn11946', 'rxn02285', 'rxn00122'
```

To do that, we make a temp file with these reactions and use that to update our pickle model. This also backups the 
old model into a new file!

```bash
echo "{'rxn00293', 'rxn03164', 'rxn08333', 'rxn00392', 'rxn03638', 'rxn10094', \
'rxn03395', 'rxn03397', 'rxn11946', 'rxn02285', 'rxn00122'}" > temp/addnl
python flux_balance_scripts/update_pickle.py -p Citrobacter.67826.8.p -r temp/addnl -v
```


