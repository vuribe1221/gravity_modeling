cut -d ' ' -f 3 *.out > onlycol3

split -a 4 -dl 10000 onlycol3 out.

paste -d ' ' out.* > calc

sed ':a;N;$!ba;s/ /+/g' calc > plus

let i=1
let j=`wc -l output|cut -f 1 -d ' '`

while [ $i -le $j ];
        do echo -n $i" "
        head -n $i output|tail -n 1|bc; let i=$i+1; done
let i=1
