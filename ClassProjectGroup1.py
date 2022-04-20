# CLASS Project
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# COURSE: CMPS 3500
# DATE: 04/06/22
# Student 1:
# Student 2: 
# Student 3: 
# Student 4:
# DESCRIPTION: Implementation Basic Data Analysys Routines
import time
import pandas as pd

# Output: Implemented functions to answer the following questions about any data sets provided:
def print_menu():
    print()
    print(60 * "-" , "MENU" , 60 * "-")
    print("1. Display our answers")
    print("2. Get state with the most accidents in a given year.")
    print("3. Get state that had the most accidents of a given severity and year.")
    print("4. Get the most common severity in a given state.")
    print("5. Get the 5 cities that had the most accidents in a given year and state.")
    print("6. Get the average humidity and average temperature of all accidents of given severity and year.")
    print("7. Get the maximum visibility of all accidents of a given severity and given state.")
    print("8. Get the total accidents of each severity recorded in a given city.")
    print("9. Get the longest accident (in hours) recorded in a given state, month period, and year.")
    print("10. Exit")
    print(126 * "-")
# Validate if input is in the dataframe
def validateYear(input):
    dfCopy = df.copy()
    dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time']).dt.strftime('%Y')
    if input not in dfCopy.values:
        return False
    else:
        return True
def validateMonth(input):
    dfCopy = df.copy()
    dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time']).dt.strftime('%m')
    if input not in dfCopy.values:
        return False
    else:
        return True
def anyOtherValidation(input):
    if input not in df.values:
        return False
    else:
        return True
# Used to answer question 1.
def getMonth(month):
    theMonths = ["January","February","March","April", "May", "June", "July", "August", 
    "September", "October", "November","December"]
    monthName = theMonths[month-1]
    return monthName
# To answer questions in the structure: "What is the state that had the most accidents in 2020?", with a given year.
def mostAccInStByYR(yr):
    dfCopy = df.copy()
    dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time']).dt.strftime('%Y')
    accidentsByYrInSt = dfCopy[['Start_Time','State']]
    mostByStInYr = accidentsByYrInSt[accidentsByYrInSt['Start_Time'] == yr].value_counts().index[0]
    state = mostByStInYr[1]
    return state
# To answer questions in the structure: "What is the state that had the most accidents of severity 2 in 2021?", with
# a given year and severity.
def mostAccInStBySev_YR(yr, sev):
    dfCopy = df.copy()
    dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time']).dt.strftime('%Y')
    accidentsByYr_SvtyInST = dfCopy[['Start_Time','State','Severity']]
    mostByYr_SvtyInST = accidentsByYr_SvtyInST[(accidentsByYr_SvtyInST['Start_Time'] == yr) 
    & (accidentsByYr_SvtyInST['Severity'] == sev)].value_counts().index[0]
    state = mostByYr_SvtyInST[1]
    return state
# To answer questions in the structure: "What severity is the most common in Virginia?", with given state.
def sevByState(st):
    dfCopy = df.copy()
    accidentsBySvtyInST = dfCopy[['State','Severity']]
    mostBySvtyInST = accidentsBySvtyInST[(accidentsBySvtyInST['State'] == st)].value_counts().index[0]
    severity = mostBySvtyInST[1]
    return severity
# To answer questions in the structure: "What are the 5 cities that had the most accidents in 2019 in California?", with
# given year and state.
def fiveCitiesByYR_ST(yr, st):
    dfCopy = df.copy()
    dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time']).dt.strftime('%Y')
    accidentsByYr_St_Cty = dfCopy[['Start_Time','State','City']]
    mostByYr_St_Cty = accidentsByYr_St_Cty[(accidentsByYr_St_Cty['State'] == st) 
    & (accidentsByYr_St_Cty['Start_Time'] == yr)].value_counts().index[0:5]
    cities = mostByYr_St_Cty.get_level_values('City')
    return cities
# To answer questions in the structure: "What was the average humidity and average temperature of 
# all accidents of severity 4 that occurred in 2021?", with given year and severity.
def avgHumid_TempBySev_YR(yr, sev):
    dfCopy = df.copy()
    dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time']).dt.strftime('%Y')
    accidentsByHumid_Temp_Sev_Yr = dfCopy[['Start_Time','Severity','Humidity(%)','Temperature(F)']]
    accidentsByHumid_Temp_Sev_Yr = accidentsByHumid_Temp_Sev_Yr[(accidentsByHumid_Temp_Sev_Yr['Start_Time'] == yr) 
    & (accidentsByHumid_Temp_Sev_Yr['Severity'] == sev)]
    averageHumidity = accidentsByHumid_Temp_Sev_Yr['Humidity(%)'].mean()
    averageTemperature = accidentsByHumid_Temp_Sev_Yr['Temperature(F)'].mean()
    return averageHumidity, averageTemperature
# To answer questions in the structure: "What was the maximum visibility of all accidents of severity 2 
# that occurred in the state of New Hampshire?", with given severity and state.
def maxVisBySev_St(sev, st):
    dfCopy = df.copy()
    accidentsByVisibility_Sev_State = dfCopy[['Visibility(mi)', 'Severity', 'State']]
    accidentsByVisibility_Sev_State = accidentsByVisibility_Sev_State[(accidentsByVisibility_Sev_State['State'] == st) 
    & (accidentsByVisibility_Sev_State['Severity'] == sev)]
    maxVisibility = accidentsByVisibility_Sev_State['Visibility(mi)'].max()
    return maxVisibility
# To answer questions in the structure: "How many accidents of each severity were recorded in
# Bakersfield?", with given city.
def totalBySevInCity(city):
    dfCopy = df.copy()
    accidentsBySvtyInST = dfCopy[['City','Severity']]
    totalBySvtyInST = accidentsBySvtyInST.loc[(accidentsBySvtyInST['City'] == city), 'Severity'].value_counts()
    return totalBySvtyInST
# To answer questions in the structure: "What was the longest accident (in hours) recorded in Florida 
# in the Spring (March, April, and May) of 2022?" with given month range, state, and year.
def longestAcc(startMonth, endMonth, st, yr):
    dfCopy = df.copy()
    dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time'])
    dfCopy['End_Time'] = pd.to_datetime(dfCopy['End_Time'])
    accidentsByTime_ST = dfCopy[['Start_Time','End_Time','State']]
    betweenMonths = accidentsByTime_ST['Start_Time'].dt.month.between(startMonth,endMonth)
    betweenMonths = accidentsByTime_ST[betweenMonths]
    accidentsByTime_ST_Month = betweenMonths[(betweenMonths['State'] == st) 
    & (pd.to_datetime(betweenMonths['Start_Time']).dt.year  == yr)]
    totalTimeOfAccident = accidentsByTime_ST_Month['End_Time'] - accidentsByTime_ST_Month['Start_Time']
    longestAccident = totalTimeOfAccident.max()
    longestAccidentInSecs = (longestAccident.days*86400) + (longestAccident.seconds)
    return longestAccidentInSecs
def getAnswers():
    # For all these question, Start_Time is used as the reference date to determine the year and month of the accident.
    print()
    print("Answering questions:")
    print("********************")
        # 1. In what month were there more accidents reported?
    print("[ ", time.process_time()," ] 1. The month with the most accidents reported is:")
    dfCopy = df.copy()
    dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time']).dt.strftime('%m')
    newMonth = dfCopy['Start_Time']
    n = 1
    finalMonth = int((newMonth.value_counts()[:n].index.tolist())[0])
    print("[ ", time.process_time()," ]", getMonth(finalMonth))
        # 2. What is the state that had the most accidents in 2020?
    print("[ ", time.process_time()," ] 2. The state with the most accidents reported in 2020 is:")
    print("[ ", time.process_time()," ]", mostAccInStByYR("2020"))
        # 3. What is the state that had the most accidents of severity 2 in 2021?
    print("[ ", time.process_time()," ] 3. The state with the most accidents of severity 2 in 2021 is:")
    print("[ ", time.process_time()," ]", mostAccInStBySev_YR("2021", 2))
        # 4. What severity is the most common in Virginia?
    print("[ ", time.process_time()," ] 4. The severity most common in VA is:")
    print("[ ", time.process_time()," ] Severity:", sevByState("VA"))
        # 5. What are the 5 cities that had the most accidents in 2019 in California?
    print("[ ", time.process_time()," ] 5. The 5 cities that had the most accidents in 2019 in CA are:")
    print("[ ", time.process_time()," ]")
    for i in fiveCitiesByYR_ST("2019", "CA"):
        print("\t\t\t", i)
        # 6. What was the average humidity and average temperature of all accidents of severity 4 that occurred in 2021?
    print("[ ", time.process_time()," ] 6. The average humidity and the average temperature of all accidents of severity 4 that occurred in 2021:")
    average = avgHumid_TempBySev_YR("2021", 4)
    print("[ ", time.process_time()," ]")
    print("\t\t\tAverage humidity:", average[0] ,"%\n\t\t\tAverage temperature is:", average[1], "F")
        # 7. What are the 3 most common weather conditions (weather_conditions) when accidents occurred?
    print("[ ", time.process_time()," ] 7. The 3 most common weather conditions when accidents occurred are:")
    dfCopy = df.copy()
    accidentsByWeather = dfCopy[['Weather_Condition']]
    mostByWeather= accidentsByWeather.value_counts().index[0:3]
    weathers = mostByWeather.get_level_values('Weather_Condition')
    print("[ ", time.process_time()," ]")
    for i in weathers:
        print("\t\t\t", i)
        # 8. What was the maximum visibility of all accidents of severity 2 that occurred in the state of New Hampshire?
    print("[ ", time.process_time()," ] 8. The maximum visibility of all accidents of severity 2 that occurred in the state of New Hampshire is:")
    print("[ ", time.process_time()," ]", maxVisBySev_St(2, "NH"),"mi")
        # 9. How many accidents of each severity were recorded in Bakersfield?
    print("[ ", time.process_time()," ] 9. The total accidents of each severity recorded in Bakersfield are:")
    total = totalBySevInCity('Bakersfield')
    print("[ ", time.process_time()," ]")
    s = 0
    for i in total:
        print("\t\t\tSeverity", total.index[s],":", i)
        s = s + 1
        # 10. What was the longest accident (in hours) recorded in Florida in the Spring (March, April, and May) of 2022?
    print("[ ", time.process_time()," ] 10. The longest accident (in hours) recorded in Flordia in the Spring of 2022 is:")
    print("[ ", time.process_time()," ]", longestAcc(3, 5, "FL", 2022)/(3600), "hours.")

# Data Loading: Read data from the csv files
print("Loading and cleaning input data set:")
print("************************************")
# !!!REMOVE PERIOD IN FRONT OF FILE NAME ONCE DONE WITH PROJECT!!!
file = '.US_Accidents_data.csv'                      # Has a TOTAL of 711336 written lines
# Load CSV file and store its data into a dataframe
start = time.process_time()
print("[ ", start," ] Starting Script")
print("[ ", time.process_time()," ] Loading US_Accidents_data.csv")
df = pd.read_csv(file, sep=',')
print("[ ", time.process_time()," ] Performing Data Clean Up...")
# Data Cleaning: Performing the following cleaning tasks...
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
fixZips = df.loc[(df['Zipcode'].str.len() > 5), 'Zipcode'].index
i = 0
while i < len(fixZips):
    index = fixZips[i]
    df.at[index, "Zipcode"] = df["Zipcode"][index][0:5] 
    i = i + 1
    # 5. All accidents that lasted no time (The difference between End_Time and Start_Time is zero) (No data like this?)
    #df.drop(df[df['End_Time'] == df['Start_Time']].index, inplace=True)
print("[ ", time.process_time()," ] Printing row count after data cleaning is finished:")
print("[ ", time.process_time()," ]", len(df.index))

getAnswers()
print("\nTotal Running Time (In Minutes):", (time.process_time())/(60), "minutes")

# Interfaces: A textual menu should be implemented in a way that the user could load several samples of the same data 
# set (all data cleaning steps would be the same). 
# During the demo you will be ask to load several data sets with the same structure.
loop = True      
while loop:          
    print_menu()
    choice = input("Enter your choice [1-10]: ")
    if choice == '1':     
        getAnswers()
    elif choice == '2':
        year = input("Please enter a year between 2016 and 2021: ")
        if(validateYear(year) == False):
            print("There is no data recorded under that year.")
        else:
            state = mostAccInStByYR(year)
            print("The state with the most accidents reported in", year, "is:", state)
    elif choice == '3':
        print ("3")
    elif choice == '4':
        print ("4")
    elif choice == '5':
        print ("5")
    elif choice == '6':
        print ("6")
    elif choice == '7':
        print ("7")
    elif choice == '8':
        print ("8")
    elif choice == '9':
        print ("9")
    elif choice == '10':
        loop = False
    else:
        print("Invalid input. Please enter a valid choice...")