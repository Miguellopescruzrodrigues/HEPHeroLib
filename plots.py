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
basedir = '/home/miguel/Mestrado/HEPHeroLib/datasets1'
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
            np.linspace(20,600,101), #LeadingLep_pt=================
            np.linspace(0,3,20), #LepLep_deltaR==================
            np.linspace(-3.,3.,31), #MET_phi
            np.linspace(0,700,101), # MET_pt
            np.linspace(5,35,31), #Pileup_nTrueInt
            np.linspace(20,300,101), #TrailingLep_pt==========
            #np.linspace(0.00005,0.00035,30), #evtWeight
            np.linspace(0,8,9), #nElectron===================
            np.linspace(0,6,7), #nFatJet===================
            np.linspace(0,10,11), #nIsoTrack================== aumentar os
            np.linspace(0,15,16), #nJet
            np.linspace(0,10,11), #nMuon=============
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
          r"$GenMET-p_T (GeV)$",
          r"$LeadingLep-p_T (GeV)$",
          r"$LepLep deltaR$",
          r"$METphi$",
          r"$MET p_T (GeV)$",
          r"$Pileup nTrueInt$",
          r"$TrailingLep-p_T (GeV)$",
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
          r"$GenMET_p_T (GeV)$",
          r"$nIsoTrack$",
          #r"$RecoLepID$",
          #r"$genWeight$", 
]

print("foi2")

def make_compare_plots(dataset_1,dataset_2,vars,bin_vars,labels):
    for var in vars:
        fig = plt.figure(figsize=(10,6))
        grid = [2, 1]
        gs1 = gs.GridSpec(grid[0], grid[1], height_ratios=[4, 1])
        N=1
        #==================================================
        ax1 = plt.subplot(ana.position(gs1,grid,N,1))              # Positioning at subplot 1 of the plot number 1
        #==================================================
        bins = bin_vars[vars.index(var)]
        ysgn1, errsgn1 = ana.step_plot( ax1, var, dataset_1, label=r'Official', color='blue', weight="evtWeight", bins=bins, error=True, normalize=True )
        ysgn2, errsgn2 = ana.step_plot( ax1, var, dataset_2, label=r'Private', color='red', weight="evtWeight", bins=bins, error=True, normalize=True )
        #ysgn1, errsgn1 = ana.step_plot( ax1, var, dataset_1, label=r'Danyer', color='blue', bins=bins, error=True, normalize=False )
        #ysgn2, errsgn2 = ana.step_plot( ax1, var, dataset_2, label=r'Private', color='red', bins=bins, error=True, normalize=False )
        ana.labels(ax1, ylabel="Events")  # Set up the label names
        ana.style(ax1, lumi=19.5, year=2016, legend_ncol=1, xticklabels=False) # Set up the plot style and information on top

        #==================================================
        ax2 = plt.subplot(ana.position(gs1,grid,N,2), sharex=ax1)  # Positioning at subplot 2 of the plot number 2
        #==================================================
        ana.ratio_plot( ax2, ysgn1, errsgn1, ysgn2, errsgn2, bins=bins, numerator="mc", color='blue')
        ana.labels(ax2, xlabel=labels[vars.index(var)], ylabel=r'Offi/Priv')  # Set up the label names
        #ana.style(ax2, ylim=[0.8, 1.5], yticks=[0.8, 1.5], xgrid=True, ygrid=True) 
        #ana.style(ax2, yticks=[0., 1, 2], xgrid=True, ygrid=True) 


        #=================================================================================================================
        # Make final setup, save and show plots
        #=================================================================================================================
        os.makedirs('./plots/',exist_ok=True)
        plt.subplots_adjust(left=0.090, bottom=0.115, right=0.96, top=0.95, wspace=0.35, hspace=0.0)
        plt.savefig('./plots/'+var+'.png')
        #plt.show()



make_compare_plots(datasets['Signal_1000_100'],datasets['Signal_Miguel'],vars,bin_vars,labels)
