# CLASS Project
# RUBY IMPLEMENTATION: BASIC DATA ANALYSIS
# COURSE: CMPS 3500
# DATE: 04/06/22
# Student 1: Elena Castaneda
# Student 2: Marcus Schmidt
# Student 3: 
# Student 4:
# DESCRIPTION: Implementation Basic Data Analysys Routines

# ------ All functions must be implemented by the team, predesigned libraries like pandas (Python) and Daru(Ruby) are allowed. ------
# Measuring running Times: Implement functions or methods to measure the total runtime as your script runs. All scripts will be run and measured in Odin.
# Interfaces: A textual menu should be implemented in a way that the user could load several samples of the same data set (all data cleaning steps would be the same). 
# During the demo you will be ask to load several data sets with the same structure.
require "daru"

# References
# https://ankane.org/daru
# https://www.rubydoc.info/gems/daru/Daru/DataFrame
# https://nbviewer.org/github/SciRuby/sciruby-notebooks/blob/master/Data%20Analysis/Usage%20of%20DataFrame.ipynb

# Data Loading: Read data from the csv file
print("Loading and cleaning input data set:\n")
print("************************************\n")
file = "US_Accidents_data.csv"
df = Daru::DataFrame.from_csv(file)

=begin
# Print all of the data frame's column names
df.vectors.each.with_index do |element, index|
    puts("#{index}: #{element}")
end
=end

puts("Size: #{df.size}")

def nilColumns (row)
    empty_columns = 0
    row.each do |element|
        if element == nil
            empty_columns += 1
        end
    end
    empty_columns
end

# Eliminate invalid rows
df.keep_row_if do |row|
    row["ID"] != nil && row["Severity"] != nil && row["Zipcode"] != nil && row["Start_Time"] != nil && row["End_Time"] != nil &&
    row["Distance(mi)"] != 0 &&
    row["Start_Time"] != row["End_Time"] &&
    nilColumns(row) < 3
end

# Clean ZIP codes
(0..df.size-1).each do |index|
    row = df.row[index]
    zip = row["Zipcode"].to_s
    if zip.length > 5
        row["Zipcode"] = zip[0, 5]
    end
end

puts("Size: #{df.size}")

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