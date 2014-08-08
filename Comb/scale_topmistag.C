void scale_topmistag(TString inname = "ljets_all.root")
{
  // small macro to scale background and signal templates to 
  // the results from a maximum likelihood fit: only for the subjet b-tagging!

  // open existing file
  TFile* file = new TFile(inname, "READ");

  // create a new file
  TString outname = inname;
  outname.ReplaceAll(".root", "_topmistag_0.83.root");
  TFile* outfile = new TFile(outname, "RECREATE");

  // nuisance parameter for top-mistag on W+jets
  Double_t topmistag = 0.83;

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

    TString cat;
    TString sys;
    TString var;

    if (tokname->GetEntries()==4){
      cat = ((TObjString*) tokname->At(0))->GetString();
      sys = ((TObjString*) tokname->At(2))->GetString();
      var = ((TObjString*) tokname->At(3))->GetString();
    }

    // write histogram to new file
    outfile->cd();
    hist->Write("", TObject::kOverwrite);
    
    // never change DATA!
    if (process == "DATA") continue;

    // apply top-mistagging scale factor for l+jets analysis
    if (inname.Contains("ljets")){
      TString cat = ((TObjString*) tokname->At(0))->GetString();
      if (cat.Contains("_1top_")){
	if (process == "wb" || process == "wc" || process == "wlight" || process == "diboson" || process == "zlight" || process == "singletop"){
	  cout << "applying toptag-mistag scale factor of " << topmistag << " to " << hist->GetName() << endl;
	  hist->Scale(topmistag);
	}
      }
    }

    outfile->cd();
    hist->Write("", TObject::kOverwrite);

  }
 
  outfile->Write();
  outfile->Close();

}
