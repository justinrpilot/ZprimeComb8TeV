void get_eff(TString inname = "ljets_all_0911_norebin_scaled.root")
{
  //inname = "HEPTT_rsg_scaled.root";
  //inname = "CMSTT_rsg_scaled.root";
  //inname = "templates_ZpN.root";
  //inname = "dilep_10pctZprime_50GeVbin_scaled.root";
  //inname = "dilep_GKK_50GeVbin_scaled.root";

  inname.Prepend("mttbar_input_1119/");

  // small macro to calculate the signal efficiency

  // open existing file
  TFile* file = new TFile(inname, "READ");

  // numbers for l+jets analysis  
  const Int_t Np = 9;
  TString sname[Np]   = { "Zprime1000",   "Zprime2000",   "Zprime3000",   "ZprimeWide1000",   "ZprimeWide2000", "ZprimeWide3000", "RSgluon1000", "RSgluon2000", "RSgluon3000"};

  // numbers for l+jets analysis
  Double_t  sev[Np] = {         206846,        189522 ,          96371,             207430,             485137,           200810,       100000 ,       100000 ,       100000 };

  // numbers for dilepton analysis
  //Double_t  sev[Np] = {         103000,        95000,          96000,             104000,             97000,           101000,       100000 ,       100000 ,       100000 };

  // for HTT analysis
  //TString sname[Np]   = { "Zprime750",   "Zprime1000",   "Zprime2000",   "ZprimeWide750",   "ZprimeWide1000", "ZprimeWide2000", "RSgluon700", "RSgluon1000", "RSgluon2000"};
  //Double_t  sev[Np] = {         217629,        206846,        189522 ,             216010,            207430,           485137,        92960,        100000,       100000 };

  // for CMSTT analysis
  //Double_t  sev[Np] = {         101697,        90778,           91209,               102618,              93869,           97234,       100000 ,       100000 ,       100000 };

  // loop over all entries in the file
  TKey *key;
  TIter nextkey( file->GetListOfKeys() );
  while ( (key = (TKey*)nextkey())) {
    
    TH1* hist = (TH1*) file->Get(key->GetName());
    hist->SetName(key->GetName());

    TString hname = hist->GetName();
    hname.ReplaceAll("__", "#");
    TObjArray* tokname = hname.Tokenize("#");
    TString cat = ((TObjString*) tokname->At(0))->GetString();
    TString process = ((TObjString*) tokname->At(1))->GetString();

    if (tokname->GetEntries()==4){
      continue;
    }


    for (Int_t i=0; i<Np; ++i){
      if (process.Contains(sname[i])){
	//if (cat.BeginsWith("htt")) continue;
	if (cat.Contains("mjhtt")) continue;
	cout << "channel = " << cat << " process = " << process;

	// selected number of events (weighted with efficiencies)
	Double_t sel = hist->Integral();

	// expected number of events (without efficiency loss)
	Double_t Lgen = sev[i]/1000.; // 1000 fb = 1 pb = sigma_gen
	
	Double_t Ngen = 19.7 / Lgen * sev[i];
	//cout << "Lgen = " << Lgen << " Ngen = " << Ngen << endl;

	Double_t err = 0.; 
	Double_t Nmeas = hist->IntegralAndError(1, hist->GetNbinsX()+1, err);

	//cout << "eff (with weights) = " << Nmeas/Ngen*100. << " eff without weights = " << hist->GetEntries()/sev[i]*100. << endl;

	printf(" eff = %2.1f\n", Nmeas/Ngen*100.);
		//<< setprecision(2) << Nmeas / Ngen * 100.<< " +- " << err/Ngen * 100. << endl;
      }
    }    

  }
 

}

