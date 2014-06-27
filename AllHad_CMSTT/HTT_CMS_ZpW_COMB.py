def build_model(rootfile):
    model = build_model_from_rootfile(rootfile, include_mc_uncertainties=True)
    model.fill_histogram_zerobins()
    model.set_signal_processes('Zp*')
    for p in model.processes:
       if p == 'qcd': continue
       model.add_lognormal_uncertainty('lumi', 0.026, p)
       model.add_lognormal_uncertainty('trig', 0.02, p)
       model.add_lognormal_uncertainty('subSF', 0.05, p)
    #model.add_lognormal_uncertainty('xs_qcd', 0.10, 'qcd')
    model.add_lognormal_uncertainty('xs_top', 0.15, 'ttbar')

    return model


def external_to_internal(hname):
    if '0w' in hname:
	 hname = hname.replace('0w', '0')
	 hname = hname.replace('Zprime', 'ZprimeWide')
    elif 'Zprime' in hname:
	 hname = 'DONOTUSE'
    if 'RSG' in hname:
	 hname = 'DONOTUSE'
	 #hname = hname.replace('RSG', 'RSgluon')
    print hname
    return hname 





def build_HTT_model(rootfile):
    model = build_model_from_rootfile(rootfile, root_hname_to_convention = external_to_internal, include_mc_uncertainties=True)
    model.fill_histogram_zerobins()
    model.set_signal_processes('Zp*')
    for p in model.processes:
       if p == 'qcd': continue
       model.add_lognormal_uncertainty('lumi', 0.026, p)
       model.add_lognormal_uncertainty('trig', 0.02, p)
    model.add_lognormal_uncertainty('xs_top', 0.15, 'ttbar')



    return model



# Code introduced by theta_driver

# Building the statistical model

model = build_model('ZpW_templates_May20.root')
HTTmodel = build_HTT_model('htt_zprimewide-1.root')

#model = HTTmodel

model.combine(HTTmodel, strict=False)


options = Options()
options.set('minimizer', 'strategy', 'robust')
options.set('minimizer', 'minuit_tolerance_factor', '1000')

parVals = mle(model, input='data', n=1, options = options)
print parVals



plot_exp, plot_obs = bayesian_limits(model, run_theta = True)
plot_exp.write_txt('exp_limit_ZpW_comb.txt')
plot_obs.write_txt('obs_limit_ZpW_comb.txt')
model_summary(model, all_nominal_templates=True, shape_templates=True)
