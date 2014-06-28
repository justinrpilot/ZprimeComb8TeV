
### Filter definitions ###

def narrow_resonances(hname):
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
         'ZprimeNrw_1000':'zp1000w1p',
         'ZprimeNrw_1100':'zp1100w1p',
         'ZprimeNrw_1200':'zp1200w1p',
         'ZprimeNrw_1300':'zp1300w1p',
         'ZprimeNrw_1400':'zp1400w1p',
         'ZprimeNrw_1500':'zp1500w1p',
         'ZprimeNrw_1600':'zp1600w1p',
         'ZprimeNrw_1700':'zp1700w1p',
         'ZprimeNrw_1800':'zp1800w1p',
         'ZprimeNrw_1900':'zp1900w1p',
         'ZprimeNrw_2000':'zp2000w1p',
         'ZprimeNrw_2100':'zp2100w1p',
         'ZprimeNrw_2200':'zp2200w1p',
         'ZprimeNrw_2300':'zp2300w1p',
         'ZprimeNrw_2400':'zp2400w1p',
         'ZprimeNrw_2500':'zp2500w1p',
         'ZprimeNrw_2600':'zp2600w1p',
         'ZprimeNrw_2700':'zp2700w1p',
         'ZprimeNrw_2800':'zp2800w1p',
         'ZprimeNrw_2900':'zp2900w1p',
         'ZprimeNrw_3000':'zp3000w1p',
         'ZprimeNrw_3100':'zp3100w1p',
         'ZprimeNrw_3200':'zp3200w1p',
         'ZprimeNrw_3300':'zp3300w1p',
         'ZprimeNrw_3400':'zp3400w1p',
         'ZprimeNrw_3500':'zp3500w1p',
         'ZprimeNrw_3600':'zp3600w1p',
         'ZprimeNrw_3700':'zp3700w1p',
         'ZprimeNrw_3800':'zp3800w1p',
         'ZprimeNrw_3900':'zp3900w1p',
         'ZprimeNrw_4000':'zp4000w1p',
         'ZprimeWde_1000':'zp1000w10p',
         'ZprimeWde_1100':'zp1100w10p',
         'ZprimeWde_1200':'zp1200w10p',
         'ZprimeWde_1300':'zp1300w10p',
         'ZprimeWde_1400':'zp1400w10p',
         'ZprimeWde_1500':'zp1500w10p',
         'ZprimeWde_1600':'zp1600w10p',
         'ZprimeWde_1700':'zp1700w10p',
         'ZprimeWde_1800':'zp1800w10p',
         'ZprimeWde_1900':'zp1900w10p',
         'ZprimeWde_2000':'zp2000w10p',
         'ZprimeWde_2100':'zp2100w10p',
         'ZprimeWde_2200':'zp2200w10p',
         'ZprimeWde_2300':'zp2300w10p',
         'ZprimeWde_2400':'zp2400w10p',
         'ZprimeWde_2500':'zp2500w10p',
         'ZprimeWde_2600':'zp2600w10p',
         'ZprimeWde_2700':'zp2700w10p',
         'ZprimeWde_2800':'zp2800w10p',
         'ZprimeWde_2900':'zp2900w10p',
         'ZprimeWde_3000':'zp3000w10p',
         'ZprimeWde_3100':'zp3100w10p',
         'ZprimeWde_3200':'zp3200w10p',
         'ZprimeWde_3300':'zp3300w10p',
         'ZprimeWde_3400':'zp3400w10p',
         'ZprimeWde_3500':'zp3500w10p',
         'ZprimeWde_3600':'zp3600w10p',
         'ZprimeWde_3700':'zp3700w10p',
         'ZprimeWde_3800':'zp3800w10p',
         'ZprimeWde_3900':'zp3900w10p',
         'ZprimeWde_4000':'zp4000w10p',
         'ttjets':'ttbar'
         }
    for old_pname in m:
        if ('__' + old_pname) in hname: hname = hname.replace('__' + old_pname, '__' + m[old_pname])
    print ' changed to ' + hname
    return hname


def build_dilep_model(files, filter, signal, mcstat):
    # Read in and build the model automatically from the histograms in the root file. 
    # This model will contain all shape uncertainties given according to the templates
    # which also includes rate changes according to the alternate shapes.
    # For more info about this model and naming conventuion, see documentation
    # of build_model_from_rootfile.
    model = build_model_from_rootfile(files, filter, include_mc_uncertainties = mcstat)
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
    model.add_lognormal_uncertainty('zj_rate',        math.log(2.0),  'zlight'       )
    model.add_lognormal_uncertainty('st_rate',        math.log(1.50), 'singletop')
    model.add_lognormal_uncertainty('diboson_rate',   math.log(1.5),  'diboson'       )

    for p2 in model.processes:
        model.add_lognormal_uncertainty('lumi', math.log(1.026), p2)
    return model


def build_boosted_allhadronic_CMSTT_model(files, filter, signal, mcstat):
    """ All hadronic high mass model """    
    model = build_model_from_rootfile(files, filter, include_mc_uncertainties = mcstat)
    model.fill_histogram_zerobins()
    model.set_signal_processes(signal)
    for p in model.processes:
        if p=='qcd': continue
        model.add_lognormal_uncertainty('lumi', math.log(1.026), p)
        model.add_lognormal_uncertainty('subjet_scalefactor', math.log(1.084), p)
        model.add_lognormal_uncertainty('trigger', math.log(1.02), p)
    model.add_lognormal_uncertainty('ttbar_rate', math.log(1.15), 'ttbar')
    return model

def build_boosted_allhadronic_HTT_model(files, filter, signal, mcstat):
    model = build_model_from_rootfile(files, filter, signal, root_hname_to_convention = external_to_internal, include_mc_uncertainties=mcstat)
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
    model = build_model_from_rootfile(files, filter, include_mc_uncertainties = mcstat)
    model.fill_histogram_zerobins()
    model.set_signal_processes(signal)
    for p in model.processes:
        model.add_lognormal_uncertainty('lumi', math.log(1.026), p)

    model.add_lognormal_uncertainty('zj_rate', math.log(2.0), 'zlight')
    model.add_lognormal_uncertainty('wj_rate', math.log(1.5), 'wlight')
    model.add_lognormal_uncertainty('wj_rate', math.log(1.5), 'wb')
    model.add_lognormal_uncertainty('wj_rate', math.log(1.5), 'wc')
    model.add_lognormal_uncertainty('wb_rate', math.log(1.87), 'wb')
    model.add_lognormal_uncertainty('wc_rate', math.log(1.87), 'wc')
    model.add_lognormal_uncertainty('ttbar_rate', math.log(1.15), 'ttbar')
    model.add_lognormal_uncertainty('st_rate', math.log(1.5), 'singletop')
    model.add_lognormal_uncertainty('diboson_rate', math.log(1.5), 'diboson')

    if muflag:
        for obs in ['mu_0btag_mttbar']:
            for proc in ('wc', 'wb'):
                model.add_asymmetric_lognormal_uncertainty('scale_vjets', -math.log(1.577), math.log(0.710), proc, obs)
                model.add_asymmetric_lognormal_uncertainty('matching_vjets', -math.log(1.104), math.log(1.052), proc, obs)
        for obs in ['mu_1btag_mttbar']:
            for proc in ('wc', 'wb', 'wlight'):
                model.add_asymmetric_lognormal_uncertainty('scale_vjets', -math.log(1.577), math.log(0.710), proc, obs)
                model.add_asymmetric_lognormal_uncertainty('matching_vjets', -math.log(1.104), math.log(1.052), proc, obs)

    if eflag:
        for obs in ['el_0btag_mttbar']:
            for proc in ('wc', 'wb'):
                model.add_asymmetric_lognormal_uncertainty('scale_vjets', -math.log(1.584), math.log(0.690), proc, obs)
                model.add_asymmetric_lognormal_uncertainty('matching_vjets', -math.log(1.0447), math.log(1.0706), proc, obs)
            for proc in model.processes:
                model.add_lognormal_uncertainty('elid_rate', math.log(1.05), proc, obs)            
        for obs in ['el_1btag_mttbar']:
            for proc in ('wc', 'wb', 'wlight'):
                model.add_asymmetric_lognormal_uncertainty('scale_vjets', -math.log(1.584), math.log(0.690), proc, obs)
                model.add_asymmetric_lognormal_uncertainty('matching_vjets', -math.log(1.0447), math.log(1.0706), proc, obs)
            for proc in model.processes:
                model.add_lognormal_uncertainty('elid_rate', math.log(1.05), proc, obs)
    
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
            ['ZpN_templates_May20.root'],
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
            ['ZpW_templates_May20.root'],
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
            ['RSG_templates_May20.root'],
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

    return model
