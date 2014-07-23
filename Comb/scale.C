void scale(TString inname = "CMSTT_zpn.root")
{
  //inname = "dilep_zpn.root";
  //inname = "ljets_all.root";

  // small macro to scale background and signal templates to 
  // the results from a maximum likelihood fit

  // open existing file
  TFile* file = new TFile(inname, "READ");

  // create a new file
  TString outname = inname;
  outname.ReplaceAll(".root", "_scaled.root");
  TFile* outfile = new TFile(outname, "RECREATE");

  const Int_t Np = 7;
  TString pname[Np]   = { "ttbar",   "wlight",   "wc",   "st",   "wb", "diboson", "zlight"};
  Double_t pscale[Np] = {   0.986,      0.975,  1.022,  0.841,  0.954,     1.014,   1.914 };

  // nuisance parameter for top-tagging
  Double_t nutoptag = -0.465;

  // scale factor for toptagging
  //SF=exp(N*P)" where N is the nuisance parameter and P is the corresponding prior [example for 'toptag' N=-0.465 and P=ln(1.20) --> SF=0.919]
  // different strategy now, first calculate the factor (different for all-had and l+jets analyses)
  Double_t ftoptag = 1.0;
  Double_t pri = TMath::Log(1.0);
  if (inname.Contains("ljets")) pri = TMath::Log(1.2);
  if (inname.Contains("CMSTT")) pri = TMath::Log(1.4);
  Double_t ftoptag = TMath::Exp(nutoptag*pri);


  // loop over all entries in the file
  TKey *key;
  TIter nextkey( file->GetListOfKeys() );
  while ( (key = (TKey*)nextkey())) {
    
    TH1* hist = (TH1*) file->Get(key->GetName());
    hist->SetName(key->GetName());

    TString hname = hist->GetName();
    hname.ReplaceAll("__", "#");
    TObjArray* tokname = hname.Tokenize("#");
    TString process = ((TObjString*) tokname->At(1))->GetString();

    // write histogram to new file
    outfile->cd();
    hist->Write();
    
    // never change DATA!
    if (process == "DATA") continue;


    for (Int_t i=0; i<Np; ++i){
      if (process == pname[i]){
	//cout << "scale process " << process << " by " << pscale[i] << endl;
	hist->Scale(pscale[i]);
      }
    }    

    // apply top-tagging scale factor for CMSTT analysis
    if (inname.Contains("CMSTT")){
      if (process != "qcd"){
	//cout << "applying toptagging scale factor of " << ftoptag << " to " << process << endl;
	hist->Scale(ftoptag);
      }
    }

    // apply top-tagging scale factor for l+jets analysis
    if (inname.Contains("ljets")){
      TString cat = ((TObjString*) tokname->At(0))->GetString();
      if (cat.Contains("_1top_")){
	if (process != "wb" && process != "wc" && process != "wlight" && process != "diboson" && process != "zlight" && process != "singletop"){
	  //cout << "applying toptagging scale factor of " << ftoptag << " to " << process << " in category " << cat << endl;
	  hist->Scale(ftoptag);
	}
      }
    }

    // write histogram to new file
    outfile->cd();
    hist->Write("", TObject::kOverwrite);

  }
 

  outfile->Write();
  outfile->Close();



}
