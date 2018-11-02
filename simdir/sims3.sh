#for i in 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0; do
for i in 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 1.1 1.2 1.3 1.4 1.5; do
  echo $i
  /usr/bin/time python bjt_circuit3.py $i &> vc_$i.out
done

