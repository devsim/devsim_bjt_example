#for i in 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0; do
for i in 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0; do
#  echo $i
  echo "/usr/bin/time /home/jsanchez/git/devsim/linux_x86_64_release/src/main/devsim_py bjt_circuit2.py $i &> data/vb2_$i.out"
done

#for i in 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0; do
for i in 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 1.1 1.2 1.3 1.4 1.5; do
#  echo $i
  echo "/usr/bin/time /home/jsanchez/git/devsim/linux_x86_64_release/src/main/devsim_py bjt_circuit3.py $i &> data/vc_$i.out"
done

# goes from vcb=0 to vcb=0.5
# vbe is then swept from 0 to 1.0
for i in 0.0 0.1 0.2 0.3 0.4 0.5; do
#  echo $i
  echo "/usr/bin/time /home/jsanchez/git/devsim/linux_x86_64_release/src/main/devsim_py bjt_circuit4.py $i &> data/ve_$i.out"
done

# goes from vcb=0 to vcb=0.5
# vbe is then swept from 0 to 1.0
#for i in 0.0 0.1 0.2 0.3 0.4 0.5; do
#  echo $i
vc=0.0
fmin=1e3
fmax=1e11
ppd=3
echo "/usr/bin/time /home/jsanchez/git/devsim/linux_x86_64_release/src/main/devsim_py bjt_circuit5.py $vc $fmin $fmax $ppd &> data/ssac_$vc.out"
#done

