#for i in 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0; do
for i in 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0; do
  echo $i
  /usr/bin/time /home/jsanchez/git/devsim/linux_x86_64_release/src/main/devsim_py bjt_circuit2.py $i &> vb2_$i.out
done

