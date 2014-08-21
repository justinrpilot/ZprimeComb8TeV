void combine_dilepton(TString inname = "dilep_1pctZprime_50GeVbin_scaled.root")
{
  // small macro to combine the mumu, ee and emu channels into one
  // dilepton channel

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
    if (cat.Contains("ee") || cat.Contains("emu")){
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
  TString eecat = cat;
  eecat.ReplaceAll("mumu", "ee");
  TString emucat = cat;
  emucat.ReplaceAll("mumu", "emu");
  TString eename;
  TString emuname;
  TString mumuname;
  if (sys.Sizeof()>1){
    eename = eecat + "__" + process + "__" + sys + "__" + var;
    emuname = emucat + "__" + process + "__" + sys + "__" + var;
    mumuname =  cat + "__" + process + "__" + sys + "__" + var;
  } else {
    eename = eecat + "__" + process;
    emuname = emucat + "__" + process;
    mumuname =  cat + "__" + process;
  }

  TH1F* hee = (TH1F*) file->Get(eename);
  if (!hee){ 
    cout << "hist with name " << eename << " does not exist. Trying other systematics.. " << endl;
    if (sys.Contains("muoid")){
      eename.ReplaceAll("muoid", "eleid");
      hee = (TH1F*) file->Get(eename);
    } else if (sys.Contains("muontrig")){
      eename.ReplaceAll("muontrig", "electrontrig");
      hee = (TH1F*) file->Get(eename);
    } else {
      cout << "didn't work, taking nominal sample." << endl;
      eename = eecat + "__" + process;
    }
    TH1F* hee = (TH1F*) file->Get(eename);
    if (!hee){
      cout << "something went wrong, nominal sample " << eename << " does not exist." << endl;
      exit(3);
    }
  }

  TH1F* hemu = (TH1F*) file->Get(emuname);
  if (!hemu){ 
    cout << "hist with name " << emuname << " does not exist. Adding nominal sample. " << endl;
    emuname = emucat + "__" + process;
    TH1F* hemu = (TH1F*) file->Get(emuname);
    if (!hemu){
      cout << "something went wrong, nominal sample " << emuname << " does not exist." << endl;
      exit(3);
    }
  }

  hist->Add(hee);
  hist->Add(hemu);
  mumuname.ReplaceAll("mumu_", "dilepton_");
  hist->SetName(mumuname);

  hee->Delete();
  hemu->Delete();

  return;

}
