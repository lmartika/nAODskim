Files for running skims on nanoAOD using NanoAODtools (https://github.com/cms-nanoAOD/nanoAOD-tools) and crab, based on the provided examples.

Clone and compile NanoAODtools in CMSSW.

Running using DAS file paths in txt files:

(cd NanoAODTools)
bash submits.sh <path-to-txt>

or single input (edit parameters in crab_cfg)
crab submit crab_cfg.py

skimModule.py uses HLT trigger info for choosing events in output files.

If script names have been changed, double check also crabscript.sh.

NanoAODTools twiki: https://twiki.cern.ch/twiki/bin/view/CMS/NanoAODTools