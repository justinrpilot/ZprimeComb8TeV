
### Filter definitions ###

def narrow_resonances(hname):
    if 'RSg' in hname:
	return False
    # Accept anything that there is neither of the signals
    if 'rsg' not in hname and 'zp' not in hname :
        return True
    # Reject RS gluons as signal
    elif 'rsg' in hname:
        return False
    # Process signal name
    pname = hname.split('__')[1]
    # reject wide reonances
    if 'w10p' in pname:
        return False
    # Accept only a few mass points (no interpolation)
    mass = pname.split('w')[0].split('zp')[1]
    #mass_whitelist = ['500', '750','1000','1250','1500','2000','3000','4000']
    return float(mass) <= 4000


def wide_resonances(hname):
    # Accept anything that there is neither of the signals
    if 'RSg' in hname:
	return False
    if 'Zprime' in hname and 'Wide' not in hname and 'htt' not in hname:
	return False
    if 'rsg' not in hname and 'zp' not in hname :
        return True
    # Reject RS gluons as signal
    elif 'rsg' in hname:
        return False
    # Process signal name
    pname = hname.split('__')[1]
    # reject wide reonances
    if 'w1p' in pname:
        return False
    # Accept only a few mass points (no interpolation)
    mass = pname.split('w')[0].split('zp')[1]
    #mass_whitelist = ['500', '750','1000','1250','1500','2000','3000','4000']
    return float(mass) <= 4000 


def rsg_resonances(hname):
    # Accept anything that there is neither of the signals
    if 'zp' in hname or 'Zprime' in hname:
	return False
    if 'rsg' not in hname and 'zp' not in hname :
        return True
    # Reject zp as signal
    elif 'zp' in hname:
        return False
    # Process signal name
    pname = hname.split('__')[1]
    # Accept only a few mass points (no interpolation)
    mass = pname[3:]
    #mass_whitelist = ['1000','1500','2000','2500','3000','3500','4000']
    return float(mass) <= 4000




## def narrow_resonances_allhad(hname):
##     #hname = external_to_internal(hname)
##     return narrow_resonances(hname)

## def wide_resonances_allhad(hname):
##     #hname = external_to_internal(hname)
##     return wide_resonances(hname)

## def rsg_resonances_allhad(hname):
##     #hname = external_to_internal(hname)
##     return rsg_resonances(hname)

def external_to_internal(hname):
    print 'replacing ' + hname,
    m = {'RSGluon_':'rsg',
         'RSgluon':'rsg',
         'RSG':'rsg',
         'kkg':'rsg',
         'Zprime1000':'zp1000',
         'Zprime1250':'zp1250',
         'Zprime500':'zp500',
         'Zprime750':'zp750',
         'Zprime1100':'zp1100',
         'Zprime1200':'zp1200',
         'Zprime1300':'zp1300',
         'Zprime1400':'zp1400',
         'Zprime1500':'zp1500',
         'Zprime1600':'zp1600',
         'Zprime1700':'zp1700',
         'Zprime1800':'zp1800',
         'Zprime1900':'zp1900',
         'Zprime2000':'zp2000',
         'Zprime2100':'zp2100',
         'Zprime2200':'zp2200',
         'Zprime2300':'zp2300',
         'Zprime2400':'zp2400',
         'Zprime2500':'zp2500',
         'Zprime2600':'zp2600',
         'Zprime2700':'zp2700',
         'Zprime2800':'zp2800',
         'Zprime2900':'zp2900',
         'Zprime3000':'zp3000',
         'Zprime3100':'zp3100',
         'Zprime3200':'zp3200',
         'Zprime3300':'zp3300',
         'Zprime3400':'zp3400',
         'Zprime3500':'zp3500',
         'Zprime3600':'zp3600',
         'Zprime3700':'zp3700',
         'Zprime3800':'zp3800',
         'Zprime3900':'zp3900',
         'Zprime4000':'zp4000',
         'ZprimeWide1000':'zp1000',
         'ZprimeWide500':'zp500',
         'ZprimeWide750':'zp750',
         'ZprimeWide1250':'zp1250',
         'ZprimeWide1100':'zp1100',
         'ZprimeWide1200':'zp1200',
         'ZprimeWide1300':'zp1300',
         'ZprimeWide1400':'zp1400',
         'ZprimeWide1500':'zp1500',
         'ZprimeWide1600':'zp1600',
         'ZprimeWide1700':'zp1700',
         'ZprimeWide1800':'zp1800',
         'ZprimeWide1900':'zp1900',
         'ZprimeWide2000':'zp2000',
         'ZprimeWide2100':'zp2100',
         'ZprimeWide2200':'zp2200',
         'ZprimeWide2300':'zp2300',
         'ZprimeWide2400':'zp2400',
         'ZprimeWide2500':'zp2500',
         'ZprimeWide2600':'zp2600',
         'ZprimeWide2700':'zp2700',
         'ZprimeWide2800':'zp2800',
         'ZprimeWide2900':'zp2900',
         'ZprimeWide3000':'zp3000',
         'ZprimeWide3100':'zp3100',
         'ZprimeWide3200':'zp3200',
         'ZprimeWide3300':'zp3300',
         'ZprimeWide3400':'zp3400',
         'ZprimeWide3500':'zp3500',
         'ZprimeWide3600':'zp3600',
         'ZprimeWide3700':'zp3700',
         'ZprimeWide3800':'zp3800',
         'ZprimeWide3900':'zp3900',
         'ZprimeWide4000':'zp4000',
         'ttjets':'ttbar',
	 'electronid':'eleid',
	 'electrontrig':'eletrig_rate',
	 'muonid':'muoid',
	 'btagbc':'btag',
	 'btaglight':'bmistag',
	 'Q2scale':'q2'
         }
    for old_pname in m:
        if ('__' + old_pname) in hname: hname = hname.replace('__' + old_pname, '__' + m[old_pname])
    hname = hname.replace('w10p', 'w')
    hname = hname.replace('0w', '0')
    print ' changed to ' + hname
   
    return hname



def build_dilep_model(files, filter, signal, mcstat):
    # Read in and build the model automatically from the histograms in the root file. 
    # This model will contain all shape uncertainties given according to the templates
    # which also includes rate changes according to the alternate shapes.
    # For more info about this model and naming conventuion, see documentation
    # of build_model_from_rootfile.
    model = build_model_from_rootfile(files, filter, root_hname_to_convention = external_to_internal, include_mc_uncertainties = mcstat)
    model.fill_histogram_zerobins()
    model.set_signal_processes(signal)

    # Add some lognormal rate uncertainties. The first parameter is the name of the
    # uncertainty (which will also be the name of the nuisance parameter), the second
    # is the 'effect' as a fraction, the third one is the process name. The fourth parameter
    # is optional and denotes the channl. The default '*' means that the uncertainty applies
    # to all channels in the same way.
    # Note that you can use the same name for a systematic here as for a shape
    # systematic. In this case, the same parameter will be used; shape and rate changes 
    # will be 100% correlated.

    model.add_lognormal_uncertainty('ttbar_rate',     math.log(1.15), 'ttbar'    )
    model.add_lognormal_uncertainty('zj_rate',        math.log(2.0),  'DY'       )
    model.add_lognormal_uncertainty('st_rate',        math.log(1.50), 'singletop')
    model.add_lognormal_uncertainty('diboson_rate',   math.log(1.5),  'VV'       )

    for p2 in model.processes:
        model.add_lognormal_uncertainty('lumi', math.log(1.026), p2)
    return model


def build_boosted_allhadronic_CMSTT_model(files, filter, signal, mcstat):
    """ All hadronic high mass model """    
    model = build_model_from_rootfile(files, filter, root_hname_to_convention = external_to_internal, include_mc_uncertainties = mcstat)
    model.fill_histogram_zerobins()
    model.set_signal_processes(signal)
    for p in model.processes:
        if p=='qcd': continue
        model.add_lognormal_uncertainty('lumi', math.log(1.026), p)
        model.add_lognormal_uncertainty('toptag', math.log(1.200), p)
        model.add_lognormal_uncertainty('trigger', math.log(1.02), p)
    model.add_lognormal_uncertainty('ttbar_rate', math.log(1.15), 'ttbar')
    return model

def build_boosted_allhadronic_HTT_model(files, filter, signal, mcstat):
    model = build_model_from_rootfile(files, filter, root_hname_to_convention = external_to_internal, include_mc_uncertainties=mcstat)
    model.fill_histogram_zerobins()
    model.set_signal_processes(signal)
    for p in model.processes:
       if p == 'qcd': continue
       model.add_lognormal_uncertainty('lumi', math.log(1.026), p)
       model.add_lognormal_uncertainty('trigger', math.log(1.02), p)
    model.add_lognormal_uncertainty('ttbar_rate', math.log(1.15), 'ttbar')
    return model

def build_boosted_allhadronic_model(files, filter, signal, mcstat):
    model1 = build_boosted_allhadronic_CMSTT_model(files, filter, signal, mcstat)
    model2 = build_boosted_allhadronic_HTT_model(files, filter, signal, mcstat)
    model = model1
    model1.combine( model2, False)

def build_boosted_semileptonic_model(files, filter, signal, mcstat, eflag=False, muflag=False):
    """ Semileptonic high mass model"""
    model = build_model_from_rootfile(files, filter, root_hname_to_convention = external_to_internal, include_mc_uncertainties = mcstat)
    model.fill_histogram_zerobins()
    model.set_signal_processes(signal)

    for p in model.processes:
        model.add_lognormal_uncertainty('lumi', math.log(1.026), p)
        if eflag: model.add_lognormal_uncertainty('eltrig', math.log(1.01), p)

    model.add_lognormal_uncertainty('ttbar_rate', math.log(1.15), 'ttbar')
    model.add_lognormal_uncertainty('wl_rate', math.log(1.5), 'wlight')
    model.add_lognormal_uncertainty('wc_rate', math.log(2.0), 'wc')
    model.add_lognormal_uncertainty('wb_rate', math.log(2.0), 'wb')
    model.add_lognormal_uncertainty('st_rate', math.log(1.5), 'singletop')
    model.add_lognormal_uncertainty('zj_rate', math.log(2.0), 'zlight')
    model.add_lognormal_uncertainty('diboson_rate', math.log(1.5), 'diboson')

#    if muflag:
#        for obs in ['mu_0top0btag_mttbar','mu_0top1btag_mttbar','mu_1top_mttbar']:
#            for proc in ('wc', 'wb', 'wlight'):
#                model.add_asymmetric_lognormal_uncertainty('scale_vjets', -math.log(1.577), math.log(0.710), proc, obs)
#                model.add_asymmetric_lognormal_uncertainty('matching_vjets', -math.log(1.104), math.log(1.052), proc, obs)
#
#    if eflag:
#        #For categories with low statistics, use flat uncertainties instead of shape
#        #  Template for the following lines:
#        #    model.add_lognormal_uncertainty(sys, math.log( _DIFF_ ), proc, obs)
#        #  Where _DIFF_ = 2.0 * proc_sys_plus.Integral() / (proc_sys_minus.Integral() + proc_sys_plus.Integral())
#        #    after the Chi2 selection
#        for obs in ['el_0top0btag_mttbar','el_0top1btag_mttbar','el_1top_mttbar']:
#            model.add_lognormal_uncertainty('scale_vjets', math.log(0.50611), 'wb', obs)
#            model.add_lognormal_uncertainty('matching_vjets', math.log(0.98630), 'wb', obs)
#
#            model.add_lognormal_uncertainty('scale_vjets', math.log(0.50099), 'wc', obs)
#            model.add_lognormal_uncertainty('matching_vjets', math.log(1.01989), 'wc', obs)
#
#        for obs in ['el_0top0btag_mttbar','el_0top1btag_mttbar','el_1top_mttbar']:
#            model.add_lognormal_uncertainty('scale_vjets', math.log(0.49152), 'wlight', obs)
#            model.add_lognormal_uncertainty('matching_vjets', math.log(1.02911), 'wlight', obs)

    return model


import exceptions


def build_model(type, jet1 = None, mcstat = True):

    model = None

    if type == 'narrow_resonances':

        model1 = build_boosted_semileptonic_model(
            ['ljets_0627.root'],
            narrow_resonances,
            'zp*',
            mcstat,
            eflag = True, 
            muflag = True                
        )
        model2 = build_boosted_allhadronic_CMSTT_model(
            ['templates_ZpN.root'],
            narrow_resonances,
            'zp*',
            mcstat
        )
        model3 = build_boosted_allhadronic_HTT_model(
            ['htt_zprimenarrow.root'],
            narrow_resonances,
            'zp*',
            mcstat
            )
        model4 = build_dilep_model(
            ['dilep_1pctZprime.root'],
            narrow_resonances,
            'zp*',
            mcstat
            )
        model = model1
        model.combine(model2,False)
        model.combine(model3,False)
        model.combine(model4,False)

    elif type == 'wide_resonances':

        model1 = build_boosted_semileptonic_model(
            ['ljets_0627.root'],
            wide_resonances,
            'zp*',
            mcstat,
            eflag = True, 
            muflag = True                
        )
        model2 = build_boosted_allhadronic_CMSTT_model(
            ['templates_ZpW.root'],
            wide_resonances,
            'zp*',
            mcstat
        )
        model3 = build_boosted_allhadronic_HTT_model(
            ['htt_zprimewide.root'],
            wide_resonances,
            'zp*',
            mcstat
            )
        model4 = build_dilep_model(
            ['dilep_10pctZprime.root'],
            wide_resonances,
            'zp*',
            mcstat
            )
        model = model1
        model.combine(model2,False)
        model.combine(model3,False)
        model.combine(model4,False)

    elif type == 'rsg_resonances':

        model1 = build_boosted_semileptonic_model(
            ['ljets_0627.root'],
            rsg_resonances,
            'rsg*',
            mcstat,
            eflag = True,
            muflag = True
        )
        model2 = build_boosted_allhadronic_CMSTT_model(
            ['templates_RSG.root'],
            rsg_resonances,
            'rsg*',
            mcstat
        )
        model3 = build_boosted_allhadronic_HTT_model(
            ['htt_rsg.root'],
            rsg_resonances,
            'rsg*',
            mcstat
            )
        model4 = build_dilep_model(
            ['dilep_GKK.root'],
            rsg_resonances,
            'rsg*',
            mcstat
            )
        model = model1
        model.combine(model2,False)
        model.combine(model3,False)
        model.combine(model4,False)




    else:

        raise exceptions.ValueError('Type %s is undefined' % type)

    for p in model.distribution.get_parameters():
        d = model.distribution.get_distribution(p)
        if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0:
            model.distribution.set_distribution_parameters(p, range = [-5.0, 5.0])
        #if 'rate' in p:
        #    if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0:
        #        model.distribution.set_distribution_parameters(p, range = [-5.0, 5.0])
        #else:
        #    if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0:
        #        model.distribution.set_distribution_parameters(p, range = [-0.0, 0.0])
	if p == 'toptag' or p == 'btag' or p == 'subjbtag':
	     model.distribution.set_distribution_parameters(p, range = [-inf, inf])

    return model


model = build_model('narrow_resonances')
model_summary(model)


