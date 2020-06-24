import os

allFiles = os.listdir(".")


def filterPy(filesList):
    pyFiles = {}
    index = 0
    for file in filesList:
        if file.endswith(".py") and file != "main.py":
            pyFiles.update({index: file})
            index += 1
        else:
            pass
    return pyFiles


def displayFiles(filesDict):

    for key in filesDict:
        fileName = " ".join(filesDict[key].split("-"))
        print(f"\n\n Press: {key} to use => {fileName}\n\n")


def executeFile():
    pyFilesDict = filterPy(allFiles)
    displayFiles(pyFilesDict)
    keyPressed = int(input("Enter your selection => ").strip())
    os.system(f"python3 {pyFilesDict[keyPressed]}")


executeFile()
