import os

f=open('files.txt','r')
files = f.readlines()
os.system('hadd test.root '+' '+files)
