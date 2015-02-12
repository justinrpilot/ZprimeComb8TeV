{

gROOT->LoadMacro("CMS_lumi.C");

wide3000->SetLineColor(kBlue);
narrow3000->SetLineColor(kRed);
rsgluon3000->SetLineColor(kBlack);

wide3000->SetLineStyle(kDashed);
narrow3000->SetLineStyle(kSolid);
rsgluon3000->SetLineStyle(kDotted);

wide3000->SetLineWidth(4);
narrow3000->SetLineWidth(4);
rsgluon3000->SetLineWidth(4);


wide3000->Rebin(5);
narrow3000->Rebin(5);
rsgluon3000->Rebin(5);

narrow3000->GetXaxis()->SetTitle("Generated M_{t#bar{t}} [GeV]");
narrow3000->GetYaxis()->SetTitle("Fraction of Events / Bin");
narrow3000->GetXaxis()->SetRangeUser(0., 4000.);
narrow3000->GetXaxis()->SetTitleSize(0.06);
narrow3000->GetXaxis()->SetLabelSize(0.06);
narrow3000->GetYaxis()->SetTitleSize(0.06);
narrow3000->GetYaxis()->SetLabelSize(0.06);
narrow3000->GetYaxis()->SetTitleFont(42);
narrow3000->GetXaxis()->SetTitleFont(42);
narrow3000->GetYaxis()->SetLabelFont(42);
narrow3000->GetXaxis()->SetLabelFont(42);

narrow3000->GetYaxis()->SetNdivisions(505);
narrow3000->GetXaxis()->SetNdivisions(505);

narrow3000->SetTitle("");
narrow3000->DrawNormalized();
wide3000->DrawNormalized("same");
rsgluon3000->DrawNormalized("same");


TLegend *leg = new TLegend(0.19, 0.42, 0.47, 0.70);
//TLegend *leg = new TLegend(0.6, 0.6, 0.88, 0.88);
leg->AddEntry(narrow3000, "Z' 1% width", "l");
leg->AddEntry(wide3000, "Z' 10% width", "l");
leg->AddEntry(rsgluon3000, "KK gluon", "l");
leg->AddEntry(rsgluon3000, "M = 3 TeV", "");

leg->SetLineColor(0);
leg->SetFillColor(0);

leg->Draw();

c1->SetLeftMargin(0.15);
c1->SetBottomMargin(0.15);
c1->Update();


CMS_lumi(c1, 12, 10, "Simulation");

c1->SaveAs("Mttbargen3000.pdf");

}


