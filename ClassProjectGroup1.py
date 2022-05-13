# CLASS Project
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# COURSE: CMPS 3500
# DATE: 05/12/22
# Student 1: Elena Castaneda
# Student 2: Elijah Morris
# Student 3: Marcus Schmidt
# Student 4: Michael Wisehart
# DESCRIPTION: Implementation Basic Data Analysys Routines

import time
import pandas as pd

def printMenu():
    print()
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Load Data")
    print("2. Process Data.")
    print("3. Print Answers.")
    print("4. Search Accidents (Use City, State, and Zip Code).")
    print("5. Search Accidents (Year, Month, and Day).")
    print("6. Search Accidents (Temperature Range and Visibility Range).")
    print("7. Exit")
    print(66 * "-")

# Print the message in a standardized message format that includes the current time
def printMessage(*args):
    print("[ ", round(time.process_time(), 4)," ] ", *args)

# Validatation: Validate if input is in the dataframe
def simpleValidation(column, value):
    # Confirm that the column is one of the ones that this method can safely operate on
    if column == 'State' or column == 'Temperature(F)' or column == 'Visibility(mi)':
        # Then return true if the value is None or exists in the data frame
        if not value or value in df[column].values:
            return True
        else:
            return False

def validateCity(city, state):
    if not city:
        return True
    if city not in df['City'].values:
        return False
    else:
        validateCityInSt = df[['State','City']]
        selectByState = validateCityInSt['State'] == state
        possibleCities = validateCityInSt[selectByState]
        if city not in possibleCities['City'].values:
            return False
        else:
            return True

def validateZip(zip, city, state):
    if not zip:
        return True
    if zip not in df['Zipcode'].values:
        return False
    else:
        if city:
            validateZipInCity = df[['Zipcode','City']]
            selectByCity = validateZipInCity['City'] == city
            possibleZips = validateZipInCity[selectByCity]
            if zip not in possibleZips['Zipcode'].values:
                return False
            else:
                return True
        else:
            if state:
                validateZipInSt = df[['Zipcode','State']]
                selectByState = validateZipInSt['State'] == state
                possibleZips = validateZipInSt[selectByState]
                if zip not in possibleZips['Zipcode'].values:
                    return False
                else:
                    return True
            else:
                return True

def validateYear(year):
    if not year:
        return True

    # Return whether or not this year exists in the data set
    years = pd.to_datetime(df['Start_Time']).dt.strftime('%Y')
    if year not in years.values:
        return False
    else:
        return True

def validateMonth(month):
    if not month:
        return True

    # Return whether or not this year exists in the data set
    months = pd.to_datetime(df['Start_Time']).dt.strftime('%m')
    if month not in months.values:
        return False
    else:
        return True

def validateDay(day):
    if not day:
        return True

    # Return whether or not this year exists in the data set
    days = pd.to_datetime(df['Start_Time']).dt.strftime('%d')
    if day not in days.values:
        return False
    else:
        return True

def anyOtherValidation(input):
    if not input:
        return True
    if input not in df.values:
        return False
    else:
        return True

# Convert a month's number (1-12) into its name
def getMonth(month):
    if month >= 1 and month <= 12:
        months = ["January","February","March","April", "May", "June", "July", "August", "September", "October", "November","December"]
        return months[month-1]
    else:
        return "ERROR"

# Find the state with the most accidents in a given year (and with optional severity)
def maxAccidentState(year, severity = None):
    if df is None:
        return "ERROR - UNINITIALIZED DATA FRAME"
    
    # Copy only the columns that are relevant to this method
    data = df[['State','Start_Time','Severity']].copy()
    # Reformat the Start_Time column to be searchable by year
    data['Start_Time'] = pd.to_datetime(data['Start_Time']).dt.strftime('%Y')

    # Search the data for rows that match the provided conditions
    rows = None
    if severity is not None:
        rows = data.loc[(data['Start_Time'] == year) & (data['Severity'] == severity)]
    else:
        rows = data.loc[data['Start_Time'] == year]

    # Count the number of times each state occurs in the searched rows and return the most frequent result
    rankedStates = rows['State'].value_counts()
    if rankedStates.size > 0:
        return rankedStates.index[0]
    else:
        return "NULL"

# Find the most common severity in the provided state
def sevByState(state):
    if df is None:
        return "ERROR - UNINITIALIZED DATA FRAME"
    
    # Copy columns State and Severity into a new dataframe to focus on specific columns based on the question
    data = df[['State','Severity']].copy()
    
    # Select only rows with the given state
    rows = data.loc[data['State'] == state]
    
    # Count how often each severity appears for this state
    rankedSeverity = rows['Severity'].value_counts()
    if rankedSeverity.size > 0:
        return rankedSeverity.index[0]
    else:
        return "NULL"

# Find the top 'num' cities with the most accidents in the provided year and state
def maxAccidentCities(year, state, num):
    if df is None:
        return "ERROR - UNINITIALIZED DATA FRAME"
    elif num < 1:
        return "ERROR - INVALID NUM"

    # Copy original dataframe to modify Start_Time by year
    data = df[['State', 'City', 'Start_Time']].copy()
    data['Start_Time'] = pd.to_datetime(data['Start_Time']).dt.strftime('%Y')
    
    # Select rows with the provided conditions
    rows = data.loc[(data['State'] == state) & (data['Start_Time'] == year)]
    
    # Count how many accidents occur in each city and return the requested number of top results
    rankedCities = rows['City'].value_counts()
    if rankedCities.size >= num:
        return rankedCities.index[0:num]
    else:
        return "ERROR - NOT ENOUGH CITIES"

# Find average humidity and temperature of accidents with a certain year and severity
def averageConditions(year, severity):
    if df is None:
        return "ERROR - UNINITIALIZED DATA FRAME"

    # Copy original dataframe to modify Start_Time by year
    data = df[['Start_Time','Severity','Humidity(%)','Temperature(F)']].copy()
    data['Start_Time'] = pd.to_datetime(data['Start_Time']).dt.strftime('%Y')
    
    # Select rows with the provided conditions
    rows = data.loc[(data['Start_Time'] == year) & (data['Severity'] == severity)]
    
    # Get the average (mean) of the humidity and temperature from the selected rows
    averageHumidity = round(rows['Humidity(%)'].mean(), 2)
    averageTemperature = round(rows['Temperature(F)'].mean(), 2)
    return averageHumidity, averageTemperature

# To answer questions in the structure: "What was the maximum visibility of all accidents of severity 2 
# that occurred in the state of New Hampshire?", with given severity and state.
def maxVisBySev_St(sev, st):
    # Copy columns Visibility(mi), Severity, and State into a new dataframe to focus on specific columns based on the question
    dfCopy = df.copy()
    questionDF = dfCopy[['Visibility(mi)', 'Severity', 'State']]
    # Select only rows by given state and severity
    selectByState = questionDF['State'] == st
    selectBySeverity = questionDF['Severity'] == sev
    questionDF = questionDF[(selectByState) & (selectBySeverity)]
    # Get the max visibility from the dataframe created to fit the question conditions
    maxVisibility = questionDF['Visibility(mi)'].max()
    return maxVisibility

# To answer questions in the structure: "How many accidents of each severity were recorded in Bakersfield?", with given city.
def totalBySevInCity(city):
    # Copy columns City and Severity into a new dataframe to focus on specific columns based on the question
    dfCopy = df.copy()
    questionDF = dfCopy[['City','Severity']]
    # Select only rows by given city
    selectByCity = questionDF['City'] == city
    # Count the number of accidents by severity
    totalBySeverityInST = questionDF.loc[(selectByCity), 'Severity'].value_counts()
    return totalBySeverityInST

# To answer questions in the structure: "What was the longest accident (in hours) recorded in Florida 
# in the Spring (March, April, and May) of 2020?" with given month range, state, and year.
def longestAcc(startMonth, endMonth, st, yr):
    # Copy original dataframe to modify Start_Time and End_Time by year
    dfCopy = df.copy()
    dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time'])
    dfCopy['End_Time'] = pd.to_datetime(dfCopy['End_Time'])
    # Copy columns Start_Time, End_Time, and State into a new dataframe to focus on specific columns based on the question
    questionDF = dfCopy[['Start_Time','End_Time','State']]
    # Select rows that have a Start_Time between a given month range
    betweenMonths = questionDF['Start_Time'].dt.month.between(startMonth,endMonth)
    betweenMonths = questionDF[betweenMonths]
    # Select only rows by given state and year
    selectByState = betweenMonths['State'] == st
    selectByYear = pd.to_datetime(betweenMonths['Start_Time']).dt.year  == yr
    questionDF = betweenMonths[(selectByState) & (selectByYear)]
    # Get the End_Time and Start_Time to calculate the total time of the accidents and get the longest accident
    totalTimeOfAccident = questionDF['End_Time'] - questionDF['Start_Time']
    longestAccident = totalTimeOfAccident.max()
    # Convert the date to hours
    longestAccidentInHrs = (longestAccident.days*86400) + (longestAccident.seconds)
    return longestAccidentInHrs

# Menu option #1 (returns the data frame read from CSV file and a boolean value of whether it read properly)
def readFile():
    print("\nLoading input data set:\n************************************")

    # Start timing the process
    start = round(time.process_time(), 4)
    print("[ ", start," ]  Starting Script")

    # Load CSV file and store its data into a dataframe
    printMessage("Loading")
    try:
        df = pd.read_csv(file, sep=',')
        printMessage("Total Columns Read:", df.shape[1])
        printMessage("Total Rows Read:", df.shape[0])
        end = round(time.process_time(), 4)
        print("\nTime to load is: ", round((end - start), 4), "seconds")
        return df, True
    except FileNotFoundError:
        printMessage("Could not find file, please confirm it is in the correct directory")
        return None, False

# Menu option #2 (returns a boolean value of whether the data was fully cleaned and is ready to use)
def cleanData(df):
    print("\nCleaning data set:\n************************************")
    isProcessed = False

    # Start timing the process
    start = round(time.process_time(), 4)
    print("[ ", start, " ]  Performing Data Clean Up...")

    # First, confirm that all of the absolutely necessary columns exist in the file that has been loaded
    valid = True
    columns = ['ID', 'Severity', 'Start_Time', 'End_Time', 'Distance(mi)', 'City', 'State', 'Zipcode',
                'Country', 'Weather_Timestamp', 'Humidity(%)', 'Visibility(mi)', 'Weather_Condition']
    for column in columns:
        # Attempt to access each column
        try:
            df[column]
        # And catch it if it fails (indicating the column does not exist)
        except KeyError:
            printMessage("Invalid file format, cannot use data")
            valid = False
            break
    
    # Only continue processing the data if all of these columns exist
    if valid:
        # 1. Eliminate all rows with data missing in either of the following columns: ID, Severity, Zipcode, 
        # Start_Time, End_Time, Visibility(mi), Weather_Condition or Country
        df.drop(df[(df['ID'].isnull()) | (df['Severity'].isnull()) | (df['Zipcode'].isnull()) | 
        (df['Start_Time'].isnull()) | (df['End_Time'].isnull()) | (df['Visibility(mi)'].isnull()) | 
        (df['Weather_Condition'].isnull()) | (df['Country'].isnull())].index, inplace=True)
        
        # 2. Eliminate all rows with empty values in 3 or more columns
        # thresh: number of required non-NA values...(df.shape[1] returns the number of columns) then minus 3 
        df.dropna(thresh=(df.shape[1])-3, inplace=True)
        
        # 3. Eliminate all rows with distance equal to zero
        df.drop(df[df['Distance(mi)'] == 0].index, inplace=True)
        
        # 4. Only consider in your analysis the first 5 digits of the zipcode
        # Test cases: df.loc[(df['Zipcode'].str.len() > 5), 'Zipcode']
        zipOver5Digits = df['Zipcode'].str.len() > 5
        fixZips = df.loc[(zipOver5Digits), 'Zipcode'].index
        i = 0
        while i < len(fixZips):
            index = fixZips[i]
            df.at[index, "Zipcode"] = df["Zipcode"][index][0:5] 
            i = i + 1
        
        # 5. All accidents that lasted no time (The difference between End_Time and Start_Time is zero)
        df.drop(df[df['End_Time'] == df['Start_Time']].index, inplace=True)

        # Print the results
        end = round(time.process_time(), 4)
        printMessage("Total Rows Read after cleaning is finished:", df.shape[0])
        print("\nTime to process is: ", round((end - start), 3))
        isProcessed = True

    return isProcessed

# Menu option #3
def getAnswers(df):
    # For all these questions, Start_Time is used as the reference date to determine the year and month of the accident.
    print("\nAnswering questions:\n********************")

    # Short-circuit the function if there are no rows in the data frame
    if df.shape[0] == 0:
        printMessage("No data. File might be improperly formatted or corrupted.")
        return
    
    # 1. In what month were the most accidents reported?
    printMessage("1. The month with the most accidents reported is:")
    dfCopy = df.copy()
    dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time']).dt.strftime('%m')
    newMonth = dfCopy['Start_Time']
    n = 1
    finalMonth = int((newMonth.value_counts()[:n].index.tolist())[0])
    printMessage(getMonth(finalMonth))
    
    # 2. What is the state that had the most accidents in 2020?
    printMessage("2. The state with the most accidents reported in 2020 is:")
    printMessage(maxAccidentState("2020"))
    
    # 3. What is the state that had the most accidents of severity 2 in 2021?
    printMessage("3. The state with the most accidents of severity 2 in 2021 is:")
    printMessage(maxAccidentState("2021", 2))
    
    # 4. What severity is the most common in Virginia?
    printMessage("4. The severity most common in VA is:")
    printMessage("Severity:", sevByState("VA"))
    
    # 5. What are the 5 cities that had the most accidents in 2019 in California?
    printMessage("5. The 5 cities that had the most accidents in 2019 in CA are:")
    topCities = maxAccidentCities("2019", "CA", 5)
    printMessage("")
    for city in topCities:
        print("\t\t\t", city)
    
    # 6. What was the average humidity and average temperature of all accidents of severity 4 that occurred in 2021?
    printMessage("6. The average humidity and the average temperature of all accidents of severity 4 that occurred in 2021:")
    humidity, temperature = averageConditions("2021", 4)
    printMessage("")
    print("\t\t\tAverage humidity:", humidity ,"%\n\t\t\tAverage temperature is:", temperature, "F")
    
    # 7. What are the 3 most common weather conditions (weather_conditions) when accidents occurred?
    printMessage("7. The 3 most common weather conditions when accidents occurred are:")
    conditionCount = df['Weather_Condition'].value_counts()
    mostCommon = conditionCount.index[0:3]
    printMessage("")
    for i in mostCommon:
        print("\t\t\t", i)
    
    # 8. What was the maximum visibility of all accidents of severity 2 that occurred in the state of New Hampshire?
    printMessage("8. The maximum visibility of all accidents of severity 2 that occurred in the state of New Hampshire is:")
    printMessage(maxVisBySev_St(2, "NH"),"mi")
    
    # 9. How many accidents of each severity were recorded in Bakersfield?
    printMessage("9. The total accidents of each severity recorded in Bakersfield are:")
    total = totalBySevInCity('Bakersfield')
    printMessage("")
    s = 0
    for i in total:
        print("\t\t\tSeverity", total.index[s],":", i)
        s = s + 1
    
    # 10. What was the longest accident (in hours) recorded in Florida in the Spring (March, April, and May) of 2020?
    printMessage("10. The longest accident (in hours) recorded in Flordia in the Spring of 2020 is:")
    longAccidentTime = longestAcc(3, 5, "FL", 2020)
    if pd.notnull(longAccidentTime):
        printMessage(round(longAccidentTime/(3600),2), "hours.")
    else:
        printMessage("There were no accidents during this time in this state.")

# Menu option #4
def searchByLocation(df):
    print("\nSearch Accidents:\n*****************")

    # Short-circuit the function if there are no rows in the data frame
    if df.shape[0] == 0:
        printMessage("No data. File might be improperly formatted or corrupted.")
        return

    # Copy city, state, and zipcode columns 
    accidentsBySt_Cty_Zip = df[['City', 'State', 'Zipcode']]
    # Prompt user for city, state, and zipcode
    # --- If an empty value is inputted, search using all possibilities
    start = round(time.process_time(), 5)
    stateName = input("Enter State (Ex. California as CA): ")
    if not stateName:
        selectByState = pd.notnull(accidentsBySt_Cty_Zip['State'])
    else:
        while not simpleValidation('State', stateName):
            stateName = input("\nInvalid value, enter again or press enter to search for all possibilities: ")
        if not stateName:
            selectByState = pd.notnull(accidentsBySt_Cty_Zip['State'])
        else:
            selectByState = accidentsBySt_Cty_Zip['State'] == stateName

    cityName = input("Enter a City Name: ")
    if not cityName:
        selectByCity = pd.notnull(accidentsBySt_Cty_Zip['City'])
    else:
        while not validateCity(cityName, stateName):
            cityName = input("\nInvalid value, enter again or press enter to search for all possibilities: ")
        if not cityName:
            selectByCity = pd.notnull(accidentsBySt_Cty_Zip['City'])
        else: 
            selectByCity = accidentsBySt_Cty_Zip['City'] == cityName

    zipCode = input("Enter a ZIP Code: ")
    if not zipCode:
        selectByZip = pd.notnull(accidentsBySt_Cty_Zip['Zipcode'])
    else:
        while not validateZip(zipCode, cityName, stateName):
            zipCode = input("\nInvalid value, enter again or press enter to search for all possibilities: ")
        if not zipCode:
            selectByZip = pd.notnull(accidentsBySt_Cty_Zip['Zipcode'])
        else:
            selectByZip = accidentsBySt_Cty_Zip['Zipcode'] == zipCode

    # Start searching for rows by given data
    totalBySt_Cty_Zip = accidentsBySt_Cty_Zip[(selectByState) & (selectByCity) & (selectByZip)].count()
    print ("\nThere were", totalBySt_Cty_Zip.value_counts().index[0] , "accidents.")
    end = round(time.process_time(), 5)
    print("\nTime to perform search is:", round((end - start), 4), "seconds")

# Menu option #5
def searchByDate(df):
    print("\nSearch Accidents:\n*****************")

    # Short-circuit the function if there are no rows in the data frame
    if df.shape[0] == 0:
        printMessage("No data. File might be improperly formatted or corrupted.")
        return

    start = time.process_time()

    # Initialize an empty date format
    dateFormat = ''

    # Prompt the user for a year and validate it (can enter nothing to check every year)
    year = None
    while year is None:
        year = input("Enter a Year: ")
        # If the user entered nothing, proceed without a specific year
        if not year:
            year = ''
        # If the user entered something invalid, repeat the loop
        elif not validateYear(year):
            printMessage("\nInvalid year, try again or press enter to search all possibilities")
            year = None
        # If the user entered a valid year, add it to the date format and proceed
        else:
            dateFormat += '%Y'

    month = None
    while month is None:
        month = input("Enter a Month (1-12): ")

        # Ensure that month is two digits (e.g. 1 => 01)
        if len(month) == 1:
            month = "0" + month

        if not month:
            month = ''
        elif not validateMonth(month):
            printMessage("\nInvalid month, try again or press enter to search all possibilities")
            month = None
        else:
            dateFormat += '%m'

    day = None
    while day is None:
        day = input("Enter a Day (1-31): ")

        # Ensure that day is two digits (e.g. 1 => 01)
        if len(day) == 1:
            day = "0" + day

        if not day:
            day = ''
        elif not validateDay(day):
            printMessage("\nInvalid day, try again or press enter to search all possibilities")
            day = None
        else:
            dateFormat += '%d'

    # Count the number of times this date appears in the data frame
    dates = pd.to_datetime(df['Start_Time']).dt.strftime(dateFormat)
    date = str(year) + str(month) + str(day)
    count = 0
    try:
        count = dates.value_counts()[date]
    # If the date does not exist in the data frame, catch the error but don't do anything (count is already 0)
    except KeyError:
        pass

    end = time.process_time()
    print("\nThere were ", count, " accidents.")
    print("\nTime to perform search is:", round((end - start), 4), "seconds")

# Menu option #6
def searchByConditions(df):
    # Prompt user for a min/max temperature and min/max visibility
    print("\nSearch Accidents:\n*****************")

    # Short-circuit the function if there are no rows in the data frame
    if df.shape[0] == 0:
        printMessage("No data. File might be improperly formatted or corrupted.")
        return

    start = round(time.process_time(), 5)

    # Grab the columns from the dataset that are relevant to this question
    data = df[['Temperature(F)', 'Visibility(mi)']]

    # Ask for the minimum temperature
    minTemp = None
    while minTemp is None:
        minTemp = input("Enter a Minimum Temperature (F): ")
        # If the user does not enter anything, break the loop and don't include this condition
        if not minTemp:
            break
        else:
            try:
                minTemp = float(minTemp)
                # If the number provided is less than absolute zero or more than an arbitrarily huge number, reject it
                if minTemp < -459.67 or minTemp > 200:
                    print("\nInvalid input. Enter between -459 and 200 or press enter to search all possibilities.")
                    minTemp = None
                # However, if it's a valid number then narrow down our current data set to only compliant rows
                else:
                    data = data.loc[data['Temperature(F)'] >= minTemp]
            except ValueError:
                print("\nInvalid input. Please enter a number choice.")
                minTemp = None
    
    maxTemp = None
    while maxTemp is None:
        maxTemp = input("Enter a Maximum Temperature (F): ")
        # If the user does not enter anything, break the loop and don't include this condition
        if not maxTemp:
            break
        else:
            try:
                maxTemp = float(maxTemp)
                # If maxTemp is less than absolute zero, more than an arbitrarily huge number, or more than minTemp, reject it
                if maxTemp < -459.67 or maxTemp > 200 or (minTemp is not None and minTemp > maxTemp):
                    print("\nInvalid input. Enter between -459 and 200 and larger than minimum temperature, or press enter to search all possibilities.")
                    maxTemp = None
                # However, if it's a valid number then narrow down our current data subset to only compliant rows
                else:
                    data = data.loc[data['Temperature(F)'] <= maxTemp]
            except ValueError:
                print("\nInvalid input. Please enter a number choice.")
                maxTemp = None
        
    minVis = None
    while minVis is None:
        minVis = input("Enter a Minimum Visibility (mi): ")
        # If the user does not enter anything, break the loop and don't include this condition
        if not minVis:
            break
        else:
            try:
                minVis = float(minVis)
                # If the number provided is less than zero, reject it
                if minVis < 0:
                    print("\nInvalid input. Enter a number greater than 0 or press enter to search all possibilities.")
                    minVis = None
                # However, if it's a valid number then narrow down our current data subset to only compliant rows
                else:
                    data = data.loc[data['Visibility(mi)'] >= minVis]
            except ValueError:
                print("\nInvalid input. Please enter a number choice.")
                minVis = None

    maxVis = None
    while maxVis is None:
        maxVis = input("Enter a Maximum Visibility (mi): ")
        # If the user does not enter anything, break the loop and don't include this condition
        if not maxVis:
            break
        else:
            try:
                maxVis = float(maxVis)
                # If the number provided is less than zero or the minimum visibility, reject it
                if maxVis < 0 or (minVis is not None and minVis > maxVis):
                    print("\nInvalid input. Enter a number greater than 0 and the minimum visibility, or press enter to search all possibilities.")
                    maxVis = None
                # However, if it's a valid number then narrow down our current data subset to only compliant rows
                else:
                    data = data.loc[data['Visibility(mi)'] <= maxVis]
            except ValueError:
                print("\nInvalid input. Please enter a number choice.")
                maxVis = None

    # Print results
    print("\nThere were", data.shape[0], "accidents.")
    end = round(time.process_time(), 5)
    print("\nTime to perform search is:", round((end - start), 4), "seconds")

# Interfaces: A textual menu should be implemented in a way that the user could load several samples of the same data 
# set (all data cleaning steps would be the same).
loop = True  
isLoaded = False     
isProcessed = False
while loop:          
    printMenu()
    choice = input("Enter your choice [1-7]: ")
    try:
        choice = int(choice)

        # Option 1: Load the data from the CSV file
        if choice == 1:
            file = input("Enter the name of the file to load: ")
            isProcessed = False
            df, isLoaded = readFile()
            
        # Catch options 2-6 if the data has not been loaded
        elif (choice >= 2 and choice <= 6) and not isLoaded:
            print("You need to load data first. Please enter '1', then try again...")

        # Option 2: Clean the data (but only if it's already been loaded)
        elif choice == 2 and isLoaded:
            isProcessed = cleanData(df)

        # Catch options 3-6 if the data has not been cleaned
        elif (choice >= 3 and choice <= 6) and not isProcessed:
            print("You need to process data first. Please enter '2', then try again...")

        # Option 3: Display answers to preset questions
        elif choice == 3 and isProcessed:
            getAnswers(df)

        # Option 4: Conduct a search by state, city, and ZIP
        elif choice == 4 and isProcessed:
            searchByLocation(df)

        # Option 5: Conduct a search by year, month, and day
        elif choice == 5 and isProcessed:
            searchByDate(df)

        # Option 6: Conduct a search by temperature and visibility
        elif choice == 6 and isProcessed:
            searchByConditions(df)

        # Option 7: Exit
        elif choice == 7:
            loop = False
            print("\nTotal Running Time (In Minutes):", round(time.process_time()/(60), 5), "minutes\n")

        # Catch any unrecognized input (e.g. outside the range 1-7)
        else:
            print("Invalid input. Please enter a valid choice [1-7].")

    # Catch any invalid input (e.g. not an integer)
    except ValueError:
        print("Invalid input. Please enter a number choice.") 
