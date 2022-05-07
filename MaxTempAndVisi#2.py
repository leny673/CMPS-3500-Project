# I included this file for you guys to decided if this method would of been any better, but honestly it ended up doing more work
# and it ended up being the same number of lines, but just in case you guys wanted to work off this then thats fine too but I 
# don't know what I was thinking anymore lol

askForMaxTemp = True
while askForMaxTemp:
    maxTemp = input("Enter a Maximum Temperature (F): ")
    if not maxTemp:
        selectByMaxTemp = pd.notnull(accidentsByTemp_Vis['Temperature(F)'])
        askForMaxTemp = False
    else:
        try:
            maxTemp = float(maxTemp)
            if minTemp:
                while maxTemp <= minTemp:
                    copyMaxTemp = maxTemp
                    print("\nInvalid input. Maximum temperature must be greater than the minimum temperature.")
                    maxTemp = input("Enter a Maximum Temperature (F) or press enter for all possibilites: ")
                    if not maxTemp:
                        selectByMaxTemp = pd.notnull(accidentsByTemp_Vis['Temperature(F)'])
                        break
                    try:
                        maxTemp = float(maxTemp)
                    except ValueError:
                        print("\nInvalid input. Please enter a number choice.")
                        maxTemp = copyMaxTemp
            while not simpleValidation('Temperature(F)', maxTemp):
                maxTemp = input("\nInvalid value, enter again or press enter to search for all possibilities: ")
            if not maxTemp:
                selectByMaxTemp = pd.notnull(accidentsByTemp_Vis['Temperature(F)'])
                askForMaxTemp = False
            else:
                selectByMaxTemp = accidentsByTemp_Vis['Temperature(F)'] < maxTemp
                askForMaxTemp = False
        except ValueError:
            print("\nInvalid input. Please enter a number choice.")

askForMaxVis = True
while askForMaxVis:
    maxVis = input("Enter a Maximum Visibility (mi): ")
    if not maxVis:
        selectByMaxVis = pd.notnull(accidentsByTemp_Vis['Visibility(mi)'])
        askForMaxVis = False
    else:
        try:
            maxVis = float(maxVis)
            if minVis:
                while maxVis <= minVis:
                    copyMaxVis = maxVis
                    print("\nInvalid input. Maximum visibility must be greater than the minimum visibility.")
                    maxVis = input("Enter a Maximum Visibility (mi) or press enter for all possibilites: ")
                    if not maxVis:
                        selectByMaxVis = pd.notnull(accidentsByTemp_Vis['Visibility(mi)'])
                        break
                    try:
                        maxVis = float(maxVis)
                    except ValueError:
                        print("\nInvalid input. Please enter a number choice.")
                        maxVis = copyMaxVis
            while not simpleValidation('Visibility(mi)', maxVis):
                maxVis = input("\nInvalid value, enter again or press enter to search for all possibilities: ")
            if not maxVis:
                selectByMaxVis = pd.notnull(accidentsByTemp_Vis['Visibility(mi)'])
                askForMaxVis = False
            else:
                selectByMaxVis = accidentsByTemp_Vis['Visibility(mi)'] < maxVis
                askForMaxVis = False
        except ValueError:
            print("\nInvalid input. Please enter a number choice.")`