# goes from vcb=0 to vcb=0.5
# vbe is then swept from 0 to 1.0
for i in 0.0 0.1 0.2 0.3 0.4 0.5; do
  echo $i
  /usr/bin/time python bjt_circuit4.py $i &> ve_$i.out
done

