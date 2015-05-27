void combine_ljets(TString inname = "itheta_lepton_0709_scaled.root")
{
  // small macro to combine the e+jets and mu+jets channels 
  // into a l+jets channel


  // open existing file
  TFile* file = new TFile(inname, "READ");

  // create a new file
  TString outname = inname;
  outname.ReplaceAll(".root", "_combined.root");
  TFile* outfile = new TFile(outname, "RECREATE");


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
    TString sys;
    TString var;
    if (tokname->GetEntries()==4){
      sys = ((TObjString*) tokname->At(2))->GetString();
      var = ((TObjString*) tokname->At(3))->GetString();      
    }

    // write muon histogram to new file, add electron histos to it
    // i.e. skip electron hist
    if (cat.Contains("el_")){
      continue;
    }

    CombineChannels(hist, cat, process, sys, var, file);	

    // write histogram to new file
    outfile->cd();
    hist->Write("", TObject::kOverwrite);

  }


  outfile->Write();
  outfile->Close();


}

void CombineChannels(TH1* hist, TString cat, TString process, TString sys, TString var, TFile* file)
{

  // combine mu and el channels in one 

  // get the elec hist:
  TString ecat = cat;
  ecat.ReplaceAll("mu_", "el_");
  TString elname;
  TString muname;
  if (sys.Sizeof()>1){
    elname = ecat + "__" + process + "__" + sys + "__" + var;
    muname =  cat + "__" + process + "__" + sys + "__" + var;
  } else {
    elname = ecat + "__" + process;
    muname =  cat + "__" + process;
  }


  TH1F* hel = (TH1F*) file->Get(elname);
  if (!hel){ 
    cout << "hist with name " << elname << " does not exist. Trying other systematics... " << endl;
    if (sys.Contains("muoid")){
      elname.ReplaceAll("muoid", "eleid");
      hel = (TH1F*) file->Get(elname);
    } else {
      cout << "didn't work, using nominal sample" << endl;
      elname = ecat + "__" + process;
      hel = (TH1F*) file->Get(elname);
    }
    if (!hel){
      cout << "something went wrong, nominal sample " << elname << " does not exist." << endl;
      exit(3);
    }
  }

  //if (!(elname.Contains("Zprime") || elname.Contains("RSgluon"))){
  //  cout << "adding " << elname << endl
  //	 << " to    " << muname << endl << endl;
  //}
  hist->Add(hel);
  muname.ReplaceAll("mu_", "lepton_");
  hist->SetName(muname);

  hel->Delete();

  return;

}
