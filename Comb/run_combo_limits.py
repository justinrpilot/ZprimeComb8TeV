#!/usr/bin/env python
import os

if 'THETA_PATH' not in os.environ:
    ext = os.system('source theta_driver/setup.sh')
    
model = 'model.py'

signal_dict = {
  'narrow_resonances': 'n_test',
  'wide_resonances'  : 'w_test',
  'rsg_resonances'   : 'r_test'
}

input_files = '*_zpn_scaled.root ljets_all_scaled.root'

for sig in signal_dict:
    cmd1 = 'theta_driver preprocess --model \''+model.strip('.py')+': type = '+sig+'\' --workdir '+signal_dict[sig]+' --analysis bayesian '+input_files
    cmd2 = 'theta_driver submit --workdir '+signal_dict[sig]
    if os.system(cmd1): raise SystemExit
    if os.system(cmd2): raise SystemExit
