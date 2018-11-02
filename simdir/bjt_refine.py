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

from devsim import *

device="bjt"
region="bjt"
mesh_name="bjt"

import read_gmsh
read_gmsh.run("bjt.msh", device, region, "Silicon", ("base", "collector", "emitter"))

import netdoping
netdoping.run(device, region)

write_devices    (file="bjt_doping.tec", type="tecplot")

#import sys
#sys.exit()

import initial_guess
initial_guess.run(device, region)

import refinement
refinement.run(device, region, outfile="bjt_bgmesh.pos", mincl=2.0e-6, maxcl=1e-4, pdiff=0.025)
    
# this is is the devsim format
write_devices    (file="bjt_refine.tec", type="tecplot")

