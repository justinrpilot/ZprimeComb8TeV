#!/usr/bin/env python
from ROOT import ROOT, TCanvas, TColor, TGraph, TLegend, TPaveText, TString, TLine
from read_input_file import *
from theory_XsecBR import *

label_TL = '#font[62]{CMS}'
label_TR = '19.7 fb^{-1} (8 TeV)'

signal_dict = {
  'n': ['Z\'', 'Z\' 1.2% width'],
  'w': ['Z\'', 'Z\' 10% width'],
  'r': ['g_{KK}', 'KK gluon']
}

def limit_canvas(limits_, signal_, oname_):

    m = [mp.mass for mp in limits_]
    exp = [mp.exp for mp in limits_]
    exp68up = [mp.exp68up for mp in limits_]
    exp68dn = [mp.exp68dn for mp in limits_]
    exp95up = [mp.exp95up for mp in limits_]
    exp95dn = [mp.exp95dn for mp in limits_]
    obs = [mp.obs for mp in limits_]

    N = len(limits_)
    gExp = TGraph()
    g68 = TGraph(2*N)
    g95 = TGraph(2*N)
    gObs = TGraph()
    gTH = get_theory_XsecBR_graph(signal_)

    for a in range(0,N):
        gExp.SetPoint(a,m[a],exp[a])
        gObs.SetPoint(a,m[a],obs[a])
        g68.SetPoint(a,m[a],exp68dn[a])
        g95.SetPoint(a,m[a],exp95dn[a])
        g68.SetPoint(N+a,m[N-a-1],exp68up[N-a-1])
        g95.SetPoint(N+a,m[N-a-1],exp95up[N-a-1])

    trans = 0
    up = 0
    if signal_ == 'n':
        trans = 0.770776
        up = 3
    if signal_ == 'w':
        trans = 0.836432
        up = 10
    if signal_ == 'r':
        trans = 0.899902
        up = 4

    gExp.SetLineStyle(2)
    gExp.SetLineWidth(4)
    gExp.SetLineColor(TColor.GetColor('#112288'))

    g68.SetLineStyle(1)
    g68.SetLineWidth(0)
    g68.SetLineColor(ROOT.kBlack)
    g68.SetFillColor(TColor.GetColor('#4488dd'))

    g95.SetLineStyle(1)
    g95.SetLineWidth(0)
    g95.SetLineColor(ROOT.kBlack)
    g95.SetFillColor(TColor.GetColor('#99bbff'))

    gObs.SetLineStyle(1)
    gObs.SetLineWidth(4)
    gObs.SetLineColor(ROOT.kBlack)
    gObs.SetMarkerStyle(21)
    gObs.SetMarkerSize(0.8)

    gTH.SetLineStyle(7)
    gTH.SetLineWidth(4)
    gTH.SetLineColor(ROOT.kRed+1)

    leg = TLegend(0.58,0.633,0.969,0.908)
    leg.SetFillColor(0)
    leg.SetBorderSize(0)
    leg.AddEntry(gExp,'Expected (95% CL)','l')
    leg.AddEntry(gObs,'Observed (95% CL)','l')
    leg.AddEntry(gTH,signal_dict[signal_][1],'l')
    leg.AddEntry(g68,'#pm1#sigma Expected','f')
    leg.AddEntry(g95,'#pm2#sigma Expected','f')

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

    c = TCanvas('c','c',950,750)
    c.SetTopMargin(0.08)
    c.SetRightMargin(0.02)
    c.SetBottomMargin(0.135)
    c.SetLeftMargin(0.11)
    #c.SetGrid()
    c.SetLogy()

    hr = c.DrawFrame(0.401,0.001,3.099,1000)

    gExp.Sort()

    g95.Draw('f')
    g68.Draw('f')
    gTH.Draw('PL')
    gExp.Draw('L')

    gObs.Sort()
    gObs.Draw('L')

    hr.GetXaxis().SetTitle('M_{'+signal_dict[signal_][0]+'} [TeV]')
    hr.GetYaxis().SetTitle('Upper limit on #sigma_{'+signal_dict[signal_][0]+'} #times B('+signal_dict[signal_][0]+' #rightarrow t#bar{t}) [pb]')
    #hr.GetYaxis().SetTitle('\\mathrm{Upper~limit~on~}\\sigma_{'+signal_dict[signal_][0]+'}\\times\\mathscr{B}('+signal_dict[signal_][0]+' \\rightarrow t\\bar{t}) [pb]')
    hr.GetXaxis().SetTitleSize(0.055)
    hr.GetYaxis().SetTitleSize(0.055)
    hr.GetXaxis().SetTitleFont(42)
    hr.GetYaxis().SetTitleFont(42)
    hr.GetXaxis().SetTitleOffset(1.00)
    hr.GetYaxis().SetTitleOffset(0.98)
    hr.GetXaxis().SetLabelSize(0.045)
    hr.GetYaxis().SetLabelSize(0.045)

    name = TString(oname_)
    if name.Contains("com"):
        tl = TLine(trans, 1e-3, trans, up)
        tl.SetLineStyle(ROOT.kDashed)
        tl.SetLineColor(ROOT.kGray+1)
        tl.SetLineWidth(3)
        tl.Draw()

    c.Update()
    text_TL.Draw('same')
    text_TR.Draw('same')
    leg.Draw()

    c.SaveAs(oname_+'.pdf')
    c.Close()

def limit_plot(ifile_, signal_, output_name_):

    limits = get_limits_from_file(ifile_)
    limit_canvas(limits, signal_, output_name_)

###

for s in signal_dict:
    limit_plot('txt/limits_'+s+'_com_0828.txt', s, s+'_combo')
    limit_plot('txt/limits_'+s+'_lep_0828.txt', s, s+'_ljets')
    limit_plot('txt/limits_'+s+'_had_0828.txt', s, s+'_alhad')
    limit_plot('txt/limits_'+s+'_ctt_0828.txt', s, s+'_cmstt')
    limit_plot('txt/limits_'+s+'_htt_0828.txt', s, s+'_heptt')
    limit_plot('txt/limits_'+s+'_dil_0828.txt', s, s+'_dilep')
