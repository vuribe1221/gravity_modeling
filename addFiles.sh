#Begin------Contents of gravmodeling.sh
#!/bin/bash

if [ -f ./sum ]
then
	rm sum
fi


cut -f 3 -d ' ' *.out > col
 
split -a 10 -dl 3 col col.

paste -d"+" col.*|while read line
	do
	#echo -n"$line="
	echo $line|bc >> sum
	done

rm col*

let i=1
let j=`wc -l sum|cut -f1 -d ' '`

while [ $i -le $j ];
do
	echo $i' '1 `head -n $i sum|tail -n 1` 
	let i=$i+1
done
#End--------Contents of chunkFile.sh
