{

gROOT->LoadMacro("CMS_lumi.C");

wide1500->SetLineColor(kBlue);
narrow1500->SetLineColor(kRed);
rsgluon1500->SetLineColor(kBlack);

wide1500->SetLineWidth(2);
narrow1500->SetLineWidth(2);
rsgluon1500->SetLineWidth(2);


wide1500->Rebin(5);
narrow1500->Rebin(5);
rsgluon1500->Rebin(5);

narrow1500->GetXaxis()->SetTitle("Generated M_{t#bar{t}} [GeV]");
narrow1500->GetYaxis()->SetTitle("Fraction of Events / Bin");
narrow1500->GetXaxis()->SetRangeUser(0., 4000.);
narrow1500->GetXaxis()->SetTitleSize(0.06);
narrow1500->GetXaxis()->SetLabelSize(0.06);
narrow1500->GetYaxis()->SetTitleSize(0.06);
narrow1500->GetYaxis()->SetLabelSize(0.06);
narrow1500->DrawNormalized();
wide1500->DrawNormalized("same");
rsgluon1500->DrawNormalized("same");


TLegend *leg = new TLegend(0.6, 0.6, 0.88, 0.88);
leg->AddEntry(narrow1500, "Z' 1% width", "l");
leg->AddEntry(wide1500, "Z' 10% width", "l");
leg->AddEntry(rsgluon1500, "KK gluon", "l");
leg->AddEntry(rsgluon1500, "M = 1.5 TeV", "");

leg->SetLineColor(0);
leg->SetFillColor(0);

leg->Draw();

c1->SetLeftMargin(0.15);
c1->SetBottomMargin(0.15);
c1->Update();


CMS_lumi(c1, 12, 10, "Simulation");


}


