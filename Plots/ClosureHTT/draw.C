void draw(TString fname = "qcdClosure_lowDY.root", int lohiDY = 0)
{

  gROOT->SetStyle("Plain");
  gROOT->LoadMacro("CMS_lumi.C");
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
       
  m_rp1_top->SetTopMargin(0.1); m_rp1_top->SetBottomMargin(0.0); m_rp1_top->SetLeftMargin(0.19); m_rp1_top->SetRightMargin(0.05);
  m_rp1->SetTopMargin(0.0); m_rp1->SetBottomMargin(0.35); m_rp1->SetLeftMargin(0.19); m_rp1->SetRightMargin(0.05);

  //TGraphAsymmErrors* data_eff = (TGraphAsymmErrors*) file->Get("qcd3H");
  //TGraphAsymmErrors* mc_eff = (TGraphAsymmErrors*) file->Get("qcd3predH");
  TH1F *data_eff = file->Get("totalH");
  TH1F *mc_eff = file->Get("totalPredH");


  m_rp1_top->Draw();
  m_rp1->Draw();

  m_rp1_top->cd();

  data_eff->SetMarkerStyle(20);
  data_eff->SetMarkerColor(kBlack);
  data_eff->SetLineColor(kBlack);
  data_eff->SetLineWidth(1);
  data_eff->SetMarkerSize(0.5);
  data_eff->Draw("E1");
  

  double x,y;

  mc_eff->SetMarkerStyle(25);
  mc_eff->SetMarkerColor(kRed+1);
  mc_eff->SetLineColor(kRed+1);
  mc_eff->SetLineWidth(1);
  mc_eff->SetMarkerSize(0.5);   

 
  TH1F* painter = data_eff->Clone();

  data_eff->GetXaxis()->SetTitle("Dijet Invariant Mass [GeV]");
  data_eff->GetYaxis()->SetTitle("Events");
  data_eff->SetTitle("");
  data_eff->GetXaxis()->SetRangeUser(250, 3000);
  data_eff->GetYaxis()->SetRangeUser(0.02, 100000);
  if (lohiDY == 1) data_eff->GetYaxis()->SetRangeUser(0.02, 1000000);


  data_eff->GetXaxis()->SetTickLength(0.05);
  
  // y-axis
  data_eff->GetYaxis()->SetTitleSize(0.09);
  data_eff->GetYaxis()->SetLabelSize(0.07);
  data_eff->GetYaxis()->SetLabelOffset(0.01);
  data_eff->GetYaxis()->SetTitleOffset(0.89);
  data_eff->GetYaxis()->SetTickLength(0.02);
  data_eff->SetLineWidth(1);

  //TLine* l = new TLine(painter->GetXaxis()->GetXmin(), 1., painter->GetXaxis()->GetXmax(), 1.);
  //l->SetLineColor(kBlue);
  //l->Draw();

  mc_eff->Draw("E1same");
  data_eff->Draw("E1same");

  m_rp1_top->SetLogy(1);

  TString infotext = TString::Format("19.7 fb^{-1} (8 TeV)");
  TLatex *text1 = new TLatex(3.5, 24, infotext);
  text1->SetNDC();
  text1->SetTextAlign(33);
  text1->SetX(0.95);
  text1->SetTextFont(42);
  text1->SetTextSize(0.06);
  text1->SetY(1.);
  //text1->Draw();

  /*TString cmstext = "CMS";
  TLatex *text2 = new TLatex(3.5, 24, cmstext);
  text2->SetNDC();
  text2->SetTextAlign(13);
  text2->SetX(0.24);
  text2->SetTextFont(62);
  text2->SetTextSize(0.08);
  text2->SetY(0.87);
  text2->Draw();*/
  CMS_lumi(m_rp1_top, 12, 10,"Simulation");

  TString cattext = "Z/#gamma^{*}(#rightarrow ee)+jets";
  if (fname.Contains("mu")) cattext.ReplaceAll("ee", "#mu#mu");
  TLatex *text3 = new TLatex(3.5, 24, cattext);
  text3->SetNDC();
  text3->SetTextAlign(13);
  text3->SetX(0.24);
  text3->SetTextFont(42);
  text3->SetTextSize(0.06);
  text3->SetY(0.73);
  //text3->Draw();

  TLegend *leg = new TLegend(0.4,0.675,0.73,0.845, NULL,"brNDC");
  leg->SetFillColor(0);
  leg->SetLineColor(1);
  leg->SetBorderSize(0);
  leg->SetTextFont(42);
  leg->SetFillStyle(0);
  if (lohiDY == 0) leg->AddEntry(totalH, "0+1+2 b-tags, H_{T}>800 GeV", "");
  else leg->AddEntry(totalH, "0+1+2 b-tags, H_{T}<800 GeV", "");
  TLegendEntry* dleg = leg->AddEntry(data_eff, "Selected QCD", "lpe");
  TLegendEntry* dmc = leg->AddEntry(mc_eff, "Predicted QCD", "lpe");

  dleg->SetTextFont(42);
  dmc->SetTextFont(42);
  dleg->SetTextSize(0.06);
  dmc->SetTextSize(0.06);
  leg->SetTextSize(0.06);

  leg->Draw();

  m_rp1->cd();

  //TGraphAsymmErrors* ratio = (TGraphAsymmErrors*) file->Get("SF");
  TH1F *ratio = data_eff->Clone();
  ratio->Divide(mc_eff);

  ratio->SetMarkerStyle(20);
  ratio->SetMarkerColor(kBlack);
  ratio->SetLineWidth(1);
  ratio->SetLineColor(kBlack);
  ratio->SetMarkerSize(1.0);
  ratio->Draw("E1");

  TLine* l = new TLine(250, 1, 3000, 1);
  l->SetLineStyle(kDashed);
  l->Draw("same");

  TH1F* rpainter = data_eff->Clone();
  rpainter->Divide(mc_eff);

  ratio->GetXaxis()->SetRangeUser(0, 0.5);

  ratio->GetXaxis()->SetTitle("Dijet Invariant Mass [GeV]");
  ratio->GetYaxis()->SetTitle("Sel./Pred.");
  ratio->SetTitle("");

  ratio->GetYaxis()->SetRangeUser(0.3, 2.3);
  ratio->GetXaxis()->SetRangeUser(250, 3000);
  ratio->SetMarkerSize(0.7);

  ratio->GetXaxis()->SetLabelSize(0.13);
  ratio->GetXaxis()->SetLabelOffset(0.013);
  ratio->GetXaxis()->SetTickLength(0.08);
  ratio->GetXaxis()->SetTitleSize(0.16);
  ratio->GetXaxis()->SetTitleOffset(1.0);
  
  // y-axis
  ratio->GetYaxis()->CenterTitle();
  ratio->GetYaxis()->SetTitleSize(0.16);
  ratio->GetYaxis()->SetTitleOffset(0.5);
  ratio->GetYaxis()->SetLabelSize(0.13);
  //ratio->GetYaxis()->SetNdivisions(210);
  ratio->GetYaxis()->SetNdivisions(505);
  ratio->GetYaxis()->SetTickLength(0.03);
  ratio->GetYaxis()->SetLabelOffset(0.011);
  
  TString epsname = fname;
  epsname.ReplaceAll(".root", ".eps");
  m_can->SaveAs(epsname);



}
