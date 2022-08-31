import os
from pathlib import Path
path_atual = Path()

#Get current absolute path
def getCurrentPath():
    return path_atual.absolute()

#Show data about the current path
def showPathData(p):
    print('Current directory name: ' + str(p.name))
    print('Directory\'s root: ' + str(p.root))
    print('Directory\'s parent path: ' + str(p.parent))
    print('Directory\'s parts: ' + str(p.parts))

#Check if a file exists
def fileExists(f, p):
    return (p / f).exists()

#Get text from a file
def getText(f, p):
    if fileExists(f, p): return (p / f).read_text()

#Gets all files with certain extensions inside the directory if option = 1
#Gets all files from the subdirectories too if option != 1
#Returns just file name if opt2 == 1, returns absolute path for opt2 != 1
def getFiles(p, ext, opt, opt2):
    files = []
    if opt == 1: flist = list(p.glob('*.' + ext))
    else: flist = list(p.glob('**/*.' + ext))
    for x in flist:
        x = str(x)
        if(opt2 == 1):
            x = x.split('/')
            files.append(x[len(x) - 1])
        else: files.append(x)
    return files

def main():
    p = getCurrentPath()
    for x in getFiles(p, 'py', 2, 1):
        print('FILE FOUND: ' + x)
main()
