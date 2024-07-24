# Depreciation calculator by (PIKI)

import locale
import os
from UserInput import UserInput as UI
from Asset import Asset

cost = 0.0
salvage = 0.0
life = 0


def main():
    global cost, salvage, life
    result = locale.setlocale(locale.LC_ALL, '')
    if result == 'C' or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL, 'en_US')
    print("Welcome to the Depreciation Calculator")

    choice = input("Asset by: <i>nput, <f>ile, <q>uit (i/f/q): ").lower()
    while len(choice) > 0 and choice[0] != "q":
        if choice[0] == "i":
            cost = UI.getValue("Cost: ", "f", 0)
            salvage = UI.getValue("Salvage: ", "f", 0)
            life = UI.getValue("Life: ", "i", 0)
        else:
            cost = -1
            flnm = getAssetFile()
            if flnm != None:
                print("File selected: " + flnm)
                print("Cost = " + str(cost) + " Salvage = " + str(salvage) + " Life = " + str(life))
        if cost >= 0:
            doDepreciation()
        else:
            print("No valid asset to process..")
        choice = input("Asset by: <i>nput, <f>ile, <q>uit (i/f/q): ").lower()
    print("Thanks for using the depreciation calculator.")

def getAssetFile():
    global cost,salvage,life
    print("Asset files available: ")

    assets = []
    cwd = os.getcwd() #This will be top-level project folder
    fnum = 0
    for entry in os.listdir(cwd):
        fullpath = os.path.join(cwd,entry)
        if os.path.isfile(fullpath) and entry.lower().endswith(".ast"):
            fnum += 1
            print(str(fnum) + ": " + entry)
            assets.append(fullpath)
    if fnum == 0:
        print("No Asset Files found.")
        cost = salvage = life = -1
        return None
    if fnum == 1:
        fullpath = assets[0]
    else:
        fnum = UI.getValue("File #(0=abort): ", "i", 0, len(assets))
        if fnum == 0:
            print("Operation aborted.")
            cost = salvage = life = -1
            return None
        fullpath = assets[fnum-1]
    try:
        f = open(fullpath, "r")
        cost = float(f.readline())
        salvage = float(f.readline())
        life = int(f.readline())
        f.close()
    except OSError as e:
        print("Asset File " + fullpath + " could not be read: " + str(e))
        cost = salvage = life = -1
        fullpath = None
    except ValueError as e:
        print("Read error on file: " + fullpath)
        cost = salvage = life = -1
        fullpath = None
    return fullpath

def doDepreciation():
    global cost, salvage, life
    asset = Asset(cost, salvage, life)
    #asset.buildAsset()
    if not asset.isValid():
        print(asset.getErrorMsg())
    else:
        print("Straight-Line annual depreciation is %s" % locale.currency(asset.getAnnDep(), grouping=True))
        print("Last Year Beg. Balance = %s " % locale.currency(asset.getBegBalSL(life), grouping=True))
        print("Last Year End Balance = %s " % locale.currency(asset.getEndBalSL(life), grouping=True) )

if __name__ == '__main__':
    main()

