# -*- coding: utf-8 -*- 

# Copyright 2016 Devsim LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pylab
import numpy
#ACHEADER: f V(base) V(collector) V(emitter) I(base) I(collector) I(emitter) IR(base) II(base) IR(collector) II(collector) IR(emitter) II(emitter)
filename = 'ft_data.out'

def create_data(data):
    vbe = data[0,1]-data[0,3]
    IC = data[0,5]
    ic = data[:,9] + 1j*data[:,10]
    ib = data[:,7] + 1j*data[:,8]
    beta = abs(ic / ib)
    f = data[:,0]
    betadc = beta[0]
    ft = None
    if betadc > 1:
        for i in range(1, len(beta)):
            if beta[i] < 1:
                # simple linear interpolation
                # should use log
                y1 = numpy.log(beta[i])
                y0 = numpy.log(beta[i-1])
                x1 = numpy.log(f[i])
                x0 = numpy.log(f[i-1])
                m = (y1-y0)/(x1-x0)
                x = x1 - y1/m
                ft = numpy.exp(x)
                break
    return (vbe, {
        'f' : f,
      'ib' : ib, #ac ib
      'ic' : ic, #ac ic
      'IC' : IC, #dc Ic
      'beta' : beta, #ac beta
      'ft' : ft,
    })

data = pylab.loadtxt(filename)
#print len(data)
fmin = data[0,0]
#print fmin
imin = 0
datasets = []
for i in range(1,len(data)):
    f = data[i,0]
    if f == fmin:
        datasets.append(create_data(data[imin:i]))
        imin = i
datasets.append(create_data(data[imin:i]))
#print datasets
pylab.figure()
for v, d in datasets:
    #print '%g %d' %(v, round(v*10))
    if abs(round(v*10.0) - v*10.0) < 1e-2:
        pylab.loglog(d['f'], d['beta'], label=str(v))
pylab.xlabel(r'$f$ (Hz)')
pylab.ylabel(r'$|\beta\|$')
pylab.legend(loc='upper right')
pylab.savefig('ft_curves.pdf')
pylab.savefig('ft_curves.eps', format='eps')


pylab.figure()
IC = []
ft = []
pylab.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
for i in datasets:
    if i[1]['ft']:
        IC.append(i[1]['IC'])
        ft.append(i[1]['ft'])
pylab.semilogx(IC, ft, '-+')
pylab.xlabel(r"$I_c$ (A/cm)")
pylab.ylabel(r"$f_T$ (Hz)")
pylab.savefig('ft.pdf')
pylab.savefig('ft.eps', format='eps')

