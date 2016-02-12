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

import sys
Vc=float(sys.argv[1])

import bjt_common
bjt_common.run()

from physics.ramp2 import *
rampvoltage("bjt", "Vc", 0.0, Vc, 0.1, 0.0001, 40, 1e-1, 1e6, bjt_common.make_bias("collector"))
rampvoltage("bjt", "Vb", 0.0, 1.0, 0.1, 0.0001, 40, 1e-2, 1e6, bjt_common.make_sweep(("base", "collector", "emitter"), ("Vb", "Vc", "Ve")))

