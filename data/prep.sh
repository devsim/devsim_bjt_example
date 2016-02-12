#!/bin/bash
#format Vb, Vc, Ve, Ib, Ic, Ie
#HEADER: V(base) V(collector) V(emitter) I(base) I(collector) I(emitter)
# each curve is for constant vb
for i in vb2_*.out; do
  fn=`echo $i | sed -e 's/vb2_/ic_vce_/'`
  grep "CURVE: " $i  | sed -e 's/CURVE: //' > $fn
done

# each curve is for constant vcb and ve swept negative
#http://en.wikipedia.org/wiki/Gummel_plot
for i in ve_*.out; do
  fn=`echo $i | sed -e 's/ve_/gummel_/'`
  grep "CURVE: " $i  | sed -e 's/CURVE: //' > $fn
done


# for this data Vcb is 0.0 and Ve is swept negative
#ACHEADER: f V(base) V(collector) V(emitter) I(base) I(collector) I(emitter) IR(base) II(base) IR(collector) II(collector) IR(emitter) II(emitter)
grep 'AC: ' ssac_0.0.out |  sed -e 's/AC: //' > ft_data.out
