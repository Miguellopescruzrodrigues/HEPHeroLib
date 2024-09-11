import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import hepherolib.data as data
import hepherolib.analysis as ana

ana.start()

print("foi1")

# Caminho para a pasta 'datasets' que foi gerada pelo script grouper.py do HepHero
basedir = '/home/miguel/Mestrado/HEPHeroLib/datasets'
#Ano dos dados, no caso do NanoAOD testado, 17 (2017)
period = 'APV_16'
datasets = data.read_files(basedir, period)




vars = ['GenMET_phi',
        'GenMET_pt',
        'LeadingLep_pt',
        'LepLep_deltaR',
        'MET_phi',
        'MET_pt',
        'Pileup_nTrueInt',
        'TrailingLep_pt', 
        #'evtWeight', 
        'nElectron',
        'nFatJet', 
        'nIsoTrack', 
        'nJet', 
        'nMuon',
        'nSV', 
        'nTau',
        'LepLep_deltaR',
        'GenMET_phi',
        'GenMET_pt',
        'nIsoTrack',
        #'RecoLepID',
        #'genWeight'
        
        
]
bin_vars = [np.linspace(-3.,3.,31), #GenMET_phi
            np.linspace(0,300,101), #GenMET_pt
            np.linspace(20,600,101), #LeadingLep_pt ===============
            np.linspace(0,3,20), #LepLep_deltaR ===============
            np.linspace(-3.,3.,31), #MET_phi
            np.linspace(0,700,101), # MET_pt ======================
            np.linspace(5,35,31), #Pileup_nTrueInt
            np.linspace(20,300,101), #TrailingLep_pt ====================
            #np.linspace(0.00005,0.00035,30), #evtWeight
            np.linspace(0,8,9), #nElectron
            np.linspace(0,6,7), #nFatJet
            np.linspace(0,10,11), #nIsoTrack
            np.linspace(0,15,16), #nJet
            np.linspace(0,10,11), #nMuon
            np.linspace(0,10,11), #nSV
            np.linspace(0,6,7), #nTau 
            np.linspace(0,700,101), # LepLep_deltaR
            np.linspace(0,700,101), # GenMET_phi
            np.linspace(0,700,101), # GenMET_pt
            np.linspace(0,700,101), # nIsoTrack
            #np.linspace(0,20,20), # RecoLepID
            #np.linspace(0.,0.001,500), # genWeight
]


labels = [ r"$GenMETphi$",
          r"$GenMET-p_T$",
          r"$LeadingLep-p_T$",
          r"$LepLep deltaR$",
          r"$METphi$",
          r"$MET p_T$",
          r"$Pileup nTrueInt$",
          r"$TrailingLep-p_T$",
          #r"$evtWeight$",
          r"$NElectron$",
          r"$nFatJet$",
          r"$nIsoTrack$",
          r"$nJet$",
          r"$nMuon$",
          r"$nSV$",
          r"$nTau$",
          r"$LepLep deltaR$",
          r"$GenMET phi$",
          r"$GenMET_p_T$",
          r"$nIsoTrack$",
          #r"$RecoLepID$",
          #r"$genWeight$", 
]

print("foi2")

def make_compare_plots(dataset_1, dataset_2, dataset_3, dataset_4, vars, bin_vars, labels):
    for var in vars:
        fig = plt.figure(figsize=(10,6))
        ax1 = plt.subplot(1, 1, 1)  # Create a single subplot

        bins = bin_vars[vars.index(var)]
        ysgn1, errsgn1 = ana.step_plot(ax1, var, dataset_1, label=r'MH=1000 Ma=100', color='blue', weight="evtWeight", bins=bins, error=True, normalize=True)
        ysgn2, errsgn2 = ana.step_plot(ax1, var, dataset_2, label=r'MH=1000 Ma=100 Private', color='red', weight="evtWeight", bins=bins, error=True, normalize=True)
        ysgn3, errsgn3 = ana.step_plot(ax1, var, dataset_3, label=r'MH=400   Ma=100', color='purple', weight="evtWeight", bins=bins, error=True, normalize=True)
        ysgn4, errsgn4 = ana.step_plot(ax1, var, dataset_4, label=r'MH=400   Ma=100 Private', color='green', weight="evtWeight", bins=bins, error=True, normalize=True)

        ana.labels(ax1, xlabel=labels[vars.index(var)], ylabel="Events")
        ana.style(ax1, year=2016, legend_ncol=1)

        # Save and show plots
        os.makedirs('./plots_400_100/', exist_ok=True)
        plt.subplots_adjust(left=0.090, bottom=0.115, right=0.96, top=0.95)
        plt.savefig('./plots_400_100/' + var + '.png')
        plt.close(fig)

make_compare_plots(datasets['Signal_1000_100'], datasets['Signal_Miguel'], datasets['Signal_400_100'], datasets['Signal_Miguel_400_100'], vars, bin_vars, labels)
