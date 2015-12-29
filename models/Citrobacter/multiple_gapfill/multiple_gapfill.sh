export PYTHONPATH=/home3/redwards/PyFBA::/usr/local/opencv/lib/python2.6/site-packages/:/home3/redwards/bioinformatics/Modules/:/home3/redwards/python/lib/python2.7/site-packages/:/usr/local/opencv/lib/python2.6/site-packages/:/home3/redwards/bioinformatics/Modules/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/lib:/usr/local/lib
export ModelSEEDDatabase=/home3/redwards/ModelSEEDDatabase
python2.7 ~/PyFBA/example_code/gapfill_from_reactions_multiple_conditions.py  -r 67826.8.reactions -p ~/PyFBA/media/MOPS_NoN_Adenine.txt -p ~/PyFBA/media/MOPS_NoN_L-Glutathione.txt -p ~/PyFBA/media/MOPS_NoN_N-Acetyl-D-Glucosamine.txt -n ~/PyFBA/media/MOPS_NoC_Negative_Control.txt -n ~/PyFBA/media/MOPS_NoC_D-Glutamic_Acid.txt -f 0.6 -c citrobacter.roles -g closest.genomes.roles -v
