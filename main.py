import os, hashlib
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

def md5(filename):
    md5_hash = hashlib.md5()
    with open(filename,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""): md5_hash.update(byte_block)
    return md5_hash.hexdigest()

#Gets all files with certain extensions inside the directory if option = 1
#Gets all files from the subdirectories too if option != 1
#Returns just file name if opt2 == 1, returns absolute path for opt2 != 1
def getFiles(p, ext, opt, opt2):
    files = []
    if opt == 1: flist = list(p.glob('*.' + ext))
    else:
        if len(ext) > 0: flist = list(p.glob('**/*.' + ext))
        else: flist = list(p.glob('**/*'))
    for x in flist:
        if x.is_file():
            x = str(x)
            if(opt2 == 1):
                x = x.split('/')
                files.append(x[len(x) - 1])
            else: files.append(x)
    return files

def getBiggerStr(strlist):
    higher = 0
    for x in strlist:
        if len(x) > higher: higher = len(x)
    return higher

def main():
    higher = getBiggerStr(getFiles(getCurrentPath(), '', 2, 0))
    f = open('data.txt', 'w')
    f.close()
    f = open('data.txt', 'a')
    for x in getFiles(getCurrentPath(), '', 2, 0):
        f.write(x)
        for y in range(higher - len(x) + 1): f.write(' ')
        f.write(md5(x) + '\n')
    f.close()
main()
