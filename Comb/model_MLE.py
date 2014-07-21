### Filter definitions ###

def narrow_resonances(hname):
    pname = hname.split('__')[1]
    if ('Wide' in pname) or ('RSgluon' in pname): return False
    elif ('Zprime' in pname):
        mass = pname.strip('Zprime')
        mass_list = [750, 1000, 1250, 1500, 2000, 3000] 
        return float(mass) in mass_list
    else: return True

def wide_resonances(hname):
    pname = hname.split('__')[1]
    if ('RSgluon' in pname): return False
    elif ('Zprime' in pname) and ('Wide' not in pname): return False
    elif ('ZprimeWide' in pname):
        mass = pname.strip('ZprimeWide')
        mass_list = [750, 1000, 1250, 1500, 2000, 3000] 
        return float(mass) in mass_list
    else: return True

def rsg_resonances(hname):
    pname = hname.split('__')[1]
    if ('Zprime' in pname): return False
    elif ('RSgluon' in pname):
        mass = pname.strip('RSgluon')
        mass_list = [700, 1000, 1400, 1500, 1800, 2000, 2500, 3000] 
        return float(mass) in mass_list
    else: return True


def build_dilep_model(files, filter, signal, mcstat):
    model = build_model_from_rootfile(files, filter, include_mc_uncertainties = mcstat)
    model.fill_histogram_zerobins()
    model.set_signal_processes(signal)

    model.add_lognormal_uncertainty('ttbar_rate',   math.log(1.15), 'ttbar')
    model.add_lognormal_uncertainty('zj_rate',      math.log(1.50), 'zlight')
    model.add_lognormal_uncertainty('st_rate',      math.log(1.23), 'singletop')
    model.add_lognormal_uncertainty('diboson_rate', math.log(1.20), 'diboson')

    for p in model.processes:
        model.add_lognormal_uncertainty('lumi', math.log(1.026), p)
    return model

def build_boosted_allhadronic_CMSTT_model(files, filter, signal, mcstat):
    """ All hadronic high mass model """    
    model = build_model_from_rootfile(files, filter, include_mc_uncertainties = mcstat)
    model.fill_histogram_zerobins()
    model.set_signal_processes(signal)
    for p in model.processes:
        if p=='qcd': continue
        model.add_lognormal_uncertainty('lumi', math.log(1.026), p)
        model.add_lognormal_uncertainty('toptag', math.log(1.400), p)
        model.add_lognormal_uncertainty('trigger', math.log(1.02), p)
    model.add_lognormal_uncertainty('ttbar_rate', math.log(1.15), 'ttbar')
    return model

def build_boosted_allhadronic_HTT_model(files, filter, signal, mcstat):
    model = build_model_from_rootfile(files, filter, include_mc_uncertainties = mcstat)
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

def build_boosted_semileptonic_model(files, filter, signal, mcstat):
    model = build_model_from_rootfile(files, filter, include_mc_uncertainties = mcstat)
    model.fill_histogram_zerobins()
    model.set_signal_processes(signal)

    for p in model.processes:
        model.add_lognormal_uncertainty('lumi', math.log(1.026), p)
        for obs in ['el_0top0btag_mttbar','el_0top1btag_mttbar','el_1top_mttbar']:
            model.add_lognormal_uncertainty('eleORjet_trig', math.log(1.01), p, obs)

    model.add_lognormal_uncertainty('ttbar_rate',   math.log(1.15), 'ttbar')
    model.add_lognormal_uncertainty('wl_rate',      math.log(1.09), 'wlight')
    model.add_lognormal_uncertainty('wc_rate',      math.log(1.23), 'wc')
    model.add_lognormal_uncertainty('wb_rate',      math.log(1.23), 'wb')
    model.add_lognormal_uncertainty('st_rate',      math.log(1.23), 'singletop')
    model.add_lognormal_uncertainty('zj_rate',      math.log(1.50), 'zlight')
    model.add_lognormal_uncertainty('diboson_rate', math.log(1.20), 'diboson')

    return model


import exceptions

def build_model(type, mcstat = True):

    model_ljets = None
    model_cmstt = None
    model_heptt = None
    model_dilep = None

    if type == 'narrow_resonances':

        model_ljets = build_boosted_semileptonic_model(
            ['ljets_all.root'],
            narrow_resonances,
            'Zprime*',
            mcstat
        )
        model_cmstt = build_boosted_allhadronic_CMSTT_model(
            ['CMSTT_zpn.root'],
            narrow_resonances,
            'Zprime*',
            mcstat
        )
        model_heptt = build_boosted_allhadronic_HTT_model(
            ['HEPTT_zpn.root'],
            narrow_resonances,
            'Zprime*',
            mcstat
        )
        model_dilep = build_dilep_model(
            ['dilep_zpn.root'],
            narrow_resonances,
            'Zprime*',
            mcstat
        )

    elif type == 'wide_resonances':

        model_ljets = build_boosted_semileptonic_model(
            ['ljets_all.root'],
            wide_resonances,
            'ZprimeWide*',
            mcstat
        )
        model_cmstt = build_boosted_allhadronic_CMSTT_model(
            ['CMSTT_zpw.root'],
            wide_resonances,
            'ZprimeWide*',
            mcstat
        )
        model_heptt = build_boosted_allhadronic_HTT_model(
            ['HEPTT_zpw.root'],
            wide_resonances,
            'ZprimeWide*',
            mcstat
        )
        model_dilep = build_dilep_model(
            ['dilep_zpw.root'],
            wide_resonances,
            'ZprimeWide*',
            mcstat
        )

    elif type == 'rsg_resonances':

        model_ljets = build_boosted_semileptonic_model(
            ['ljets_all.root'],
            rsg_resonances,
            'RSgluon*',
            mcstat
        )
        model_cmstt = build_boosted_allhadronic_CMSTT_model(
            ['CMSTT_rsg.root'],
            rsg_resonances,
            'RSgluon*',
            mcstat
        )
        model_heptt = build_boosted_allhadronic_HTT_model(
            ['HEPTT_rsg.root'],
            rsg_resonances,
            'RSgluon*',
            mcstat
        )
        model_dilep = build_dilep_model(
            ['dilep_rsg.root'],
            rsg_resonances,
            'RSgluon*',
            mcstat
        )

    else: raise exceptions.ValueError('Type %s is undefined' % type)

    model = model_ljets
    model.combine(model_cmstt,False)
    model.combine(model_heptt,False)
    model.combine(model_dilep,False)

    for p in model.signal_processes:
        model.scale_predictions(0.1,p)
        if (p == 'Zprime1250') or (p == 'Zprime1500') or (p == 'Zprime2000') or (p == 'Zprime3000'): model.scale_predictions(0.01,p)
        if (p == 'ZprimeWide1250') or (p == 'ZprimeWide1500') or (p == 'ZprimeWide2000') or (p == 'ZprimeWide3000'): model.scale_predictions(0.01,p)
        if ('RSgluon' in p) and (float(p.strip('RSgluon')) >= 1200): model.scale_predictions(0.01,p)

    for p in model.distribution.get_parameters():
        d = model.distribution.get_distribution(p)
        if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0:
            model.distribution.set_distribution_parameters(p, range = [-5.0, 5.0])
        if p == 'toptag' or p == 'subjbtag':
            model.distribution.set_distribution_parameters(p, width = float("inf"))
        if (p == 'misErr'): model.distribution.set_distribution_parameters(p, width = float(0.0001))
        if (p == 'q2'): model.distribution.set_distribution_parameters(p, width = float(0.0001))
        if (p == 'q2_wjets'): model.distribution.set_distribution_parameters(p, width = float(0.0001))
        if (p == 'matching_wjets'): model.distribution.set_distribution_parameters(p, width = float(0.0001))
        if (p == 'pdf'): model.distribution.set_distribution_parameters(p, width = float(0.0001))

    return model


#model = build_model('narrow_resonances')
#model_summary(model)
