void draw(TString fname = "2dcut_dRjet_muon.root")
{

  gROOT->SetStyle("Plain");
  gStyle->SetOptStat(0);
  gStyle -> SetPadTickX(1);
  gStyle -> SetPadTickY(1);

  gStyle->SetPadBorderMode(0);
  gStyle->SetPadColor(kWhite);
  gStyle->SetPadGridX(false);
  gStyle->SetPadGridY(false);
  gStyle->SetGridColor(0);
  gStyle->SetGridStyle(3);
  gStyle->SetGridWidth(1);

  gStyle->SetFrameBorderMode(0);
  gStyle->SetFrameBorderSize(1);
  gStyle->SetFrameFillColor(0);
  gStyle->SetFrameFillStyle(0);
  gStyle->SetFrameLineColor(1);
  gStyle->SetFrameLineStyle(1);
  gStyle->SetFrameLineWidth(2);

  gStyle->SetTitleFont(42, "XYZ");
  gStyle->SetLabelFont(42, "XYZ");

  gStyle->SetAxisColor(1, "XYZ");
  gStyle->SetStripDecimals(kTRUE);
  gStyle->SetTickLength(0.03, "XYZ");
  gStyle->SetNdivisions(510, "XYZ");

  gStyle->UseCurrentStyle();

  TFile* file = new TFile(fname, "READ");
  
  Int_t CanWidth;
  Int_t CanHeight;
  CanWidth = 400;
  CanHeight = 400;

  //TPostScript* m_ps = new TPostScript(filename, 113);

  // set up the canvas
  TCanvas* m_can = new TCanvas("canvas","Control Plots", CanWidth, CanHeight);

  Float_t yplot = 0.65;
  Float_t yratio = 0.34;

  // set up the coordinates of the two pads:
  Float_t y1, y2, y3;
  y3 = 0.99; 
  y2 = y3-yplot;
  y1 = y2-yratio;
  Float_t x1, x2;
  x1 = 0.01; 
  x2 = 0.99; 

  TPad* m_rp1_top = new TPad("pad1", "Control Plots 2", x1, y2, x2, y3);
  TPad* m_rp1 = new TPad("rp1", "Ratio2", x1, y1, x2, y2);
       
  m_rp1_top->SetTopMargin(0.065); m_rp1_top->SetBottomMargin(0.0); m_rp1_top->SetLeftMargin(0.19); m_rp1_top->SetRightMargin(0.05);
  m_rp1->SetTopMargin(0.0); m_rp1->SetBottomMargin(0.35); m_rp1->SetLeftMargin(0.19); m_rp1->SetRightMargin(0.05);

  TGraphAsymmErrors* data_eff = (TGraphAsymmErrors*) file->Get("DATA_eff");
  TGraphAsymmErrors* mc_eff = (TGraphAsymmErrors*) file->Get("MC_eff");

  m_rp1_top->Draw();
  m_rp1->Draw();

  m_rp1_top->cd();

  data_eff->SetMarkerStyle(20);
  data_eff->SetMarkerColor(kBlack);
  data_eff->SetLineColor(kBlack);
  data_eff->Draw("AP");
  double x,y;

  mc_eff->SetMarkerStyle(25);
  mc_eff->SetMarkerColor(kRed+1);
  mc_eff->SetLineColor(kRed+1);
    
  TH1F* painter = data_eff->GetHistogram();

  painter->GetXaxis()->SetTitle("#DeltaR(l,jet)");
  painter->GetYaxis()->SetTitle("Efficiency");
  painter->SetTitle("");
  painter->GetXaxis()->SetRangeUser(0, 0.5);
  painter->GetYaxis()->SetRangeUser(0.0001, 1.0);

  painter->GetXaxis()->SetTickLength(0.05);
  
  // y-axis
  painter->GetYaxis()->SetTitleSize(0.09);
  painter->GetYaxis()->SetLabelSize(0.07);
  painter->GetYaxis()->SetLabelOffset(0.01);
  painter->GetYaxis()->SetTitleOffset(0.89);
  painter->GetYaxis()->SetTickLength(0.02);

  //TLine* l = new TLine(painter->GetXaxis()->GetXmin(), 1., painter->GetXaxis()->GetXmax(), 1.);
  //l->SetLineColor(kBlue);
  //l->Draw();

  mc_eff->Draw("Psame");
  data_eff->Draw("Psame");

  TString infotext = TString::Format("19.7 fb^{-1} (8 TeV)");
  TLatex *text1 = new TLatex(3.5, 24, infotext);
  text1->SetNDC();
  text1->SetTextAlign(33);
  text1->SetX(0.95);
  text1->SetTextFont(42);
  text1->SetTextSize(0.06);
  text1->SetY(1.);
  text1->Draw();

  TString cmstext = "CMS";
  TLatex *text2 = new TLatex(3.5, 24, cmstext);
  text2->SetNDC();
  text2->SetTextAlign(13);
  text2->SetX(0.24);
  text2->SetTextFont(62);
  text2->SetTextSize(0.08);
  text2->SetY(0.87);
  text2->Draw();

  TString cattext = "Z/#gamma^{*}(#rightarrow ee)+jets";
  if (fname.Contains("mu")) cattext.ReplaceAll("ee", "#mu#mu");
  TLatex *text3 = new TLatex(3.5, 24, cattext);
  text3->SetNDC();
  text3->SetTextAlign(13);
  text3->SetX(0.24);
  text3->SetTextFont(42);
  text3->SetTextSize(0.06);
  text3->SetY(0.73);
  text3->Draw();

  TLegend *leg = new TLegend(0.23,0.5,0.5,0.65, NULL,"brNDC");
  leg->SetFillColor(0);
  leg->SetLineColor(1);
  leg->SetBorderSize(0);
  leg->SetTextFont(42);
  leg->SetFillStyle(0);
  TLegendEntry* dleg = leg->AddEntry(data_eff, "Data", "lpe");
  //TLegendEntry* dmc = leg->AddEntry(mc_eff, "Simulation", "lpe");
  TLegendEntry* dmc = leg->AddEntry(mc_eff, "Simulation", "");

  TGraphErrors* gleg = new TGraphErrors(1);
  gleg->SetPoint(0, 0.049, 0.58);
  gleg->SetPointError(0, 0.015, 0.025);
  gleg->SetMarkerStyle(25);
  gleg->SetMarkerColor(kRed+1);
  gleg->SetLineColor(kRed+1);
  gleg->Draw("Z0P");

  dleg->SetTextFont(42);
  dmc->SetTextFont(42);
  dleg->SetTextSize(0.06);
  dmc->SetTextSize(0.06);

  leg->Draw();

  m_rp1->cd();

  TGraphAsymmErrors* ratio = (TGraphAsymmErrors*) file->Get("SF");

  ratio->SetMarkerStyle(20);
  ratio->SetMarkerColor(kBlack);
  ratio->SetLineColor(kBlack);
  ratio->Draw("AP");

  TLine* l = new TLine(0, 1, 0.5, 1);
  l->SetLineStyle(kDashed);
  l->Draw();

  TH1F* rpainter = ratio->GetHistogram();

  rpainter->GetXaxis()->SetRangeUser(0, 0.5);

  rpainter->GetXaxis()->SetTitle("#DeltaR(l,jet)");
  rpainter->GetYaxis()->SetTitle("Data/MC");
  rpainter->SetTitle("");

  rpainter->GetYaxis()->SetRangeUser(0.3, 1.7);
  rpainter->SetMarkerSize(0.7);

  rpainter->GetXaxis()->SetLabelSize(0.13);
  rpainter->GetXaxis()->SetLabelOffset(0.013);
  rpainter->GetXaxis()->SetTickLength(0.08);
  rpainter->GetXaxis()->SetTitleSize(0.16);
  rpainter->GetXaxis()->SetTitleOffset(1.0);
  
  // y-axis
  rpainter->GetYaxis()->CenterTitle();
  rpainter->GetYaxis()->SetTitleSize(0.16);
  rpainter->GetYaxis()->SetTitleOffset(0.5);
  rpainter->GetYaxis()->SetLabelSize(0.13);
  //rpainter->GetYaxis()->SetNdivisions(210);
  rpainter->GetYaxis()->SetNdivisions(505);
  rpainter->GetYaxis()->SetTickLength(0.03);
  rpainter->GetYaxis()->SetLabelOffset(0.011);
  
  TString epsname = fname;
  epsname.ReplaceAll(".root", ".eps");
  m_can->SaveAs(epsname);



}
