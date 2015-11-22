
for DIR in models/2*; 
	do 
		RAST=$(echo $DIR | sed -e 's/models\///');
		GENOMEID=$(grep $RAST models/growth_predictions.tsv | cut -f 3 | sort -u);
		REACTF=$DIR/$GENOMEID.reactions
		for MEDIA in $(grep $GENOMEID models/growth_predictions.tsv | grep \+ | cut -f 4); do
			MEDIAF="PyFBA/media/$MEDIA.txt";
			if [ -e $MEDIAF ]; then
				OUT="$DIR/$GENOMEID.gapfilled.$MEDIA.txt";
				ERR="$DIR/$GENOMEID.gapfilled.$MEDIA.err";
				echo "python scripts/gapfill_from_reactions.py -r $REACTF -m $MEDIAF -c $DIR/$GENOMEID.closest.genomes.roles > $OUT 2> $ERR";
			fi;
		done;
	done;
