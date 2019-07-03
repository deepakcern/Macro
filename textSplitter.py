from itertools import izip_longest
from glob import glob
import os

cwd = os.getcwd()

def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def mergeFiles(path)

outPutDir='mergedROOT'
os.system('rm -rf '+outPutDir)
os.system('mkdir '+outPutDir)
path='/afs/cern.ch/work/d/dekumar/public/monoH/Filelists/NewSkimmed/test/Files'

txtFiles = glob(path+'/*txt')

n = 2

dirName='splittedFiles'
os.system('rm -rf '+dirName)
os.system('mkdir '+dirName) 

for ifile in txtFiles:
    outstr=ifile.split('/')[-1].replace('.txt','')
 #   print ('outstr',outstr)
    
    with open(ifile) as f:
        for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
            with open(dirName+'/'+outstr+'_{0}.txt'.format(i), 'w') as fout:
	        fout.writelines(g)
    

with open('copy_TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_0000.txt') as f:
    for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
        with open(dirName+'/'+'TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_{0}.txt'.format(i), 'w') as fout:
            fout.writelines(g)

newPath = cwd+'/'+dirName

#print ('newPath',newPath)
splitFiles = glob(newPath+'/*.txt')
#print ('splitFiles',splitFiles)

for sfile in splitFiles:
	strName=sfile.split('/')[-1].replace('.txt','.root')
#	print ('strName',strName)
	os.system('hadd '+outPutDir+'/'+str(strName)+' '+'@'+sfile)

