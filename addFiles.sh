#Begin------Contents of gravmodeling.sh
#!/bin/bash

if [ -f ./sum ]
then
	rm sum
fi
sed '3q;d' *0000.out
let i=0;
let j=0;
let k=`ls *.out|wc -l`;
####
#while [ $i -le 1 ];
#	do
#	while [ $j -le 1 ]
#		do
#		sed '1q;d' *0000.out
#		done
#	done
#End--------Contents of chunkFile.sh
