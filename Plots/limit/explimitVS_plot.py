#!/usr/bin/env python
from ROOT import ROOT, TCanvas, TColor, TGraph, TLegend, TPaveText
from read_input_file import *

label_TL = '#font[62]{CMS}'
label_TR = '19.7 fb^{-1} (8 TeV)'

signal_dict = {
  'n': ['Z\'', '#splitline{95% CL expected}{Z\' 1% width}'],
  'w': ['Z\'', '#splitline{95% CL expected}{Z\' 10% width}'],
  'r': ['g_{KK}', '#splitline{95% CL expected}{KK gluon}']
}

def get_expectedlimit_graph(input_file_, title_, linestyle_, linecolor_):

    mpoints = get_limits_from_file(input_file_)
    m = [mp.mass for mp in mpoints]
    exp = [mp.exp for mp in mpoints]

    g = TGraph()
    for a in range(0,len(mpoints)):
        g.SetPoint(a,m[a],exp[a])

    g.SetTitle(title_)
    g.SetLineStyle(linestyle_)
    g.SetLineColor(linecolor_)
    g.SetLineWidth(5)

    return g

def explimitVS_plot(input_dict_, signal_, oname_):

    graphs = list()
    for i in input_dict_:
        graphs.append(get_expectedlimit_graph(i[0], i[1], i[2], i[3]))

    leg = TLegend(0.58,0.633,0.969,0.908)
    leg.SetFillColor(0)
    leg.SetBorderSize(0)
    for g in graphs: leg.AddEntry(g,g.GetTitle(),'l')

    text_TL = TPaveText(0.14,0.830,0.44,0.900,'NDC')
    text_TL.AddText(label_TL)
    text_TL.SetFillColor(0)
    text_TL.SetTextAlign(12)
    text_TL.SetTextSize(0.06)
    text_TL.SetTextFont(42)

    text_TR = TPaveText(0.586,0.923,0.999,0.997,'NDC')
    text_TR.AddText(label_TR)
    text_TR.SetFillColor(0)
    text_TR.SetTextAlign(32)
    text_TR.SetTextSize(0.055)
    text_TR.SetTextFont(42)

    sticker = TPaveText(0.14,0.685,0.425,0.830,'NDC')
    #sticker = TPaveText(0.14,0.800,0.425,0.910,'NDC')
    sticker.AddText(signal_dict[signal_][1])
    sticker.SetFillColor(0)
    sticker.SetTextAlign(12)
    sticker.SetTextFont(42)

    c = TCanvas('c','c',950,750)
    c.SetTopMargin(0.08)
    c.SetRightMargin(0.02)
    c.SetBottomMargin(0.135)
    c.SetLeftMargin(0.11)
    #c.SetGrid()
    c.SetLogy()

    hr = c.DrawFrame(0.401,0.001,3.099,1000)

    for g in graphs: g.Draw('l')

    hr.GetXaxis().SetTitle('M_{'+signal_dict[signal_][0]+'} [TeV]')
    hr.GetYaxis().SetTitle('Upper limit on #sigma_{'+signal_dict[signal_][0]+'} #times B('+signal_dict[signal_][0]+' #rightarrow t#bar{t}) [pb]')
    hr.GetXaxis().SetTitleSize(0.055)
    hr.GetYaxis().SetTitleSize(0.055)
    hr.GetXaxis().SetTitleFont(42)
    hr.GetYaxis().SetTitleFont(42)
    hr.GetXaxis().SetTitleOffset(1.00)
    hr.GetYaxis().SetTitleOffset(0.98)
    hr.GetXaxis().SetLabelSize(0.045)
    hr.GetYaxis().SetLabelSize(0.045)

    c.Update()
    text_TL.Draw('same')
    text_TR.Draw('same')
    sticker.Draw('same')
    leg.Draw()

    c.SaveAs(oname_+'.pdf')
    c.Close()

###

c_BlueT0        = TColor.GetColor( "#112288" );
c_BlueT1        = TColor.GetColor( "#2255cc" );
c_BlueT2        = TColor.GetColor( "#4488dd" );
c_BlueT3        = TColor.GetColor( "#99bbff" );
c_BlueT4        = TColor.GetColor( "#99bbff" );
c_BlueT5        = TColor.GetColor( "#aaddff" );

c_RedT0         = TColor.GetColor( "#660000" );
c_RedT1         = TColor.GetColor( "#B20000" );
c_RedT2         = TColor.GetColor( "#FF0000" );
c_RedT3         = TColor.GetColor( "#FF4D4D" );
c_RedT4         = TColor.GetColor( "#FF9999" );
c_RedT5         = TColor.GetColor( "#FFCCCC" );

c_LightOrange   = TColor.GetColor( "#ffcc00" );
c_VLightOrange  = TColor.GetColor( "#ffdd44" );
c_FaintOrange   = TColor.GetColor( "#FFEBCD" );
c_MediumOrange  = TColor.GetColor( "#FFCC00" );
c_DarkOrange    = TColor.GetColor( "#ff6600" );
c_VDarkOrange   = TColor.GetColor( "#aa4400" );

c_GreenT0       = TColor.GetColor( "#142907" );
c_GreenT1       = TColor.GetColor( "#29520E" );
c_GreenT2       = TColor.GetColor( "#478F18" );
c_GreenT3       = TColor.GetColor( "#66CC22" );
c_GreenT4       = TColor.GetColor( "#94DB64" );
c_GreenT5       = TColor.GetColor( "#C2EBA7" );

for s in signal_dict:

    input_tuple = (
      ('txt/limits_'+s+'_com_0828.txt', 'combination'       , 1, ROOT.kBlack),
      ('txt/limits_'+s+'_dil_0828.txt', 'dilepton'          , 1, c_GreenT3),
      ('txt/limits_'+s+'_ltr.txt'     , 'lepton+jets (threshold)', 2, c_BlueT3),
      ('txt/limits_'+s+'_lep_0828.txt', 'lepton+jets (boosted)'  , 1, c_BlueT1),
      ('txt/limits_'+s+'_htt_0828.txt', 'all-hadronic (low-mass)'  , 3, c_DarkOrange),
      ('txt/limits_'+s+'_ctt_0828.txt', 'all-hadronic (high-mass)'  , 5, c_RedT1)
      #('txt/limits_'+s+'_B2G13001.txt', 'PRL'        , 2, ROOT.kGray+1),
    )

    explimitVS_plot(input_tuple, s, s+'_explimitVS')
#    explimitVS_plot(input_tuple, s, s+'_pub_comparison')
