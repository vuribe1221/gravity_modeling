cut -d ' ' -f 3 *.out > cutfiles

let temp=`wc -l cutfiles|cut -d ' ' -f 1`

let temp1=`ls *.out|wc -l`
let temp2=`echo $(($temp/$temp1))`

split -dl $temp2 cutfiles

paste -d ' ' x* > pstdfile

sed ':a;N;$!ba;s/ /+/g' pstdfile > plus

let i=1
let j=`wc -l pstdfile|cut -d ' ' -f 1`

while [ $i -le $j ];
        do echo -n $i" "
        head -n $i plus|tail -n 1|bc; let i=$i+1; done
let i=1
