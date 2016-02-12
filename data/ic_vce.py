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
#import numpy
#import matplotlib.pyplot as plt
##HEADER: V(base) V(collector) V(emitter) I(base) I(collector) I(emitter)

files = (
#'ic_vce_0.1.out',
#'ic_vce_0.2.out',
#'ic_vce_0.3.out',
#'ic_vce_0.4.out',
#'ic_vce_0.5.out',
#'ic_vce_0.6.out',
'ic_vce_0.7.out',
#'ic_vce_0.8.out',
#'ic_vce_0.9.out',
#'ic_vce_1.0.out',
)

for filename in files:
  data = pylab.loadtxt(filename)
  vce = data[:,1]-data[:,2]
  ic = data[:,4]
  pylab.plot(vce, ic)

pylab.xlabel(r"$V_{ce}$ (V)")
pylab.ylabel(r"$I_c$ (A/cm)")
pylab.savefig('ic_vce.pdf')
pylab.savefig('ic_vce.eps', format='eps')
