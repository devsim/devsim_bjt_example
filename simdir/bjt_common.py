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
import bjt_params
import netdoping

def make_bias(contact):
  def mycall():
    print "BIAS %s %1.15g" % (contact, get_circuit_node_value(solution="dcop", node=GetContactBiasName(contact)))
  return mycall

def make_sweep(contact_names, bias_names):
  #cnames = ("base", "collector", "emitter")
  def mycall():
    v=[]
    for c in contact_names:
      v.append("%1.15g" % get_circuit_node_value(solution="dcop", node=GetContactBiasName(c)))
    for b in bias_names:
      v.append("%1.15g" % -get_circuit_node_value(solution="dcop", node=b+".I"))
    print "CURVE: " + " ".join(v)
  h = []
  for c in contact_names:
    h.append("V(%s)" % c)
  for c in contact_names:
    h.append("I(%s)" % c)
  print "HEADER: " + " ".join(h)
  return mycall

def make_ac_callback(contact_names, bias_names, minf, maxf, ppd):
  cnames = ("base", "collector", "emitter")
  if (minf > maxf) or (minf <= 0.0) or (ppd <= 0):
    raise NameError("minf must be less than maxf and greater than zero.  ppd must be greater than 0")
  ppde = pow(10, 1/ppd)
  f = minf
  freqs = [minf]
  while f < maxf:
    f *= ppde
    if f > maxf:
      f = maxf
    freqs.append(f)
  h = ["f"]
  for c in contact_names:
    h.append("V(%s)" % c)
  for c in contact_names:
    h.append("I(%s)" % c)
  for c in contact_names:
    h.append("IR(%s)" % c)
    h.append("II(%s)" % c)
  print "ACHEADER: " + " ".join(h)
  def ac_callback():
    # solve a few extra times for better ac sensitivity
    solve(type="dc", absolute_error=1e10, relative_error=1e-2, maximum_iterations=40)
    solve(type="dc", absolute_error=1e10, relative_error=1e-2, maximum_iterations=40)
    solve(type="dc", absolute_error=1e10, relative_error=1e-2, maximum_iterations=40)
    cinfo = []
    for c in contact_names:
      cinfo.append("%1.15g" % get_circuit_node_value(solution="dcop", node=GetContactBiasName(c)))
    for b in bias_names:
      cinfo.append("%1.15g" % -get_circuit_node_value(solution="dcop", node=b+".I"))
    for f in freqs:
      v = ["%1.15g" % f]
      v.extend(cinfo)
      solve(type="ac", frequency=f)
      for b in bias_names:
        v.append("%1.15g" % -get_circuit_node_value(solution="ssac_real", node=b+".I"))
        v.append("%1.15g" % -get_circuit_node_value(solution="ssac_imag", node=b+".I"))
      print "AC: " + " ".join(v)
  return ac_callback

def run():
  device="bjt"
  region="bjt"
  load_devices(file="bjt_dd_0.msh")
  bjt_params.run(device, region)
  netdoping.set_params(device, region)
  SetSiliconParameters(device, region)

  for c in ("base", "emitter", "collector"):
    #set_parameter(device=device, region=region, name=GetContactBiasName(c), value=0.0)
    CreateSiliconDriftDiffusionContact(device, region, c, "Jn", "Jp", True)
    # use first initial of each contact name
    circuit_element(name="V%s" % c[0], n1=GetContactBiasName(c), n2="0", value=0.0)

  solve(type="dc", absolute_error=1e6, relative_error=1e-1, maximum_iterations=40)
  solve(type="dc", absolute_error=1e6, relative_error=1e-1, maximum_iterations=40)
  solve(type="dc", absolute_error=1e6, relative_error=1e-1, maximum_iterations=40)


