#!/usr/bin/env python
from ROOT import ROOT, TCanvas, TColor, TGraph, TLegend, TPaveText
from read_input_file import *

label_TL = '#font[62]{CMS}'
label_TR = '19.7 fb^{-1} (8 TeV)'

signal_dict = {
  'n': ['Z\'', '#splitline{95% CL expected}{Z\' 1.2% width}'],
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
    g.SetLineWidth(4)

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

for s in signal_dict:

    input_tuple = (
      ('txt/limits_'+s+'_dil_0731.txt', 'dilepton'          , 1, ROOT.kViolet),
      ('txt/limits_'+s+'_ltr.txt'     , 'l+jets (threshold)', 1, ROOT.kOrange+1),
      ('txt/limits_'+s+'_lep_0731.txt', 'l+jets (boosted)'  , 1, ROOT.kRed),
      ('txt/limits_'+s+'_htt_0731.txt', 'hadronic (HEPTT)'  , 1, ROOT.kBlue),
      ('txt/limits_'+s+'_ctt_0731.txt', 'hadronic (CMSTT)'  , 1, ROOT.kGreen+1),
      ('txt/limits_'+s+'_B2G13001.txt', 'B2G-13-001'        , 2, ROOT.kGray+1),
      ('txt/limits_'+s+'_com_0731.txt', 'combination'       , 1, ROOT.kBlack)
    )

    explimitVS_plot(input_tuple, s, s+'_explimitVS')
