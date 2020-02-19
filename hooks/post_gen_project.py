import os
from distutils.dir_util import copy_tree

if __name__ == "__main__":
    currentFullPath = os.getcwd()
    currentDirName = os.path.basename(os.getcwd())
    sourceDirName = currentDirName.split('_')[-1]
    parrentDirFullPath = os.path.dirname(currentFullPath)
    copyFromDirectory = parrentDirFullPath + '/' + sourceDirName
    copyToDirectory = parrentDirFullPath + '/' + currentDirName
    copy_tree(copyFromDirectory,copyToDirectory)