# CLASS Project
# RUBY IMPLEMENTATION: BASIC DATA ANALYSIS
# COURSE: CMPS 3500
# DATE: 04/06/22
# Student 1: Elena Castaneda
# Student 2: 
# Student 3: 
# Student 4:
# DESCRIPTION: Implementation Basic Data Analysys Routines

# ------ All functions must be implemented by the team, predesigned libraries like pandas (Python) and Daru(Ruby) are allowed. ------
# Measuring running Times: Implement functions or methods to measure the total runtime as your script runs. All scripts will be run and measured in Odin.
# Interfaces: A textual menu should be implemented in a way that the user could load several samples of the same data set (all data cleaning steps would be the same). 
# During the demo you will be ask to load several data sets with the same structure.

# Data Loading: Read data from the csv files
# Note - Input list will have up to 18 columns and one million rows and could be unordered and contain 
# repeated, missing, incorrect and or misleading values.

# !!!! We can try https://ankane.org/daru

# Data Cleaning: Perform the following cleaning tasks: First load the csv file and store into an array or data frame
    # 1. Eliminate all rows with data missing in either of the following columns: ID, Severity, zipcpde, Start_Time, End_Time, Visivility(m), Weather_Condition or Country
    # 2. Eliminate all rows with empty values in 3 or more columns
    # 3. Eliminate all rows with distance equal to zero
    # 4. Only consider in your analysis the first 5 digits of the zip code
    # 5. All accicent that lasted no time (The diference between End_time and Start_time is zero)

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