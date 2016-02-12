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
from physics.new_physics import *

def run(device, region):

  # this is our solution variable
  CreateSolution(device, region, "Potential")
  CreateSolution(device, region, "Electrons")
  CreateSolution(device, region, "Holes")

  #these are needed for velocity saturation
  CreateEField(device, region)
  CreateDField(device, region)
  opts = CreateAroraMobilityLF(device, region)
  opts = CreateHFMobility(device, region, **opts)


  CreateSiliconDriftDiffusion(device, region, **opts)
  for i in get_contact_list(device=device):
    set_parameter(device=device, name=GetContactBiasName(i), value=0.0)
    CreateSiliconDriftDiffusionContact(device, region, i, opts['Jn'], opts['Jp'])


