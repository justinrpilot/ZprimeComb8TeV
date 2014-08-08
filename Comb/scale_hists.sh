#!/bin/zsh

# CMSTT analysis, subjet b-tagging scale factor
root -l -b -q 'scale_subjb.C("CMSTT_zpn.root")'
root -l -b -q 'scale_subjb.C("CMSTT_zpw.root")'
root -l -b -q 'scale_subjb.C("CMSTT_rsg.root")'

# CMSTT, rates and top-tagging
root -l -b -q 'scale.C("CMSTT_zpn_subjb.root")'
root -l -b -q 'scale.C("CMSTT_zpw_subjb.root")'
root -l -b -q 'scale.C("CMSTT_rsg_subjb.root")'

mv CMSTT_zpn_subjb_scaled.root CMSTT_zpn_scaled.root
mv CMSTT_zpw_subjb_scaled.root CMSTT_zpw_scaled.root
mv CMSTT_rsg_subjb_scaled.root CMSTT_rsg_scaled.root

rm CMSTT_zpn_subjb.root CMSTT_zpw_subjb.root CMSTT_rsg_subjb.root

# l+jets rates and top-tagging, also topmistag
root -l -b -q 'scale_topmistag.C("ljets_all.root")'
root -l -b -q 'scale.C("ljets_all_topmistag_0.83.root")'
mv ljets_all_topmistag_0.83_scaled.root ljets_all_scaled.root


# dilepton rates
root -l -b -q 'scale.C("dilep_zpn.root")'
root -l -b -q 'scale.C("dilep_zpw.root")'
root -l -b -q 'scale.C("dilep_rsg.root")'

# HEPTT rates
root -l -b -q 'scale.C("HEPTT_zpn.root")'
root -l -b -q 'scale.C("HEPTT_zpw.root")'
root -l -b -q 'scale.C("HEPTT_rsg.root")'
