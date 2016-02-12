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


load_devices(file="bjt_dd_0.msh")
from physics.new_physics import *

import bjt_params
bjt_params.run(device, region)

import netdoping
netdoping.set_params(device, region)

from physics.new_physics import *
SetSiliconParameters(device, region)

#import setup_dd
#setup_dd.run(device, region)

# also in setup_dd
set_parameter(device=device, region=region, name="T", value="300")
set_parameter(device=device, region=region, name="taun", value=1e-5)
set_parameter(device=device, region=region, name="taup", value=1e-5)
set_parameter(device=device, region=region, name="n1", value=1e10)
set_parameter(device=device, region=region, name="p1", value=1e10)

for c in ("base", "emitter", "collector"):
  set_parameter(device=device, region=region, name=GetContactBiasName(c), value=0.0)
solve(type="dc", absolute_error=1e6, relative_error=1e-1, maximum_iterations=40)
write_devices    (file="bjt_dd_1.msh", type="devsim")

