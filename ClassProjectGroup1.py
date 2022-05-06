# CLASS Project
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# COURSE: CMPS 3500
# DATE: 04/06/22
# Student 1:
# Student 2: 
# Student 3: 
# Student 4:
# DESCRIPTION: Implementation Basic Data Analysys Routines
# TO DO: LINES 438
import time
import pandas as pd

# Output: Implemented functions to answer the following questions about any data sets provided:
def print_menu():
    print()
    print(60 * "-" , "MENU" , 60 * "-")
    print("1. Load Data")
    print("2. Process Data.")
    print("3. Print Answers.")
    print("4. Search Accidents (Use City, State, and Zip Code).")
    print("5. Search Accidents (Year, Month, and Day).")
    print("6. Search Accidents (Temperature Range and Visibility Range).")
    print("7. Exit")
    print(126 * "-")

# Validatation: Validate if input is in the dataframe
def validateState(input):
    if not input:
        return True
    if input not in df['State'].values:
        return False
    else:
        return True

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

def validateYear(input):
    if not input:
        return True
    dfCopy = df.copy()
    dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time']).dt.strftime('%Y')
    if input not in dfCopy.values:
        return False
    else:
        return True

def validateMonth(input):
    if not input:
        return True
    dfCopy = df.copy()
    dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time']).dt.strftime('%m')
    if input not in dfCopy.values:
        return False
    else:
        return True

def validateDay(input):
    if not input:
        return True
    dfCopy = df.copy()
    dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time']).dt.strftime('%d')
    if input not in dfCopy.values:
        return False
    else:
        return True

def validateTemp(input):
    if not input:
        return True
    if input not in df['Temperature(F)'].values:
        return False
    else:
        return True

def validateVis(input):
    if not input:
        return True
    if input not in df['Visibility(mi)'].values:
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

# Used to answer question 1.
def getMonth(month):
    theMonths = ["January","February","March","April", "May", "June", "July", "August", "September", "October", "November","December"]
    monthName = theMonths[month-1]
    return monthName

# To answer questions in the structure: "What is the state that had the most accidents in 2020?", with a given year.
def mostAccInStByYR(yr):
    # Copy original dataframe to modify Start_Time by year
    dfCopy = df.copy()
    dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time']).dt.strftime('%Y')
    # Copy columns Start_Time and State into a new dataframe to focus on specific columns based on the question
    questionDF = dfCopy[['Start_Time','State']]
    # Select only rows by given year
    selectByYear = questionDF['Start_Time'] == yr
    # Count the number of year appearances by State and get the top result
    possibleAnswers = questionDF[selectByYear].value_counts().index[0]
    state = possibleAnswers[1]
    return state

# To answer questions in the structure: "What is the state that had the most accidents of severity 2 in 2021?", with
# a given year and severity.
def mostAccInStBySev_YR(yr, sev):
    # Copy original dataframe to modify Start_Time by year
    dfCopy = df.copy()
    dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time']).dt.strftime('%Y')
    # Copy columns Start_Time, State, and Severity into a new dataframe to focus on specific columns based on the question
    questionDF = dfCopy[['Start_Time','State','Severity']]
    # Select only rows by given year and severity
    selectByYear = questionDF['Start_Time'] == yr
    selectBySev = questionDF['Severity'] == sev
    # Count the number of year AND severity appearances by state and get the top result
    possibleAnswers = questionDF[(selectByYear) & (selectBySev)].value_counts().index[0]
    state = possibleAnswers[1]
    return state

# To answer questions in the structure: "What severity is the most common in Virginia?", with given state.
def sevByState(st):
    # Copy columns State and Severity into a new dataframe to focus on specific columns based on the question
    dfCopy = df.copy()
    questionDF = dfCopy[['State','Severity']]
    # Select only rows by given state
    selectByState = questionDF['State'] == st
    # Count the number of state appearances by severity and get the top result
    possibleAnswers = questionDF[selectByState].value_counts().index[0]
    severity = possibleAnswers[1]
    return severity

# To answer questions in the structure: "What are the 5 cities that had the most accidents in 2019 in California?", with
# given year and state.
def fiveCitiesByYR_ST(yr, st):
    # Copy original dataframe to modify Start_Time by year
    dfCopy = df.copy()
    dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time']).dt.strftime('%Y')
    # Copy columns Start_Time, State, and City into a new dataframe to focus on specific columns based on the question
    questionDF = dfCopy[['Start_Time','State','City']]
    # Select only rows by given state and year
    selectByState = questionDF['State'] == st
    selectByYear = questionDF['Start_Time'] == yr
    # Count the number of state AND year appearances by city and get the top 5 results
    possibleAnswers = questionDF[(selectByState) & (selectByYear)].value_counts().index[0:5]
    cities = possibleAnswers.get_level_values('City')
    return cities

# To answer questions in the structure: "What was the average humidity and average temperature of 
# all accidents of severity 4 that occurred in 2021?", with given year and severity.
def avgHumid_TempBySev_YR(yr, sev):
    # Copy original dataframe to modify Start_Time by year
    dfCopy = df.copy()
    dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time']).dt.strftime('%Y')
    # Copy columns Start_Time, Severity, Humidity(%), and Temperature(F) into a new dataframe to focus on specific columns based on the question
    questionDF = dfCopy[['Start_Time','Severity','Humidity(%)','Temperature(F)']]
    # Select only rows by given state and severity
    selectByYear = questionDF['Start_Time'] == yr
    selectBySeverity = questionDF['Severity'] == sev
    questionDF = questionDF[(selectByYear) & (selectBySeverity)]
    # Get the average (mean) of the humidity and temperature from the dataframe created to fit the question conditions
    averageHumidity = questionDF['Humidity(%)'].mean()
    averageTemperature = questionDF['Temperature(F)'].mean()
    averageHumidity = round(averageHumidity, 2)
    averageTemperature = round(averageTemperature, 2)
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

def getAnswers():
    # For all these questions, Start_Time is used as the reference date to determine the year and month of the accident.
    print("\nAnswering questions:\n********************")
        # 1. In what month were there more accidents reported?
    print("[ ", round(time.process_time(), 5)," ] 1. The month with the most accidents reported is:")
    dfCopy = df.copy()
    dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time']).dt.strftime('%m')
    newMonth = dfCopy['Start_Time']
    n = 1
    finalMonth = int((newMonth.value_counts()[:n].index.tolist())[0])
    print("[ ", round(time.process_time(), 4)," ]", getMonth(finalMonth))
        # 2. What is the state that had the most accidents in 2020?
    print("[ ", round(time.process_time(), 4)," ] 2. The state with the most accidents reported in 2020 is:")
    print("[ ", round(time.process_time(), 4)," ]", mostAccInStByYR("2020"))
        # 3. What is the state that had the most accidents of severity 2 in 2021?
    print("[ ", round(time.process_time(), 4)," ] 3. The state with the most accidents of severity 2 in 2021 is:")
    print("[ ", round(time.process_time(), 4)," ]", mostAccInStBySev_YR("2021", 2))
        # 4. What severity is the most common in Virginia?
    print("[ ", round(time.process_time(), 4)," ] 4. The severity most common in VA is:")
    print("[ ", round(time.process_time(), 4)," ] Severity:", sevByState("VA"))
        # 5. What are the 5 cities that had the most accidents in 2019 in California?
    print("[ ", round(time.process_time(), 4)," ] 5. The 5 cities that had the most accidents in 2019 in CA are:")
    print("[ ", round(time.process_time(), 4)," ]")
    for i in fiveCitiesByYR_ST("2019", "CA"):
        print("\t\t\t", i)
        # 6. What was the average humidity and average temperature of all accidents of severity 4 that occurred in 2021?
    print("[ ", round(time.process_time(), 4)," ] 6. The average humidity and the average temperature of all accidents of severity 4 that occurred in 2021:")
    average = avgHumid_TempBySev_YR("2021", 4)
    print("[ ", round(time.process_time(), 4)," ]")
    print("\t\t\tAverage humidity:", average[0] ,"%\n\t\t\tAverage temperature is:", average[1], "F")
        # 7. What are the 3 most common weather conditions (weather_conditions) when accidents occurred?
    print("[ ", round(time.process_time(), 4)," ] 7. The 3 most common weather conditions when accidents occurred are:")
    dfCopy = df.copy()
    accidentsByWeather = dfCopy[['Weather_Condition']]
    mostByWeather= accidentsByWeather.value_counts().index[0:3]
    weathers = mostByWeather.get_level_values('Weather_Condition')
    print("[ ", round(time.process_time(), 4)," ]")
    for i in weathers:
        print("\t\t\t", i)
        # 8. What was the maximum visibility of all accidents of severity 2 that occurred in the state of New Hampshire?
    print("[ ", round(time.process_time(), 4)," ] 8. The maximum visibility of all accidents of severity 2 that occurred in the state of New Hampshire is:")
    print("[ ", round(time.process_time(), 4)," ]", maxVisBySev_St(2, "NH"),"mi")
        # 9. How many accidents of each severity were recorded in Bakersfield?
    print("[ ", round(time.process_time(), 4)," ] 9. The total accidents of each severity recorded in Bakersfield are:")
    total = totalBySevInCity('Bakersfield')
    print("[ ", round(time.process_time(), 4)," ]")
    s = 0
    for i in total:
        print("\t\t\tSeverity", total.index[s],":", i)
        s = s + 1
        # 10. What was the longest accident (in hours) recorded in Florida in the Spring (March, April, and May) of 2020?
    print("[ ", round(time.process_time(), 4)," ] 10. The longest accident (in hours) recorded in Flordia in the Spring of 2020 is:")
    longAccidentTime = longestAcc(3, 5, "FL", 2020)
    if pd.notnull(longAccidentTime):
        print("[ ", round(time.process_time(), 4)," ]", round(longAccidentTime/(3600),2), "hours.")
    else:
        print("[ ", round(time.process_time(), 4)," ] There were no accidents during this time in this state.")

# Interfaces: A textual menu should be implemented in a way that the user could load several samples of the same data 
# set (all data cleaning steps would be the same).
loop = True  
isLoaded = False     
isProcessed = False
while loop:          
    print_menu()
    choice = input("Enter your choice [1-7]: ")
    try:
        choice = int(choice)

        # Data Loading: Read data from the csv files
        if choice == 1:     
            print("\nLoading input data set:\n************************************")
            start = round(time.process_time(), 4)
            print("[ ", start," ] Starting Script")
            file = 'US_Accidents_data.csv'                      # Has a TOTAL of 711336 written lines
            # Load CSV file and store its data into a dataframe
            print("[ ", round(time.process_time(), 4)," ] Loading US_Accidents_data.csv")
            df = pd.read_csv(file, sep=',')
            print("[ ", round(time.process_time(), 4)," ] Total Columns Read:", df.shape[1])
            print("[ ", round(time.process_time(), 4)," ] Total Rows Read:", df.shape[0])
            end = round(time.process_time(), 4)
            print("\nTime to load is: ", round((end - start), 4), "seconds")
            isLoaded = True
        
        # Make sure data has been loaded first in order to clean data...
        elif choice == 2 and isLoaded == False:
            print("You need to load data first. Please enter '1', then try again...")
        
        # Data Cleaning: Performing the cleaning tasks
        elif choice == 2 and isLoaded == True:
            print("\nCleaning data set:\n************************************")
            start = round(time.process_time(), 3)
            print("[ ", start," ] Performing Data Clean Up...")
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
                # 5. All accidents that lasted no time (The difference between End_Time and Start_Time is zero) (No data like this?)
                #df.drop(df[df['End_Time'] == df['Start_Time']].index, inplace=True)
            print("[ ", round(time.process_time(), 3)," ] Total Rows Read after cleaning is finished:", df.shape[0])
            end = round(time.process_time(), 4)
            print("\nTime to process is: ", round((end - start), 3))
            isProcessed = True
        
        # Make sure data has been loaded/processed (cleaned) first in order to display data...
        elif (choice >= 3 and choice <= 6) and isLoaded == False:
            print("You need to load data first. Please enter '1', then try again...")
        elif (choice >= 3 and choice <= 6) and isProcessed == False:
            print("You need to process data first. Please enter '2', then try again...")
        
        # Display answers to questions
        elif choice == 3 and isProcessed == True:
            getAnswers()
        
        # Searching capability
        elif choice == 4 and isProcessed == True:
            print("\nSearch Accidents:\n*****************")
            # Copy city, state, and zipcode columns 
            accidentsBySt_Cty_Zip = df[['City', 'State', 'Zipcode']]
            # Prompt user for city, state, and zipcode
            # --- If an empty value is inputted, search using all possibilities
            start = round(time.process_time(), 5)
            stateName = input("Enter State (Ex. California as CA): ")
            if not stateName:
                selectByState = pd.notnull(accidentsBySt_Cty_Zip['State'])
            else:
                while validateState(stateName) == False:
                    stateName = input("Invalid value, enter again or press enter to search for all possibilities: ")
                if not stateName:
                    selectByState = pd.notnull(accidentsBySt_Cty_Zip['State'])
                else:
                    selectByState = accidentsBySt_Cty_Zip['State'] == stateName

            cityName = input("Enter a City Name: ")
            if not cityName:
                selectByCity = pd.notnull(accidentsBySt_Cty_Zip['City'])
            else:
                while validateCity(cityName, stateName) == False:
                    cityName = input("Invalid value, enter again or press enter to search for all possibilities: ")
                if not cityName:
                    selectByCity = pd.notnull(accidentsBySt_Cty_Zip['City'])
                else: 
                    selectByCity = accidentsBySt_Cty_Zip['City'] == cityName

            zipCode = input("Enter a ZIP Code: ")
            if not zipCode:
                selectByZip = pd.notnull(accidentsBySt_Cty_Zip['Zipcode'])
            else:
                while validateZip(zipCode, cityName, stateName) == False:
                    zipCode = input("Invalid value, enter again or press enter to search for all possibilities: ")
                if not zipCode:
                    selectByZip = pd.notnull(accidentsBySt_Cty_Zip['Zipcode'])
                else:
                    selectByZip = accidentsBySt_Cty_Zip['Zipcode'] == zipCode

            # Start searching for rows by given data
            totalBySt_Cty_Zip = accidentsBySt_Cty_Zip[(selectByState) & (selectByCity) & (selectByZip)].count()
            print ("\nThere were", totalBySt_Cty_Zip.value_counts().index[0] , "accidents.")
            end = round(time.process_time(), 5)
            print("\nTime to perform search is:", round((end - start), 4), "seconds")
        
        elif choice == 5 and isProcessed == True:
            # TO DO: Takes about 15-30+ seconds, any faster way?
            print("\nSearch Accidents:\n*****************")
            # Copy start time column
            dfCopy = df.copy()
            dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time']).dt.strftime('%Y%m%d')
            accidentsByYr_Mth_Day = dfCopy[['Start_Time']]
            # Prompt user for year, month, and day
            # --- If an empty value is inputted, search using all possibilities
            start = round(time.process_time(), 5)
            accYear = input("Enter a Year: ")
            if not accYear:
                selectByYear = pd.notnull(pd.to_datetime(accidentsByYr_Mth_Day['Start_Time']).dt.strftime('%Y'))
            else:
                while validateYear(accYear) == False:
                    accYear = input("Invalid value, enter again or press enter to search for all possibilities: ")
                if not accYear:
                    selectByYear = pd.notnull(pd.to_datetime(accidentsByYr_Mth_Day['Start_Time']).dt.strftime('%Y'))
                else:
                    selectByYear = pd.to_datetime(accidentsByYr_Mth_Day['Start_Time']).dt.strftime('%Y') == accYear

            accMonth = input("Enter a Month: ")
            if not accMonth:
                selectByMonth = pd.notnull(pd.to_datetime(accidentsByYr_Mth_Day['Start_Time']).dt.strftime('%m'))
            else:
                if len(accMonth) < 2:
                    accMonth = '0' + accMonth
                while validateMonth(accMonth) == False:
                    accMonth = input("Invalid value, enter again or press enter to search for all possibilities: ")
                if not accMonth:
                    selectByMonth = pd.notnull(pd.to_datetime(accidentsByYr_Mth_Day['Start_Time']).dt.strftime('%m'))
                else:
                    selectByMonth = pd.to_datetime(accidentsByYr_Mth_Day['Start_Time']).dt.strftime('%m') == accMonth

            accDay = input("Enter a Day: ")
            if not accDay:
                selectByDay = pd.notnull(pd.to_datetime(accidentsByYr_Mth_Day['Start_Time']).dt.strftime('%d'))
            else:
                if len(accDay) < 2:
                    accDay = '0' + accDay
                while validateDay(accDay) == False:
                    accDay = input("Invalid value, enter again or press enter to search for all possibilities: ")
                if not accDay:
                    selectByDay = pd.notnull(pd.to_datetime(accidentsByYr_Mth_Day['Start_Time']).dt.strftime('%d'))
                else:
                    selectByDay = pd.to_datetime(accidentsByYr_Mth_Day['Start_Time']).dt.strftime('%d') == accDay

            # Start searching for rows by given data
            totalByYr_Mth_Day = accidentsByYr_Mth_Day[(selectByYear) & (selectByMonth) & (selectByDay)].count()
            print("\nThere were",totalByYr_Mth_Day.value_counts().index[0], "accidents.")
            end = round(time.process_time(), 5)
            print("\nTime to perform search is:", round((end - start), 4), "seconds")
        
        elif choice == 6 and isProcessed == True:
            print("\nSearch Accidents:\n*****************")
            # Copy temperature and visibility columns
            accidentsByTemp_Vis = df[['Temperature(F)', 'Visibility(mi)']]
            # Prompt user for a min/max temperature and min/max visibility
            # --- If an empty value is inputted, search using all possibilities
            start = round(time.process_time(), 5)
            askForMinTemp = True
            while askForMinTemp:
                minTemp = input("Enter a Minimum Temperature (F): ")
                if not minTemp:
                    selectByMinTemp = pd.notnull(accidentsByTemp_Vis['Temperature(F)'])
                    askForMinTemp = False
                else:
                    try:
                        minTemp = float(minTemp)
                        while validateTemp(minTemp) == False:
                            minTemp = input("Invalid value, enter again or press enter to search for all possibilities: ")
                        if not minTemp:
                            selectByMinTemp = pd.notnull(accidentsByTemp_Vis['Temperature(F)'])
                            askForMinTemp = False
                        else:
                            selectByMinTemp = accidentsByTemp_Vis['Temperature(F)'] > minTemp
                            askForMinTemp = False
                    except ValueError:
                        print("Invalid input. Please enter a number choice.")
                
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
                            if maxTemp < minTemp:
                                print("Invalid input. Maximum temperature must be greater than the minimum temperature.")
                        else:
                            while validateTemp(maxTemp) == False:
                                maxTemp = input("Invalid value, enter again or press enter to search for all possibilities: ")
                            if not maxTemp:
                                selectByMaxTemp = pd.notnull(accidentsByTemp_Vis['Temperature(F)'])
                                askForMaxTemp = False
                            else:
                                selectByMaxTemp = accidentsByTemp_Vis['Temperature(F)'] < maxTemp
                                askForMaxTemp = False
                    except ValueError:
                        print("Invalid input. Please enter a number choice.")

            askForMinVis = True
            while askForMinVis:
                minVis = input("Enter a Minimum Visibility (mi): ")
                if not minVis:
                    selectByMinVis = pd.notnull(accidentsByTemp_Vis['Visibility(mi)'])
                    askForMinVis = False
                else:
                    try:
                        minVis = float(minVis)
                        while validateVis(minVis) == False:
                            minVis = input("Invalid value, enter again or press enter to search for all possibilities: ")
                        if not minVis:
                            selectByMinVis = pd.notnull(accidentsByTemp_Vis['Visibility(mi)'])
                            askForMinVis = False
                        else:
                            selectByMinVis = accidentsByTemp_Vis['Visibility(mi)'] > minVis
                            askForMinVis = False
                    except ValueError:
                        print("Invalid input. Please enter a number choice.")

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
                            if maxVis < minVis:
                                print("Invalid input. Maximum visibility must be greater than the minimum visibility.")
                        else:
                            while validateVis(maxVis) == False:
                                maxVis = input("Invalid value, enter again or press enter to search for all possibilities: ")
                            if not maxVis:
                                selectByMaxVis = pd.notnull(accidentsByTemp_Vis['Visibility(mi)'])
                                askForMaxVis = False
                            else:
                                selectByMaxVis = accidentsByTemp_Vis['Visibility(mi)'] < maxVis
                                askForMaxVis = False
                    except ValueError:
                        print("Invalid input. Please enter a number choice.")

            # Start searching for rows by given data
            totalByTemp_Vis = accidentsByTemp_Vis[(selectByMinTemp) & (selectByMaxTemp) & (selectByMinVis) & (selectByMaxVis)].count()
            print("\nThere were",totalByTemp_Vis.value_counts().index[0], "accidents.")
            end = round(time.process_time(), 5)
            print("\nTime to perform search is:", round((end - start), 4), "seconds")
        
        elif choice == 7:
            loop = False
            print("\nTotal Running Time (In Minutes):", round(time.process_time()/(60), 5), "minutes\n")
        else:
            print("Invalid input. Please enter a valid choice [1-7].")
    except ValueError:
        print("Invalid input. Please enter a number choice.") 
    