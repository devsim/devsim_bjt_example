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

def set_params(device, region):
    params = {
        'base_center' : 13.75e-4,
      'base_depth' : 1.3e-4,
      'base_doping' : 1e17,
      'base_hdiff' : 1.0e-5,
      'base_vdiff' : 1.0e-5,
      'base_width' : 20e-4,
      'collector_doping' : 1e16,
      'emitter_center' : 20e-4,
      'emitter_depth' : 1.0e-4,
      'emitter_doping' : 1e19,
      'emitter_hdiff' : 1.0e-5,
      'emitter_vdiff' : 1.0e-5,
      'emitter_width' : 5e-4,
      'sub_collector_center' : 13.75e-4,
      'sub_collector_depth' : 4e-4,
      'sub_collector_doping' : 1e19,
      'sub_collector_hdiff' : 1.0e-5,
      'sub_collector_vdiff' : 1.0e-5,
      'sub_collector_width' : 30e-4,
    }
    for k, v in params.items():
        set_parameter(device=device, region=region, name=k, value=v)

####
#### NetDoping
####
def run(device, region):
    set_params(device, region)
    node_model(device=device, region=region, name="Acceptors", equation='''
    base_doping
    * erfc((y-base_depth)/base_vdiff)
    * erfc(-(x + 0.5*base_width-base_center)/base_hdiff)
    * erfc((x - 0.5*base_width-base_center)/base_hdiff)
  ''')
    node_model(device=device, region=region, name="Donors", equation='''
    emitter_doping
    * erfc((y-emitter_depth)/emitter_vdiff)
    * erfc(-(x + 0.5*emitter_width-emitter_center)/emitter_hdiff)
    * erfc((x - 0.5*emitter_width-emitter_center)/emitter_hdiff)
    + collector_doping
    + sub_collector_doping
    * erfc(-(y-sub_collector_depth)/sub_collector_vdiff)
    * erfc(-(x + 0.5*sub_collector_width-sub_collector_center)/sub_collector_hdiff)
    * erfc((x - 0.5*sub_collector_width-sub_collector_center)/sub_collector_hdiff)
  ''')
    node_model(device=device, region=region, name="NetDoping", equation="Donors-Acceptors;")
    node_model(device=device, region=region, name="LogNetDoping", equation="asinh(Donors-Acceptors/2)/log(10)")


