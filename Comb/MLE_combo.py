# script to run ML fit to data
# in the combination framework
#
# the model is defined in 'model_MLE.py'
#
# run this script from the Comb/ directory
#
# $ python MLE_combo.py [NAME]
#
# where NAME is the folder
# in which the output is stored

import sys, os, glob
import subprocess

if len(sys.argv)-1 != 1:
    print '\n@@@ FATAL -- only 1 argument needed (output directory)\n'
    sys.exit()

if os.environ.get('THETA_PATH') == None:
    print '\n@@@ FATAL -- global variable THETA_PATH not set in the shell ("where is theta installed?")\n'
    sys.exit()

outdir = sys.argv[1]

subprocess.call('mkdir -p '+outdir, shell=True)
subprocess.call('cp model_MLE.py '+outdir+'/analysis_ML.py', shell=True)

with open(outdir+'/analysis_ML.py', 'a') as file:
    file.write('\n\n')
    addon = """
# Building the statistical model
model = build_model('narrow_resonances')

options = Options()
#options.set('minimizer', 'strategy', 'robust')
#options.set('minimizer', 'minuit_tolerance_factor', '100')
options.set('minimizer', 'strategy', 'newton_vanilla')

sig = ''
sig_a = []
if sig != '': sig_a.append(sig)

res = mle(model, input='data', n=1, signal_process_groups = {sig : sig_a}, chi2 = True, options = options)

print '\\n-- MLE: fit results (# = '+str(len(res[sig][model.get_parameters(sig_a)[0]]))+')'
fitres = {}
print 'chi2 =',res[sig]['__chi2']
file1 = open('mle_fit.txt', 'w')
for p in model.get_parameters(sig_a):
    mean = sdev = 0.0
    for pair in res[sig][p]:
        mean += pair[0]
        sdev += pair[1]
    mean /= len(res[sig][p])
    sdev /= len(res[sig][p])

    fitres[p] = {}
    fitres[p][0] = mean
    fitres[p][1] = sdev

    line = ''
    if mean>=0: line += ' '
    line += ' %.3f' % mean + '  %.3f' % sdev + '  ' + p
    print line
    file1.write(line+'\\n')

par_values = {}
for p in model.get_parameters([]):
    par_values[p] = fitres[p][0]

# rate-scale factors for each process in each observable
mle_coeff = {}
for obs in model.get_observables():
    mle_coeff[obs] = {}
    for p in model.get_processes(obs):
        coeff = model.get_coeff(obs, p).get_value(par_values)
        mle_coeff[obs][p] = coeff

# add stuff.. eg make histograms at the ML point
print '\\n'
for p in par_values:
    if p == 'ttbar_rate':     print '%.3f' % 1.15**par_values[p] + ' ' + p
    elif p == 'wl_rate':      print '%.3f' % 1.09**par_values[p] + ' ' + p
    elif p == 'wc_rate':      print '%.3f' % 1.23**par_values[p] + ' ' + p
    elif p == 'wb_rate':      print '%.3f' % 1.23**par_values[p] + ' ' + p
    elif p == 'st_rate':      print '%.3f' % 1.23**par_values[p] + ' ' + p
    elif p == 'zj_rate':      print '%.3f' % 1.50**par_values[p] + ' ' + p
    elif p == 'diboson_rate': print '%.3f' % 1.20**par_values[p] + ' ' + p
    elif p == 'toptag':       print '%.3f' % 1.20**par_values[p] + ' ' + p
    elif p == 'subjbtag':     print '%.3f' % 1.20**par_values[p] + ' ' + p
"""
    file.write(addon)
    file.write('\n')

cmds = []

import glob

root_files = glob.glob('*.root')
for f in root_files:
    fullpath = os.path.realpath(f)
    cmds.append('ln -s '+fullpath+' '+outdir+'/'+f)

cmds += [
    'mv '+outdir+' $THETA_PATH/utils2',
    'cd $THETA_PATH/utils2/'+outdir+'; ../theta-auto.py analysis_ML.py',# > mle.log'
    'mv $THETA_PATH/utils2/'+outdir+' .'
]

for cmd in cmds:
    print cmd
    subprocess.call([cmd], shell=True)
