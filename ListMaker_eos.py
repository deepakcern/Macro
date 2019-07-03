import os,sys

errmsg="Usage:\n$ python ListMaker.py crab T2path outfileprefix\nor\n$ python ListMaker.py st T2path outfileprefix"

if len(sys.argv)==4:
    if sys.argv[1]=="crab":
        isCrab=True
    elif sys.argv[1]=="st":
        isCrab=False
    else:
        print errmsg
        sys.exit()
    T2path=sys.argv[2]
    filepref=sys.argv[3]
else:
    print errmsg
    sys.exit()

inpfilename='T2List_'+filepref+'.txt'
os.system('ls  -R '+T2path+' &> ' +inpfilename)
#os.system('ls -rR '+T2path+' | cat &> ' +inpfilename)
    
f=open(inpfilename,"r")

os.system("mkdir -p Filelist"+"_"+filepref)
pref="root://eoscms.cern.ch/"
filecount=1
lineminus1=""
lineminus2=""
fileopen=False
failedfile=False
log=open("log_"+filepref+".txt","w")

for line in f:
    if not line=="\n" and not 'failed' in line:
        fname=line.split()[-1]
    else:
        fname=""

    if fname.endswith(".root") and not fileopen:# and ('NCUGlobalTuples' in fname):
        folder=pref+lineminus2[:-2]+"/"
        if lineminus2.split("/")[-1].strip()=="failed:" or lineminus2.split("/")[-1].strip()=="log:": failedfile=True
        if not failedfile:
            #print "checking at first step", lineminus2
            if isCrab:
		#if 'log' in lineminus2: continue
               # print "checking line", lineminus2
                #print ("This will write in log", lineminus2.split("/")[-3]+"_"+filepref+str(filecount)+" "+filepref+str(filecount)+".txt\n")
                #log.write(lineminus2.split("/")[-3]+"_"+filepref+str(filecount)+" "+filepref+str(filecount)+".txt\n")          # For making a list of CRAB job outputs
                log.write(lineminus2.split("/")[-3]+"_"+lineminus2.split("/")[-1][:-2]+" "+filepref+str(filecount)+".txt\n")
            else:
		#print "checking line2", lineminus2
                log.write(lineminus2.split("/")[-1][:-2]+" "+filepref+str(filecount)+".txt\n")      # For making a list of SkimmedTrees
            #print("Filelist"+"_"+filepref+"/"+filepref+str(filecount)+".txt")
            out=open("Filelist"+"_"+filepref+"/"+filepref+str(filecount)+".txt","w")        
            out.write(folder+fname+"\n")
            filecount+=1
        fileopen=True
    elif fname.endswith(".root"):# and ('NCUGlobalTuples' in fname) :
        if not failedfile: out.write(folder+fname+"\n")
    elif fileopen:
        if not failedfile: out.close()
        fileopen=False
        failedfile=False
    
    if lineminus1=="\n":
        lineminus2=line
    else:
        lineminus2 = lineminus1
    lineminus1=line
    
log.close()
f.close()

print "Created Filelist_%s directory and log_%s.txt." %(filepref,filepref)
