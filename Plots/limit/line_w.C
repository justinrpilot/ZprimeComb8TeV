void line_w(){

  double x1 = 0.75;
  double x2 = 1.;
  double y1 = TMath::Log10(0.609);
  double y2 = TMath::Log10(0.469);

  double k1 = (y2-y1)/(x2-x1);
  double d1 = 0.5 * ((y1+y2) - k1*(x1+x2));

  cout << "k1 = " << k1 << " d1 = " << d1 << endl;

  TGraph* g = new TGraph(2);
  g->SetPoint(0, x1, TMath::Power(10,y1));
  g->SetPoint(1, x2, TMath::Power(10,y2));
  g->SetMarkerStyle(20);
  g->Draw("AP");
  
  TF1* f1 = new TF1("f1", "TMath::Power(10,[0]*x+[1])", 0, 2);
  f1->SetParameters(k1, d1);
  f1->Draw("same");

  double x3 = 0.75;
  double x4 = 1.;
  double y3 = TMath::Log10(0.81307); // expected limit from combo at 0.75
  double y4 = TMath::Log10(0.271426); // expected limit from combo at 1.0

  double k2 = (y4-y3)/(x4-x3);
  double d2 = 0.5 * ((y3+y4) - k2*(x3+x4));

  cout << "k2 = " << k2 << " d2 = " << d2 << endl;

  TF1* f2 = new TF1("f2", "TMath::Power(10,[0]*x+[1])", 0, 2);
  f2->SetParameters(k2, d2);
  f2->SetLineColor(kRed);
  f2->Draw("same");

  double x = (d2-d1)/(k1-k2);
  double exp = TMath::Power(10,k1*x+d1);

  double o1 = TMath::Log10(0.512); // observed 0.75
  double o2 = TMath::Log10(0.639); // observed 1
  double ok = (o1-o2)/(x3-x4);
  double od = 0.5 * ((o1+o2) - ok*(x3+x4));
  double obs = TMath::Power(10,ok*x + od);

  cout << "crossing = " << x << endl;
  
  double u168 = TMath::Log10(0.609+0.25);
  double u268 = TMath::Log10(0.469+0.20);
  double k = (u168-u268)/(x3-x4);
  double d = 0.5 * ((u268+u168) - k*(x3+x4));
  double u68 = TMath::Power(10,k*x + d);

  double l168 = TMath::Log10(0.609-0.16);
  double l268 = TMath::Log10(0.469-0.13);
  k = (l168-l268)/(x3-x4);
  d = 0.5 * ((l268+l168) - k*(x3+x4));
  double l68 = TMath::Power(10,k*x + d);

  double u195 = TMath::Log10(0.609+0.59);
  double u295 = TMath::Log10(0.469+0.41);
  double k = (u195-u295)/(x3-x4);
  double d = 0.5 * ((u295+u195) - k*(x3+x4));
  double u95 = TMath::Power(10,k*x + d);

  double l195 = TMath::Log10(0.609-0.28);
  double l295 = TMath::Log10(0.469-0.21);
  k = (l195-l295)/(x3-x4);
  d = 0.5 * ((l295+l195) - k*(x3+x4));
  double l95 = TMath::Power(10,k*x + d);

  cout << "final line: " << endl;
  cout << x << "  " << exp << "  " << u68 << "  " << l68 << "  " << u95 << "  " << l95 << "  " << obs << endl;
  


}
