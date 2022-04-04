import shutil
import os
import fnmatch
import time


numberoffiles = 0

totaldir = 0

isos = 0

ending = "/Users/YOURUSERNAME/YOURFILEPATH/YOURFILEPATH"

starting = "/Users/YOURUSERNAME/YOURFILEPATH/YOURFILEPATH"

for base, dirs, files in os.walk(starting):
    print('Searching in : ', base)
    for directories in dirs:
        totaldir += 1
    for Files in files:
        numberoffiles +=1

for file in os.listdir(starting):
        if fnmatch.fnmatch(file, '*iso'):
            isos += 1


print('total number of files',numberoffiles)
print('total number of directories', totaldir)
print('total number of isos', isos)
print('total:', (totaldir + numberoffiles))

def movinfile():
    startTime = time.time()
    for file in os.listdir(starting):
        if fnmatch.fnmatch(file, '*iso'):
            shutil.move(starting+'/'+file, ending+'/'+file)
    executionTime = (time.time() - startTime)
    executionTime = str(executionTime) 
    print('moved ' + str(isos) + ' files in ' + executionTime[:5] + ' seconds')

def checkiftrue():
    required_word = 'yes' or "no"

    while True:
      yon = input("do you want to move the file to the designated path?\n(Yes or No): ").lower()
      if yon == required_word:
          print()
          print("Great moving it right now!\n")
          movinfile()
          break
      elif yon == "no":
        print()
        print("dang it would have been a fast transfer!!\n")
        break
      else:
          print("Invalid input-Try Again!\n")

checkiftrue()
        
