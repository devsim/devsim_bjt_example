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
from physics.new_physics import *

def run(device, region):

    # this is our solution variable
    CreateSolution(device, region, "Potential")
    # start with temperature as a model and not a parameter
    set_parameter(device=device, name="T", value="300")

    CreateSiliconPotentialOnly(device, region)
    for i in get_contact_list(device=device):
        set_parameter(device=device, name=GetContactBiasName(i), value=0.0)
        CreateSiliconPotentialOnlyContact(device, region, i)

    ####
    #### Initial DC solution
    ####
    solve(type="dc", absolute_error=1.0, relative_error=1e-9, maximum_iterations=40)

