# Script to concatenate files.

import os
import sys   
import argparse

def concatenateFiles(p_filesToAppend,p_inputFolderName,p_outputFolderName,p_prefix,p_newFileIndex):
    newFileName = "{0}/{1}_{2}".format(p_outputFolderName,p_prefix,p_newFileIndex)

    print "file: {0}".format(newFileName)
    print "files to append:"
    print p_filesToAppend
    with open(newFileName, 'w') as outfile:
            for fname in p_filesToAppend:
                with open('{0}/{1}'.format(p_inputFolderName,fname)) as infile:
                        for line in infile:
                            outfile.write(line)

def main(argv):
    # Arguments
    parser = argparse.ArgumentParser(description = 'Concatenate files.')
    parser.add_argument('numFiles', type=int,help='Number of files to concatenate.')
    parser.add_argument('inputFolder',type=str,help='Input folder name.')
    parser.add_argument('outputFolder',type=str,help='Output folder name.')
    parser.add_argument('prefix', type=str,help='Prefix for the new files')
    arguments = parser.parse_args()
    numberOfFiles = arguments.numFiles
    inputFolderName = arguments.inputFolder
    inputFolderName = inputFolderName.strip('/')
    outputFolderName = arguments.outputFolder
    outputFolderName = outputFolderName.strip('/')
    prefix = arguments.prefix
    appendedFiles = 0
    newFileIndex = 0
    filesToAppend = []

    print "grouping every {0} files".format(numberOfFiles)
    os.mkdir(outputFolderName)

    # Loop over the files in the folder. We are assuming no garbage is in there.
    for i in os.listdir(inputFolderName):
        # Accumulate the files to concatenate.
        filesToAppend.append(i)
        appendedFiles = appendedFiles+1
        if appendedFiles == numberOfFiles:
            # Once the desired number of files has been reached, they can be concatenated.
            concatenateFiles(filesToAppend,inputFolderName,outputFolderName,prefix,newFileIndex)
            appendedFiles = 0
            newFileIndex = newFileIndex + 1
            filesToAppend = []
    
    # leftover
    if len(filesToAppend)>0:
        concatenateFiles(filesToAppend,inputFolderName,outputFolderName,prefix,newFileIndex)

if __name__ == "__main__":
    main(sys.argv)
