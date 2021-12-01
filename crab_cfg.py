from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config

config = Configuration()

config.section_("General")
config.General.requestName = 'NanoAODskims_smaller'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.scriptExe = 'crabscript.sh'
config.JobType.inputFiles = ['skimModule.py', '../scripts/haddnano.py', "keep_and_drop.txt"]
config.JobType.sendPythonFolder = True

config.section_("Data")
#config.Data.inputDataset = '/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'
config.Data.inputDataset = '/JetHT/Run2018A-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD'

config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
#config.Data.totalUnits = 1

config.Data.outLFNDirBase = '/store/user/lamartik/NanoPost'
config.Data.publication = False
config.Data.outputDatasetTag = 'NanoJetHT'
config.section_("Site")
config.Site.storageSite = "T2_FI_HIP"
