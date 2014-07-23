#!/bin/zsh

# CMSTT analysis, subjet b-tagging scale factor
root -l -b -q 'scale_subjb.C("CMSTT_zpn.root")'
root -l -b -q 'scale_subjb.C("CMSTT_zpw.root")'
root -l -b -q 'scale_subjb.C("CMSTT_rsg.root")'

# CMSTT, rates and top-tagging
root -l -b -q 'scale.C("CMSTT_zpn_subjb.root")'
root -l -b -q 'scale.C("CMSTT_zpw_subjb.root")'
root -l -b -q 'scale.C("CMSTT_rsg_subjb.root")'

# l+jets rates and top-tagging
root -l -b -q 'scale.C("ljets_all.root")'

# HEPTT rates
root -l -b -q 'scale.C("HEPTT_zpn.root")'
root -l -b -q 'scale.C("HEPTT_zpw.root")'
root -l -b -q 'scale.C("HEPTT_rsg.root")'

# dilepton rates
root -l -b -q 'scale.C("dilep_zpn.root")'
root -l -b -q 'scale.C("dilep_zpw.root")'
root -l -b -q 'scale.C("dilep_rsg.root")'

