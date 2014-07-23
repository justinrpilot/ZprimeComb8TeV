void scale_subjb(TString inname = "CMSTT_zpn.root")
{
  // small macro to scale background and signal templates to 
  // the results from a maximum likelihood fit: only for the subjet b-tagging!

  // open existing file
  TFile* file = new TFile(inname, "READ");

  // create a new file
  TString outname = inname;
  outname.ReplaceAll(".root", "_subjb.root");
  TFile* outfile = new TFile(outname, "RECREATE");

  // nuisance parameter for subjet b-tagging
  Double_t nusubjbtag = 1.296;

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
    hist->Write("", TObject::kOverwrite);
    
    // never change DATA!
    if (process == "DATA") continue;

    // now do the subjet b-tagging, a bit more complicated
    // only for CMSTT analysis
    if (inname.Contains("CMSTT")){
      if (tokname->GetEntries()==4){
	TString cat = ((TObjString*) tokname->At(0))->GetString();
	TString sys = ((TObjString*) tokname->At(2))->GetString();
	TString var = ((TObjString*) tokname->At(3))->GetString();      
	if (sys == "subjbtag" && var == "plus"){
	  cout << "\ngot subjbtag for process " << process << " and category " << cat << endl;
	  // calculate change for a given process
	  TH1F* varh = GetVariation(cat, process, sys, var, nusubjbtag, file);
	  
	  // apply the change to all histograms of this process
	  ScaleProcess(cat, process, varh, file, outfile);

	}
      }
    }

  }
 
  outfile->Write();
  outfile->Close();

}

TH1F* GetVariation(TString cat, TString process, TString sys, TString var, Double_t nu, TFile* file)
{
  TString sname = cat + "__" + process + "__" + sys + "__" + var;
  TString name = cat + "__" + process;
  
  TH1F* hsys = (TH1F*) file->Get(sname);
  TH1F* hnominal = (TH1F*) file->Get(name);

  TH1F* hvar = (TH1F*) hnominal->Clone();

  for (Int_t i=1; i<hsys->GetNbinsX()+1; ++i){

    if ( !(hnominal->GetBinContent(i)>0) ) continue;

    // get difference and scale it with the nuisance parameter
    double diff = hsys->GetBinContent(i) - hnominal->GetBinContent(i);
    double rdiff = diff/hnominal->GetBinContent(i);
    double sf = TMath::Exp( nu * TMath::Log(1+rdiff) );
    //cout << "diff = " << diff << " sd = " << sf << endl;

    hvar->SetBinContent(i, sf);
  }
  
  return hvar;

}

void ScaleProcess(TString cat, TString process, TH1F* varh, TFile* file, TFile* outfile)
{
  
  // loop over all entries in the file, scale the right ones by varh
  TKey *key;
  TIter nextkey( file->GetListOfKeys() );
  while ( (key = (TKey*)nextkey())) {
    
    TH1* hist = (TH1*) file->Get(key->GetName());
    hist->SetName(key->GetName());

    TString hname = hist->GetName();
    hname.ReplaceAll("__", "#");
    TObjArray* tokname = hname.Tokenize("#");
    
    // never change DATA!
    if (process == "DATA") continue;

    TString ccat = ((TObjString*) tokname->At(0))->GetString();
    TString cproc = ((TObjString*) tokname->At(1))->GetString();
    
    if (ccat==cat && cproc==process){
      //cout << "scale this histogram: " << hname << endl;

      for (Int_t i=1; i<hist->GetNbinsX()+1; ++i){
	
	// scale the histogram content 
	double val = hist->GetBinContent(i) * varh->GetBinContent(i);
	
	hist->SetBinContent(i, val);
      }

      // write histogram to new file
      outfile->cd();
      hist->Write("", TObject::kOverwrite);
    }
  }

  varh->Delete();

}
