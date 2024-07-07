import os
from re import search, IGNORECASE
from sys import argv
from typing import List
from subprocess import run, PIPE


MAIN_CLASS_NAME = argv[1]
CURR_DIR: str = os.getcwd()
JAVA_FILE_PATTERN: str = '%s\\.java$'%MAIN_CLASS_NAME
INPUT_FILE_PATTERN: str = '%s.*\\.txt$'%MAIN_CLASS_NAME

CLASSES_FOLDER: str = os.path.join(CURR_DIR, 'classes')
if not os.path.isdir(CLASSES_FOLDER): os.mkdir(CLASSES_FOLDER)

###################################################################################################

class FileOrDir:
    def __init__(self, path, package):
        self.path = path
        self.package = package

    def __str__(self):
        return self.path

class Directory(FileOrDir):
    pass

class File(FileOrDir):
    def __init__(self, filePath='', package='', fileName=''):
        FileOrDir.__init__(self, filePath, package)
        self.fileName = fileName

    def getFullName(self):
        if not self.package:
            return self.fileName
        else:
            return self.package + '.' + self.fileName


###################################################################################################

def searchDir(directory: Directory) -> File | None:
    subDirPackageSuffix = ''
    if directory.package:
        subDirPackageSuffix = directory.package + '.'

    for fileOrDir in os.listdir(directory.path):
        location = os.path.join(directory.path, fileOrDir)

        if os.path.isfile(location):
            if search(JAVA_FILE_PATTERN, fileOrDir, IGNORECASE):
                return File(location, directory.package, fileOrDir)
        else:
            fileInSubdir = searchDir(Directory(
                    location, subDirPackageSuffix + fileOrDir))
            if fileInSubdir:
                return fileInSubdir

def getInputFiles(javaFile: File) -> List[File]:
    files: List[File] = []
    folder = os.path.dirname(javaFile.path)

    for fileOrDir in os.listdir(folder):
        location = os.path.join(folder, fileOrDir)
        if os.path.isfile(location) and search(INPUT_FILE_PATTERN, fileOrDir, IGNORECASE):
            files.append(File(location, javaFile.package, fileOrDir))

    return files

###################################################################################################

def runCmd(cmd: str):
    print(cmd)
    run(cmd)
    print('\n')

def runClass(javaClassFile: File, inputFiles: List[File]):
    className = javaClassFile.getFullName().replace('.java', '')
    command = 'java -cp ./classes %s'%className
    print('# Running the class: %s'%className)

    if len(inputFiles) == 0:
        runCmd(command)
        return

    for fileData in inputFiles:
        print('## Running with input file: %s'%fileData.fileName)
        inputFile = open(fileData.path, 'r')

        p = run(command, stdout=PIPE, input=inputFile.read(), encoding='ascii')
        print(p.stdout)



###################################################################################################

MAIN_FILE = searchDir(Directory(CURR_DIR, ''))

if MAIN_FILE:
    print('# Compiling the Java file: %s.'%MAIN_FILE.path)
    runCmd('javac -d classes %s'%MAIN_FILE.path)

    inputFiles = getInputFiles(MAIN_FILE)
    runClass(MAIN_FILE, inputFiles)
else:
    raise Exception('Failed to find Main File: %s.java'%MAIN_CLASS_NAME)
