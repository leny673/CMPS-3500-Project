# CLASS Project
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# COURSE: CMPS 3500
# DATE: 04/06/22
# Student 1: Elena Castaneda
# Student 2: 
# Student 3: 
# Student 4:
# DESCRIPTION: Implementation Basic Data Analysys Routines
import time
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
# Output: Your job is to implement the any functions and methods to answer the following questions about the data set provided:
# For all these question use Start_Time as the reference date to determine the year and month of the accident.
    # 1. In what month were there more accidents reported?
    # 2. What is the state that had the most accidents in 2020?
    # 3. What is the state that had the most accidents of severity 2 in 2021?
    # 4. What severity is the most common in Virginia?
    # 5. What are the 5 cities that had the most accidents in 2019 in California?
    # 6. What was the average humidity and average temperature of all accidents of severity 4 that occurred in 2021?
    # 7. What are the 3 most common weather conditions (weather_conditions) when accidents occurred?
    # 8. What was the maximum visibility of all accidents of severity 2 that occurred in the state of New Hampshire?
    # 9. How many accidents of each severity were recorded in Bakersfield?
    # 10. What was the longest accident (in hours) recorded in Florida in the Spring (March, April, and May) of 2022?