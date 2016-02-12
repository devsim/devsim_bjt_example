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

from ds import *

device="bjt"
region="bjt"
mesh_name="bjt"

import read_gmsh
read_gmsh.run("bjt.msh", device, region, "Silicon", ("base", "collector", "emitter"))



# read in last simulation when ready
import netdoping
netdoping.run(device, region)
import initial_guess
initial_guess.run(device, region)




from physics.new_physics import *

import bjt_params
bjt_params.run(device, region)


import setup_dd
setup_dd.run(device, region)

#Get the initial guess from here
set_node_values(device=device, region=region, name="Electrons", init_from="IntrinsicElectrons")
set_node_values(device=device, region=region, name="Holes", init_from="IntrinsicHoles")


element_from_edge_model(edge_model="EField", device=device, region=region)
element_model(device=device, region=region, name="Emag", equation="(EField_x^2 + EField_y^2)^(0.5)")
element_from_edge_model(edge_model="Jn", device=device, region=region)
element_from_edge_model(edge_model="Jp", device=device, region=region)
element_model(device=device, region=region, name="Jnmag", equation="(Jn_x^2 + Jn_y^2)^(0.5)")
element_model(device=device, region=region, name="Jpmag", equation="(Jp_x^2 + Jp_y^2)^(0.5)")

#edge_model(device=device, region=region, name='test', equation="pow(vsat_n,(-1))")
#edge_model(device=device, region=region, name='test', equation="((mu_arora_n_lf * Epar_n) * pow(vsat_n,(-1)))")
#edge_model(device=device, region=region, name='test', equation="(1 + pow(((mu_arora_n_lf * Epar_n) * pow(vsat_n,(-1))),beta_n))")
#edge_model(device=device, region=region, name='test', equation="vec_min(((mu_arora_n_lf * Epar_n) * pow(vsat_n,(-1))))")
#edge_model(device=device, region=region, name='test', equation="vec_min(((mu_arora_n_lf * Epar_n) * pow(vsat_n,(-1))))")
#edge_model(device=device, region=region, name='test', equation="vec_min(((mu_arora_n_lf * Epar_n) * pow(vsat_n,(-1))))")
#edge_model(device=device, region=region, name='test', equation="(mu_arora_n_lf * pow((1 + pow(((mu_arora_n_lf * Epar_n) * pow(vsat_n,(-1))),beta_n)),(-pow(beta_n,(-1)))))")
#print get_edge_model_values(device=device, region=region, name='test')[0]
#print get_edge_model_values(device=device, region=region, name='mu_n')[0]
#print get_edge_model_values(device=device, region=region, name='mu_arora_n_lf')[0]

solve(type="dc", absolute_error=1e6, relative_error=1e-1, maximum_iterations=40)
write_devices    (file="bjt_dd_0.tec", type="tecplot")
write_devices    (file="bjt_dd_0.msh", type="devsim")

#from physics.ramp import *
#printAllCurrents(device)
##CreateNodeModel(device, region, 'netsrh', 'NodeVolume*USRH')
#print sum(get_node_model_values(device=device, region=region, name="netsrh"))
#set_parameter(device=device, name=GetContactBiasName('collector'), value=1.0)
#solve(type="dc", absolute_error=1e6, relative_error=1e3, maximum_iterations=40)
#printAllCurrents(device)
#set_parameter(device=device, name=GetContactBiasName('base'), value=0.5)
#solve(type="dc", absolute_error=1e10, relative_error=1e3, maximum_iterations=40)
#printAllCurrents(device)
#
#write_devices    (file="bjt_dd_1.tec", type="tecplot")
#write_devices    (file="bjt_dd_1.msh", type="devsim")
