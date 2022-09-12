import os, hashlib
from pathlib import Path

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

def getBigger(pathlist):
    higher = 0
    for p in pathlist:
        path = Path(p).absolute()
        for x in getFiles(path, '', 2, 0):
            if len(x) > higher: higher = len(x)
    return higher

def getFilesNumber(pathlist):
    total = 0;
    for p in pathlist:
        path = Path(p).absolute()
        for x in getFilesNew(path): total = total + 1
    return total

def getFilesNew(p):
    flist = p.glob('**/*')
    files = [x for x in flist if x.is_file()]
    return files

def getLog(pathlist):
    f = open('data2.txt', 'w')
    f.close()
    #higher = getBiggerStr(getFiles(Path('/etc').absolute(), '', 2, 0))
    #higher = getBigger(pathlist)
    print('Calculating number of files..')
    n = 1
    filesNumber = getFilesNumber(pathlist)
    f = open('data2.txt', 'a')
    for p in pathlist:
        path_atual = Path(p).absolute()
        #for x in getFiles(path_atual, '', 2, 0):
        for x in getFilesNew(path_atual):
            f.write(str(x) + '\n')
            #for y in range(higher - len(x) + 1): f.write(' ')
            f.write(md5(x) + '\n\n')
            #os.system('clear')
            print(str(n) + '/' + str(filesNumber) + '  ' + str(path_atual))
            n = n + 1
    f.close()
    print('Data logging completed')

def main():
    p = Path().absolute()
    for x in getFilesNew(p):
        print(os.stat(x), x)
main()
