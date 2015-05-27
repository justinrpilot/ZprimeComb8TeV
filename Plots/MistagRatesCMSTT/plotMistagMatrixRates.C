{

  gROOT->SetStyle("Plain");
  gROOT->LoadMacro("CMS_lumi.C");
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
  Int_t c_BlueT0        = TColor::GetColor( "#112288" );
  Int_t c_BlueT1        = TColor::GetColor( "#2255cc" );
  Int_t c_BlueT2        = TColor::GetColor( "#4488dd" );
  Int_t c_BlueT3        = TColor::GetColor( "#99bbff" );
  Int_t c_BlueT4        = TColor::GetColor( "#99bbff" );
  Int_t c_BlueT5        = TColor::GetColor( "#aaddff" );

  Int_t c_RedT0         = TColor::GetColor( "#660000" );
  Int_t c_RedT1         = TColor::GetColor( "#B20000" );
  Int_t c_RedT2         = TColor::GetColor( "#FF0000" );
  Int_t c_RedT3         = TColor::GetColor( "#FF4D4D" );
  Int_t c_RedT4         = TColor::GetColor( "#FF9999" );
  Int_t c_RedT5         = TColor::GetColor( "#FFCCCC" );
  
  Int_t c_LightOrange   = TColor::GetColor( "#ffcc00" );
  Int_t c_VLightOrange  = TColor::GetColor( "#ffdd44" );
  Int_t c_FaintOrange   = TColor::GetColor( "#FFEBCD" );
  Int_t c_MediumOrange  = TColor::GetColor( "#FFCC00" );
  Int_t c_DarkOrange    = TColor::GetColor( "#ff6600" );
  Int_t c_VDarkOrange   = TColor::GetColor( "#aa4400" );
  


  
  Int_t c1, c2, c3, c4, c5, c6, c7, c8, c9;
  c1 = c_BlueT0;
  c2 = c_BlueT2;
  c3 = c_BlueT3;  
  c4 = c_BlueT5;

  c5 = c_RedT0;
  c6 = c_RedT1;
  c7 = c_DarkOrange;
  c8 = c_MediumOrange;


  TFile *mistag_file = new TFile("mistagRateHists.root");
  
  float tauBins[10] = { 0.0, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.2, 2.0 };
  float csvBins[5] = { -1.0, 0.0, 0.244, 0.679, 1.0  };

  
  for (int csvBin = 0; csvBin < 4; csvBin++){
    
    
    TH1F *nsj1H = (TH1F *) mistag_file->Get(Form("0_tagPt_%d_0", csvBin));
    TH1F *nsj2H = (TH1F *) mistag_file->Get(Form("0_tagPt_%d_1", csvBin));
    TH1F *nsj3H = (TH1F *) mistag_file->Get(Form("0_tagPt_%d_2", csvBin));
    TH1F *nsj4H = (TH1F *) mistag_file->Get(Form("0_tagPt_%d_3", csvBin));
    TH1F *nsj5H = (TH1F *) mistag_file->Get(Form("0_tagPt_%d_4", csvBin));
    TH1F *nsj6H = (TH1F *) mistag_file->Get(Form("0_tagPt_%d_5", csvBin));
    TH1F *nsj7H = (TH1F *) mistag_file->Get(Form("0_tagPt_%d_6", csvBin));
    TH1F *nsj8H = (TH1F *) mistag_file->Get(Form("0_tagPt_%d_7", csvBin));
    TH1F *nsj9H = (TH1F *) mistag_file->Get(Form("0_tagPt_%d_8", csvBin));
    TH1F *axisH = new TH1F("axis", "axis", 10000, 400, 1250);
    
    nsj1H->SetMarkerSize(0);	
    nsj2H->SetMarkerSize(0);	
    nsj3H->SetMarkerSize(0);	
    nsj4H->SetMarkerSize(0);	
    nsj5H->SetMarkerSize(0);	
    nsj6H->SetMarkerSize(0);	
    nsj7H->SetMarkerSize(0);	
    nsj8H->SetMarkerSize(0);	
    nsj9H->SetMarkerSize(0);	
    
    nsj1H->SetMarkerColor(c1);
    nsj2H->SetMarkerColor(c2);
    nsj3H->SetMarkerColor(c3);
    nsj4H->SetMarkerColor(c4);
    nsj5H->SetMarkerColor(c5);
    nsj6H->SetMarkerColor(c6);
    nsj7H->SetMarkerColor(c7);
    nsj8H->SetMarkerColor(c8);
    nsj9H->SetMarkerColor(c9);
    nsj1H->SetLineColor(c1);
    nsj2H->SetLineColor(c2);
    nsj3H->SetLineColor(c3);
    nsj4H->SetLineColor(c4);
    nsj5H->SetLineColor(c5);
    nsj6H->SetLineColor(c6);
    nsj7H->SetLineColor(c7);
    nsj8H->SetLineColor(c8);
    nsj9H->SetLineColor(c9);

    nsj1H->SetLineStyle(1);
    nsj2H->SetLineStyle(1);
    nsj3H->SetLineStyle(1);
    nsj4H->SetLineStyle(1);
    nsj5H->SetLineStyle(2);
    nsj6H->SetLineStyle(2);
    nsj7H->SetLineStyle(2);
    nsj8H->SetLineStyle(2);
    nsj9H->SetLineStyle(2);

    nsj1H->SetLineWidth(3);
    nsj2H->SetLineWidth(3);
    nsj3H->SetLineWidth(3);
    nsj4H->SetLineWidth(3);
    nsj5H->SetLineWidth(3);
    nsj6H->SetLineWidth(3);
    nsj7H->SetLineWidth(3);
    nsj8H->SetLineWidth(3);
    nsj9H->SetLineWidth(3);
    
    axisH->SetMinimum(0.001);
    axisH->SetMaximum(5.0);
	    
    axisH->GetXaxis()->SetTitle("CA8 jet p_{T} [GeV]");
    axisH->GetYaxis()->SetTitle("CA8 t tagging misid. prob.");
    axisH->GetXaxis()->SetTitleSize(0.06);
    axisH->GetYaxis()->SetTitleSize(0.06);
    axisH->GetXaxis()->SetLabelSize(0.06);
    axisH->GetYaxis()->SetLabelSize(0.06);

    TCanvas* can = new TCanvas("can", "can", width, height);

    can->SetTopMargin(0.1); 
    can->SetBottomMargin(0.12); 
    can->SetLeftMargin(0.15); 
    can->SetRightMargin(0.05);

    axisH->Draw("axis");
    axisH->GetXaxis()->SetMoreLogLabels(1);
    axisH->GetXaxis()->SetNoExponent(1);
    axisH->GetXaxis()->SetTitleOffset(1.15);
    axisH->GetYaxis()->SetTitleOffset(1.15);
    
    nsj1H->Draw("hist E ][ same");
    nsj2H->Draw("hist E ][ same");	
    nsj3H->Draw("hist E ][ same");	
    nsj4H->Draw("hist E ][ same");	
    nsj5H->Draw("hist E ][ same");	
    nsj6H->Draw("hist E ][ same");	
    nsj7H->Draw("hist E ][ same");	
    nsj8H->Draw("hist E ][ same");	
    //nsj9H->Draw("hist E same");	
    can->SetBottomMargin(0.15);

    TLatex *cmsLabel = new TLatex();
    cmsLabel->SetNDC();
    cmsLabel->SetTextFont(42);
    cmsLabel->SetTextSize(0.055);
    cmsLabel.DrawLatex(0.54,0.80, Form("%1.3f < #beta_{max} < %1.3f", csvBins[csvBin], csvBins[csvBin + 1]));
    
    TLegend *leg2 = new TLegend(0.1,0.2, 0.9, 0.8);
    leg2->SetNColumns(1);
    leg2->AddEntry(nsj1H, Form("%1.1f < #tau_{32} < %1.1f", tauBins[0], tauBins[1]), "l");
    leg2->AddEntry(nsj5H, Form("%1.1f < #tau_{32} < %1.1f", tauBins[4], tauBins[5]), "l");
    leg2->AddEntry(nsj2H, Form("%1.1f < #tau_{32} < %1.1f", tauBins[1], tauBins[2]), "l");
    leg2->AddEntry(nsj6H, Form("%1.1f < #tau_{32} < %1.1f", tauBins[5], tauBins[6]), "l");
    leg2->AddEntry(nsj3H, Form("%1.1f < #tau_{32} < %1.1f", tauBins[2], tauBins[3]), "l");
    leg2->AddEntry(nsj7H, Form("%1.1f < #tau_{32} < %1.1f", tauBins[6], tauBins[7]), "l");
    leg2->AddEntry(nsj4H, Form("%1.1f < #tau_{32} < %1.1f", tauBins[3], tauBins[4]), "l");
    leg2->AddEntry(nsj8H, Form("%1.1f < #tau_{32} < %1.1f", tauBins[7], tauBins[8]), "l");
    //leg2->AddEntry(nsj9H, Form("%1.1f < #tau_{32} < %1.1f", tauBins[8], tauBins[9]), "l");
    for (int i=0; i<leg2->GetListOfPrimitives()->GetEntries(); ++i){
      TLegendEntry* ent = leg2->GetListOfPrimitives()->At(i);
      ent->SetTextFont(42);
      ent->SetTextSize(0.06);
    }
    
    leg2->SetColumnSeparation(0.05);
    leg2->SetFillColor(0);
    leg2->SetLineColor(0);
    //leg2->Draw("same");
    
    CMS_lumi(can, 2, 10, "");
    
    can->SetLogy(1);
    can->SetLogx(1);
    can->SetTickx(1);
    can->SetTicky(1);
    
    can->RedrawAxis();
    
    can->SaveAs(Form("mistagRate_csvBin%d.pdf", csvBin));
    
    if ( csvBin == 3){
      TCanvas *can2 = new TCanvas("leg", "leg", width, height);
      can2->cd();
      leg2->SetNColumns(2);
      leg2->Draw();
      
      can2->SaveAs("legend_tau32bins.pdf");
    }
  }


}
