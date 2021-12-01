#!/usr/bin/env python
import os
import PSet
import sys

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import *

# this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles, runsAndLumis

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

import ROOT
#ROOT.PyConfig.IgnoreCommandLineOptions = True


class skimmer(Module):
    def __init__(self):
        pass

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        trigDecision = False
## PFJet
        if hasattr(event._tree, 'HLT_PFJet40'):
            trigDecision = trigDecision or event.HLT_PFJet40
        if hasattr(event._tree, 'HLT_PFJet60'):
            trigDecision = trigDecision or event.HLT_PFJet60
        if hasattr(event._tree, 'HLT_PFJet80'):
            trigDecision = trigDecision or event.HLT_PFJet80
        if hasattr(event._tree, 'HLT_PFJet140'):
            trigDecision = trigDecision or event.HLT_PFJet140
        if hasattr(event._tree, 'HLT_PFJet200'):
            trigDecision = trigDecision or event.HLT_PFJet200
        if hasattr(event._tree, 'HLT_PFJet260'):
            trigDecision = trigDecision or event.HLT_PFJet260
        if hasattr(event._tree, 'HLT_PFJet320'):
            trigDecision = trigDecision or event.HLT_PFJet320
        if hasattr(event._tree, 'HLT_PFJet400'):
            trigDecision = trigDecision or event.HLT_PFJet400
        if hasattr(event._tree, 'HLT_PFJet450'):
            trigDecision = trigDecision or event.HLT_PFJet450
        if hasattr(event._tree, 'HLT_PFJet500'):
            trigDecision = trigDecision or event.HLT_PFJet500
        if hasattr(event._tree, 'HLT_PFJet550'):
            trigDecision = trigDecision or event.HLT_PFJet550
 
## PFJetfwd
        if hasattr(event._tree, 'HLT_PFJetFwd40'):
            trigDecision = trigDecision or event.HLT_PFJetFwd40
        if hasattr(event._tree, 'HLT_PFJetFwd60'):
            trigDecision = trigDecision or event.HLT_PFJetFwd60
        if hasattr(event._tree, 'HLT_PFJetFwd80'):
            trigDecision = trigDecision or event.HLT_PFJetFwd80
        if hasattr(event._tree, 'HLT_PFJetFwd140'):
            trigDecision = trigDecision or event.HLT_PFJetFwd140
        if hasattr(event._tree, 'HLT_PFJetFwd200'):
            trigDecision = trigDecision or event.HLT_PFJetFwd200
        if hasattr(event._tree, 'HLT_PFJetFwd260'):
            trigDecision = trigDecision or event.HLT_PFJetFwd260
        if hasattr(event._tree, 'HLT_PFJetFwd320'):
            trigDecision = trigDecision or event.HLT_PFJetFwd320
        if hasattr(event._tree, 'HLT_PFJetFwd400'):
            trigDecision = trigDecision or event.HLT_PFJetFwd400
        if hasattr(event._tree, 'HLT_PFJetFwd450'):
            trigDecision = trigDecision or event.HLT_PFJetFwd450
        if hasattr(event._tree, 'HLT_PFJetFwd500'):
            trigDecision = trigDecision or event.HLT_PFJetFwd500
        if hasattr(event._tree, 'HLT_PFJetFwd550'):
            trigDecision = trigDecision or event.HLT_PFJetFwd550

## AK8PFJet 
        if hasattr(event._tree, 'HLT_AK8PFJet40'):
            trigDecision = trigDecision or event.HLT_AK8PFJet40
        if hasattr(event._tree, 'HLT_AK8PFJet60'):
            trigDecision = trigDecision or event.HLT_AK8PFJet60
        if hasattr(event._tree, 'HLT_AK8PFJet80'):
            trigDecision = trigDecision or event.HLT_AK8PFJet80
        if hasattr(event._tree, 'HLT_AK8PFJet140'):
            trigDecision = trigDecision or event.HLT_AK8PFJet140
        if hasattr(event._tree, 'HLT_AK8PFJet200'):
            trigDecision = trigDecision or event.HLT_AK8PFJet200
        if hasattr(event._tree, 'HLT_AK8PFJet260'):
            trigDecision = trigDecision or event.HLT_AK8PFJet260
        if hasattr(event._tree, 'HLT_AK8PFJet320'):
            trigDecision = trigDecision or event.HLT_AK8PFJet320
        if hasattr(event._tree, 'HLT_AK8PFJet400'):
            trigDecision = trigDecision or event.HLT_AK8PFJet400
        if hasattr(event._tree, 'HLT_AK8PFJet450'):
            trigDecision = trigDecision or event.HLT_AK8PFJet450
        if hasattr(event._tree, 'HLT_AK8PFJet500'):
            trigDecision = trigDecision or event.HLT_AK8PFJet500
        if hasattr(event._tree, 'HLT_AK8PFJet550'):
            trigDecision = trigDecision or event.HLT_AK8PFJet550
 
## AK8AK8PFJetFwd
        if hasattr(event._tree, 'HLT_AK8PFJetFwd40'):
            trigDecision = trigDecision or event.HLT_AK8PFJetFwd40
        if hasattr(event._tree, 'HLT_AK8PFJetFwd60'):
            trigDecision = trigDecision or event.HLT_AK8PFJetFwd60
        if hasattr(event._tree, 'HLT_AK8PFJetFwd80'):
            trigDecision = trigDecision or event.HLT_AK8PFJetFwd80
        if hasattr(event._tree, 'HLT_AK8PFJetFwd140'):
            trigDecision = trigDecision or event.HLT_AK8PFJetFwd140
        if hasattr(event._tree, 'HLT_AK8PFJetFwd200'):
            trigDecision = trigDecision or event.HLT_AK8PFJetFwd200
        if hasattr(event._tree, 'HLT_AK8PFJetFwd260'):
            trigDecision = trigDecision or event.HLT_AK8PFJetFwd260
        if hasattr(event._tree, 'HLT_AK8PFJetFwd320'):
            trigDecision = trigDecision or event.HLT_AK8PFJetFwd320
        if hasattr(event._tree, 'HLT_AK8PFJetFwd400'):
            trigDecision = trigDecision or event.HLT_AK8PFJetFwd400
        if hasattr(event._tree, 'HLT_AK8PFJetFwd450'):
            trigDecision = trigDecision or event.HLT_AK8PFJetFwd450
        if hasattr(event._tree, 'HLT_AK8PFJetFwd500'):
            trigDecision = trigDecision or event.HLT_AK8PFJetFwd500

## Zerobias -> should this be applied only for zb data?

        if hasattr(event._tree, 'ZeroBias'):
            trigDecision = trigDecision or event.HLT_ZeroBias


        if not trigDecision:
            return False

        return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
skimmerModule = lambda: skimmer()


#files=["root://xrootd-cms.infn.it//store/mc/RunIISummer19UL18NanoAOD/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/10000/0376ED51-0D18-8D42-8091-448B0EA2898D.root"]

files=["root://xrootd-cms.infn.it///store/data/Run2018A/JetHT/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v2/100000/00AA9A90-57AA-D147-B4FA-54D6D8DA0D4A.root"]


p = PostProcessor(".",
                  inputFiles(),
#                  files,
                  "","keep_and_drop.txt",
                  modules=[skimmerModule()],
                  provenance=True,
                  fwkJobReport=True,
                  haddFileName="tree.root",
                  jsonInput=runsAndLumis())

p.run()


os.system("mv *_Skim.root tree.root")

print("DONE")
