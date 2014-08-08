#!/usr/bin/env python
from ROOT import TGraph

def get_theory_XsecBR_graph(signal_):

    th = list()

    if signal_ == 'n':
        kNLO = 1.3
        #th.append([ 400., 35.77])
        th.append([ 500., 17.82])
        th.append([ 600., 10.08])
        th.append([ 700., 5.74])
        th.append([ 750., 4.31])
        th.append([ 800., 3.32])
        th.append([ 900., 1.98])
        th.append([1000., 1.24])
        th.append([1250., 0.441])
        th.append([1500., 0.160])
        th.append([1700., 7.99E-02])
        th.append([2000., 2.75E-02])
        th.append([2500., 5.30E-03])
        th.append([3000., 1.16E-03])

    elif signal_ == 'w':
        kNLO = 1.3
        #th.append([ 400., 271.98])  
        th.append([ 500., 145.06])  
        th.append([ 600., 77.71])   
        th.append([ 700., 43.59])   
        th.append([ 750., 33.29])   
        th.append([ 800., 25.67])   
        th.append([ 900., 15.63])   
        th.append([1000., 9.84])    
        th.append([1250., 3.37])    
        th.append([1500., 1.28])    
        th.append([1700., 0.616])   
        th.append([2000., 0.218])   
        th.append([2500., 4.21E-02])
        th.append([3000., 8.59E-03])

    elif signal_ == 'r':
        kNLO = 1.3
        th.append([1000., 6.299])
        th.append([1300., 1.81968])
        th.append([1600., 0.62327])
        th.append([1900., 0.24502])
        th.append([2200., 0.10841])
        th.append([2500., 0.053149])
        th.append([2800., 0.028766])
        th.append([3100., 0.016926])

    else:
        print '\n@@@ FATAL -- undefined signal model. stopping script.\n'
        raise SystemExit

    g = TGraph()
    for a in range(0,len(th)):
        g.SetPoint(a,th[a][0]/1000.,th[a][1]*kNLO)

    return g
