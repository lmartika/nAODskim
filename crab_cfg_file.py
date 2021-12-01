#from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config

import sys

# config = Configuration()
config = config()

if len(sys.argv)<1:
  sys.exit()
  print("Give input file")

args = sys.argv

filepath = args[1]
namepath = filepath[1:]
namepath = namepath.replace("/","-")
crabdir = namepath[:25]

config.section_("General")
config.General.workArea = 'runs'
config.General.requestName = crabdir
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.scriptExe = 'crabscript.sh'
config.JobType.inputFiles = ['skimModule.py', '../scripts/haddnano.py', "keep_and_drop.txt"]
config.JobType.sendPythonFolder = True

config.section_("Data")
#config.Data.inputDataset = '/JetHT/Run2018A-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD'
config.Data.inputDataset = filepath

config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
#config.Data.totalUnits = 1

config.Data.outLFNDirBase = '/store/user/lamartik/NanoPost'
config.Data.publication = False
config.Data.outputDatasetTag = namepath
config.section_("Site")
config.Site.storageSite = "T2_FI_HIP"



if __name__ == '__main__':
  from CRABAPI.RawCommand import crabCommand
  from CRABClient.ClientExceptions import ClientException
  from httplib import HTTPException

  def submit(config):
    try:
      crabCommand('submit', config = config)
    except HTTPException as hte:
      print "Failed submitting task: %s" % (hte.headers)
    except ClientException as cle:
      print "Failed submitting task: %s" % (cle)

  submit(config)
