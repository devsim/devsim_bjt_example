# goes from vcb=0 to vcb=0.5
# vbe is then swept from 0 to 1.0
#for i in 0.0 0.1 0.2 0.3 0.4 0.5; do
#  echo $i
vc=0.0
fmin=1e3
fmax=1e11
ppd=3
/usr/bin/time python bjt_circuit5.py $vc $fmin $fmax $ppd &> ssac_$vc.out
#done

