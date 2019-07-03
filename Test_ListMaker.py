import os
 
'''
    For the given path, get the List of all files in the directory tree 
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles        
 
 
def main():
    
    dirName = '/eos/cms/store/group/phys_exotica/bbMET/monoH_2016SkimmedTrees_withReg/Filelist_2016_MC/';
    
    # Get the list of all files in directory tree at given path
    #listOfFiles = getListOfFiles(dirName)
    
    # Print the files
    #for elem in listOfFiles:
     #   print(elem)
 
    print ("****************")
    
    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
	#print "dirpath", dirpath
	#print "dirnames", dirnames
        #print  "filenames",filenames
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]

    fileout='output.txt'
    Fout=open(fileout,'w')        
    # Print the files    
    for elem in listOfFiles:
        #print(elem)    
        Fout.write(elem+'\n')
        
        
        
        
if __name__ == '__main__':
    main()
