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

def run(filename, device_name, region, region_material, contact_names):
  #this reads in the gmsh format
  create_gmsh_mesh (mesh=device_name, file=filename)
  add_gmsh_region  (mesh=device_name, gmsh_name=region,    region=region, material=region_material)
  for contact in contact_names:
    add_gmsh_contact (mesh=device_name, gmsh_name=contact, region=region, material="metal", name=contact)
  finalize_mesh    (mesh=device_name)
  create_device    (mesh=device_name, device=device_name)

