{

  gROOT->SetStyle("Plain");
  gROOT->LoadMacro("../MistagRatesCMSTT/CMS_lumi.C");
  gStyle->SetOptStat(0);
  gStyle -> SetPadTickX(1);
  gStyle -> SetPadTickY(1);

  gStyle->SetEndErrorSize(0);

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

  // canvas size
  int width = 600;
  int height = 500;

  // define colours
  Int_t c_GreenT0        = TColor::GetColor( "#142907" );
  Int_t c_GreenT1        = TColor::GetColor( "#29520E" );
  Int_t c_GreenT2        = TColor::GetColor( "#478F18" );
  Int_t c_GreenT3        = TColor::GetColor( "#66CC22" );
  Int_t c_GreenT4        = TColor::GetColor( "#94DB64" );
  Int_t c_GreenT5        = TColor::GetColor( "#C2EBA7" );


  
  Int_t c1, c2, c3;
  c1 = c_GreenT0;
  c2 = c_GreenT2;
  c3 = c_GreenT4;  

  TFile *mistag_file = NULL;

  float csvBins[4] = { 0.0, 0.244, 0.679, 1.0  };

  
  for (int HTBin = 0; HTBin < 2; HTBin++){
    
    if (HTBin==0)
      mistag_file = new TFile("mistag_HT.root", "READ");
    else
      mistag_file = new TFile("mistag_QuadJet.root", "READ");

    TH1F *px4H = (TH1F *) mistag_file->Get("Mistag_px4");
    TH1F *px3H = (TH1F *) mistag_file->Get("Mistag_px3");
    TH1F *px2H = (TH1F *) mistag_file->Get("Mistag_px2");

    TH1F *axisH = NULL;
    if (HTBin==0)
      axisH = new TH1F("axis", "axis", 10000, 150, 800);
    else 
      axisH = new TH1F("axis", "axis", 10000, 150, 400);
    
    px4H->SetMarkerSize(0);	
    px3H->SetMarkerSize(0);	
    px2H->SetMarkerSize(0);	
    
    px4H->SetMarkerColor(c1);
    px3H->SetMarkerColor(c2);
    px2H->SetMarkerColor(c3);

    px4H->SetLineColor(c1);
    px3H->SetLineColor(c2);
    px2H->SetLineColor(c3);

    px4H->SetLineStyle(1);
    px3H->SetLineStyle(1);
    px2H->SetLineStyle(2);

    px4H->SetLineWidth(3);
    px3H->SetLineWidth(3);
    px2H->SetLineWidth(3);
    
    if (HTBin==0){
      axisH->SetMinimum(0.001);
      axisH->SetMaximum(0.5);
    } else {
      axisH->SetMinimum(0.01);
      axisH->SetMaximum(0.3);
    }
	    
    axisH->GetXaxis()->SetTitle("CA15 jet p_{T} [GeV]");
    axisH->GetYaxis()->SetTitle("CA15 t-tagging Misid. Prob.");
    axisH->GetXaxis()->SetTitleSize(0.06);
    axisH->GetYaxis()->SetTitleSize(0.06);
    axisH->GetXaxis()->SetLabelSize(0.06);
    axisH->GetYaxis()->SetLabelSize(0.06);

    TCanvas* can = new TCanvas("can", "can", width, height);

    can->SetTopMargin(0.1); 
    can->SetBottomMargin(0.15); 
    can->SetLeftMargin(0.15); 
    can->SetRightMargin(0.05);

    axisH->Draw("axis");
    axisH->GetXaxis()->SetMoreLogLabels(1);
    axisH->GetXaxis()->SetNoExponent(1);
    axisH->GetXaxis()->SetTitleOffset(1.15);
    axisH->GetYaxis()->SetTitleOffset(1.15);
    
    px4H->Draw("hist E ][ same");
    px3H->Draw("hist E ][ same");	
    px2H->Draw("hist E ][ same");	

    TLatex *cmsLabel = new TLatex();
    cmsLabel->SetNDC();
    cmsLabel->SetTextFont(42);
    cmsLabel->SetTextSize(0.055);
    if (HTBin==0)
      cmsLabel.DrawLatex(0.66,0.80, "H_{T} > 800 GeV");
    else
      cmsLabel.DrawLatex(0.66,0.80, "H_{T} < 800 GeV");
    
    TLegend *leg2 = new TLegend(0.2, 0.18, 0.6, 0.43);
    leg2->AddEntry(px4H, Form("%1.3f < #beta_{max} < %1.3f", csvBins[2], csvBins[3]), "l");
    leg2->AddEntry(px3H, Form("%1.3f < #beta_{max} < %1.3f", csvBins[1], csvBins[2]), "l");
    leg2->AddEntry(px2H, Form("%1.3f < #beta_{max} < %1.3f", csvBins[0], csvBins[1]), "l");
    for (int i=0; i<leg2->GetListOfPrimitives()->GetEntries(); ++i){
      TLegendEntry* ent = leg2->GetListOfPrimitives()->At(i);
      ent->SetTextFont(42);
      ent->SetTextSize(0.055);
    }
    leg2->SetFillColor(0);
    leg2->SetLineColor(0);
    leg2->Draw("same");
    
    if (HTBin==0)
      CMS_lumi(can, 2, 10, "");
    else
      CMS_lumi(can, 23, 10, "");

    can->SetLogy(1);
    can->SetLogx(1);
    can->SetTickx(1);
    can->SetTicky(1);
    
    can->RedrawAxis();
    
    if (HTBin==0)
      can->SaveAs("mistagRate_HT.pdf");
    else 
      can->SaveAs("mistagRate_Quad.pdf");
    
  }


}
