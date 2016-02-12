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
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()
filename = 'gummel_0.0.out'
#HEADER: V(base) V(collector) V(emitter) I(base) I(collector) I(emitter)
data = pylab.loadtxt(filename)
vbe = data[:,0]-data[:,2]
ic = data[:,4]
ib = data[:,3]
beta = ic/ib
l1 = ax1.semilogy(vbe, beta, "-*", label=r"$\beta$", color="black")
l2 = ax2.semilogy(vbe, ic, "-+", label=r"$I_c$")
l3 = ax2.semilogy(vbe, ib, "-.",  label=r"$I_b$")
lns = l1 + l2 + l3
ax1.legend(l1+l2+l3, (r"$\beta$", r"$I_c$", r"$I_b$"), loc="upper left")
#pylab.title("Title of Plot")
ax1.set_xlabel(r"$V_{be}$ (V)")
ax2.set_ylabel(r"A/cm")
#ax2.set_ylabel(r"A/cm")
#pylab.ylabel("Y Axis Label")
pylab.savefig('gummel.pdf')
pylab.savefig('gummel.eps', format='eps')


