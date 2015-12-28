export PYTHONPATH=/home3/redwards/PyFBA::/usr/local/opencv/lib/python2.6/site-packages/:/home3/redwards/bioinformatics/Modules/:/home3/redwards/python/lib/python2.7/site-packages/:/usr/local/opencv/lib/python2.6/site-packages/:/home3/redwards/bioinformatics/Modules/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/lib:/usr/local/lib
export ModelSEEDDatabase=/home3/redwards/ModelSEEDDatabase
python2.7 $HOME/Genotype-Phenotype-Modeling/scripts/growth_on_all_media.py -r 20151225.model -m $HOME/Genotype-Phenotype-Modeling/media/ > 20151225.predictions
