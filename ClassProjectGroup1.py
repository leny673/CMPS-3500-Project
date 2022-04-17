# CLASS Project
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# COURSE: CMPS 3500
# DATE: 04/06/22
# Student 1: Elena Castaneda
# Student 2: 
# Student 3: 
# Student 4:
# DESCRIPTION: Implementation Basic Data Analysys Routines
from decimal import Rounded
import time
from numpy import ones
import pandas as pd
# ------ All functions must be implemented by the team, predesigned libraries like pandas (Python) and Daru(Ruby) are allowed. ------
# Measuring running Times: Implement functions or methods to measure the total runtime as your script runs. All scripts will be run and measured in Odin.
# Interfaces: A textual menu should be implemented in a way that the user could load several samples of the same data set (all data cleaning steps would be the same). 
# During the demo you will be ask to load several data sets with the same structure.

# Data Loading: Read data from the csv files
print("Loading and cleaning input data set:")
print("************************************")
# https://towardsdatascience.com/python-pandas-data-frame-basics-b5cfbcd8c039
# !!!REMOVE PERIOD IN FRONT OF FILE NAME ONCE DONE WITH PROJECT!!!
file = '.US_Accidents_data.csv'         # Has a TOTAL of 711336 written lines
# Load CSV file and store its data into a dataframe
print(time.process_time(), " Starting Script")
df = pd.read_csv(file, sep=',')
#print(df)
print(time.process_time(), " Loading US_Accidents_data.csv")
# Data Cleaning: Perform the following cleaning tasks: First load the csv file and store into an array or data frame
    # 1. Eliminate all rows with data missing in either of the following columns: ID, Severity, Zipcode, Start_Time, End_Time, Visibility(mi), Weather_Condition or Country
df.drop(df[(df['ID'].isnull()) | (df['Severity'].isnull()) | (df['Zipcode'].isnull()) | (df['Start_Time'].isnull()) | (df['End_Time'].isnull()) | 
    (df['Visibility(mi)'].isnull()) | (df['Weather_Condition'].isnull()) | (df['Country'].isnull())].index, inplace=True)
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
#df.drop(df[df['End_Time'] > df['Start_Time']].index, inplace=True)
print(time.process_time(), " Performing Data Clean Up")
print(time.process_time(), " Printing row count after data cleaning is finished: ", len(df.index))

def getMonth(month):
    theMonths = ["January","February","March","April", "May", "June", "July", "August", "September",
     "October", "November","December"]
    monthName = theMonths[month-1]
    return monthName
# Output: Your job is to implement the any functions and methods to answer the following questions about the data set provided:
# For all these question use Start_Time as the reference date to determine the year and month of the accident.
    # 1. In what month were there more accidents reported?
newMonth = pd.to_datetime(df.Start_Time).dt.strftime('%m')
n = 1
finalMonth = int((newMonth.value_counts()[:n].index.tolist())[0])
print(time.process_time()," 1. The month with the most accidents reported is:", getMonth(finalMonth))
    # 2. What is the state that had the most accidents in 2020
dfCopy = df.copy()
dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time']).dt.strftime('%Y')
accidentsByYrInSt = dfCopy[['Start_Time','State']]
mostByStInYr = accidentsByYrInSt[accidentsByYrInSt['Start_Time'] == '2020'].value_counts().index[0]
state = mostByStInYr[1]
print(time.process_time()," 2. The state with the most accidents reported in 2020 is:", state)
    # 3. What is the state that had the most accidents of severity 2 in 2021?
accidentsByYr_SvtyInST = dfCopy[['Start_Time','State','Severity']]
mostByYr_SvtyInST = accidentsByYr_SvtyInST[(accidentsByYr_SvtyInST['Start_Time'] == '2021') & (accidentsByYr_SvtyInST['Severity'] == 2)].value_counts().index[0]
state = mostByYr_SvtyInST[1]
print(time.process_time()," 3. The state with the most accidents of severity 2 in 2021 is:", state)
    # 4. What severity is the most common in Virginia?
accidentsBySvtyInST = dfCopy[['State','Severity']]
mostBySvtyInST = accidentsBySvtyInST[(accidentsBySvtyInST['State'] == 'VA')].value_counts().index[0]
severity = mostBySvtyInST[1]
print(time.process_time()," 4.",severity, "severity is the most common in VA.")
    # 5. What are the 5 cities that had the most accidents in 2019 in California?
accidentsByYr_St_Cty = dfCopy[['Start_Time','State','City']]
mostByYr_St_Cty = accidentsByYr_St_Cty[(accidentsByYr_St_Cty['State'] == 'CA') & (accidentsByYr_St_Cty['Start_Time'] == '2019')].value_counts().index[0:5]
cities = mostByYr_St_Cty.get_level_values('City')
print(time.process_time()," 5. The 5 cities that had the most accidents in 2019 in CA are:")
for i in cities:
    print("\t\t\t\t\t\t\t\t",i)
    # 6. What was the average humidity and average temperature of all accidents of severity 4 that occurred in 2021?
accidentsByHumid_Temp_Sev_Yr = dfCopy[['Start_Time','Severity','Humidity(%)','Temperature(F)']]
accidentsByHumid_Temp_Sev_Yr = accidentsByHumid_Temp_Sev_Yr[(accidentsByHumid_Temp_Sev_Yr['Start_Time'] == '2021') & (accidentsByHumid_Temp_Sev_Yr['Severity'] == 4)]
averageHumidity = accidentsByHumid_Temp_Sev_Yr['Humidity(%)'].mean()
averageTemperature = accidentsByHumid_Temp_Sev_Yr['Temperature(F)'].mean()
print(time.process_time()," 6. The average humidity is:", averageHumidity,"% and the average temperature is:", averageTemperature, "F of all accidents of severity 4 that occurred in 2021.")
    # 7. What are the 3 most common weather conditions (weather_conditions) when accidents occurred?
accidentsByWeather = dfCopy[['Weather_Condition']]
mostByWeather= accidentsByWeather.value_counts().index[0:3]
weathers = mostByWeather.get_level_values('Weather_Condition')
print(time.process_time()," 7. The 3 most common weather conditions when accidents occurred are:")
for i in weathers:
    print("\t\t\t\t\t\t\t\t", i)
    # 8. What was the maximum visibility of all accidents of severity 2 that occurred in the state of New Hampshire?
accidentsByVisibility_Sev_State = dfCopy[['Visibility(mi)', 'Severity', 'State']]
accidentsByVisibility_Sev_State = accidentsByVisibility_Sev_State[(accidentsByVisibility_Sev_State['State'] == 'NH') & (accidentsByVisibility_Sev_State['Severity'] == 4)]
maxVisibility = accidentsByVisibility_Sev_State['Visibility(mi)'].max()
print(time.process_time()," 8. The maximum visibility of all accidents of severity 2 that occurred in the state of New Hampshire is:", maxVisibility,"mi")
    # 9. How many accidents of each severity were recorded in Bakersfield?
accidentsBySvtyInST = dfCopy[['City','Severity']]
totalBySvtyInST = accidentsBySvtyInST.loc[(accidentsBySvtyInST['City'] == 'Bakersfield'), 'Severity'].value_counts()
print(time.process_time()," 9. The total accidents of each severity recorded in Bakersfield are:")
s = 0
for i in totalBySvtyInST:
    print("\t\t\t\t\t\t\t\t\tSeverity", totalBySvtyInST.index[s],":", i)
    s = s + 1
    # 10. What was the longest accident (in hours) recorded in Florida in the Spring (March, April, and May) of 2022?
dfCopy = df.copy()
dfCopy['Start_Time'] = pd.to_datetime(dfCopy['Start_Time'])
dfCopy['End_Time'] = pd.to_datetime(dfCopy['End_Time'])
accidentsByTime_ST = dfCopy[['Start_Time','End_Time','State']]
betweenMonths = accidentsByTime_ST['Start_Time'].dt.month.between(3,5)
betweenMonths = accidentsByTime_ST[betweenMonths]
accidentsByTime_ST_Month = betweenMonths[(betweenMonths['State'] == 'FL') & (pd.to_datetime(betweenMonths['Start_Time']).dt.year  == 2022)]
totalTimeOfAccident = accidentsByTime_ST_Month['End_Time'] - accidentsByTime_ST_Month['Start_Time']
longestAccident = totalTimeOfAccident.max()
longestAccidentInSecs = (longestAccident.days*86400) + (longestAccident.seconds)
print(time.process_time()," 10. The longest accident (in hours) recorded in Flordia in the Spring of 2022 is:", longestAccidentInSecs/(3600), "hours.")