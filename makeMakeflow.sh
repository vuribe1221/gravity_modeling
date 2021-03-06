#Begin------Contents of gravmodeling.sh
#!/bin/bash
# sh scriptname filename # of parts
date > startTime
if [ -d ./density.parts ]
then	
	rm -r density.parts
fi
mkdir density.parts

#DO WORK... SPLIT DENSITY_GRID.TXT INTO GIVEN NUMBER OF FILES
split -a 4 -dl$((`wc -l $1|sed 's/ .*$//'` / $2 + 1)) $1 density.parts/$1_part.

#Create Makeflow file give it the inputs files
touch Makeflow

cd density.parts
ls -N1 > ../Makeflow
cd ..

tr  '\n' ' ' < Makeflow > Makeflow1
mv Makeflow1 Makeflow
echo -e ':\n' >> Makeflow

sed 's/  //g' Makeflow > Makeflow1
mv Makeflow1 Makeflow

#Create Makeflow file step 2 formatting
let nums=$2
let i=0

while [ $nums -gt $i ];
	do
	if [ $i -le 9 ]
	then
		echo -e $1'_part.000'$i'.out: grav.py '$1'_part.000'$i' prism.py '$3'\n\tpython grav.py '$1'_part.000'$i ' '$3>> Makeflow;
	elif [ $i -le 99 ]
	then	
		echo -e $1'_part.00'$i'.out: grav.py '$1'_part.00'$i' prism.py '$3'\n\tpython grav.py '$1'_part.00'$i' '$3>> Makeflow;
	else
		echo -e $1'_part.0'$i'.out: grav.py '$1'_part.0'$i' prism.py '$3'\n\tpython grav.py '$1'_part.0'$i' '$3>> Makeflow;
	fi
	
	let i=$i+1
done

cp Makeflow density.parts/
cp $3 density.parts/
cp prism.py density.parts/
cp grav.py density.parts/
cp addFiles.sh density.parts/
cp prepare.sh density.parts/
rm Makeflow
cd density.parts
#makeflow -T torque
makeflow -T wq -a -N vuribe-calc -p $4
sh prepare.sh > ../OUT

#comment this line to debug files
cd ..
rm -r density.parts/
date > endTime
#End--------Contents of chunkFile.sh
 
