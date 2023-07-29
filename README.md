# Basic Data Exploration with pandas on Bikeshare Data
A Python project using pandas to explore bikeshare data.

## Project Overview
This project focuses on using the pandas library and basic statistical techniques to do descriptive analysis on the bikeshare data from Chicago, Washington, and New York City, three major U.S. cities, in order to display data such as the most popular days or stations.

## Running the program
You can input 'python bikeshare.py' on your terminal to run this program.

## Program Details
The programme asks the user to enter the city (for example, Chicago), the month (for example, January; there is also a 'all' option), and the day (for example, Monday; there is also a 'all' option) for which they want to view the data.

Following user input, it prompts the user to choose whether or not to examine the raw data (5 rows of data initially). The following information is printed by the programme after the input is received:

- Most popular month
- Most popular day
- Most popular hour
- Most popular start station
- Most popular end station
- Most popular combination of start and end stations
- Total trip duration
- Average trip duration
- Types of users by number
- Types of users by gender (if available)
- The oldest user (if available)
- The youngest user (if available)
- The most common birth year amongst users (if available)
- Finally, the user is prompted with the choice of restarting the program or not.

## Requirements
- Language: Python 
- Libraries: pandas, numpy, time

## Project Dataset
From [GitHub](https://github.com/Aritra96/bikeshare-project/tree/master/data).
- Chicago.csv - Stored in the data folder, the chicago.csv file is the dataset containing all bikeshare information for the city of Chicago provided by Udacity.

- New_york_city.csv - Dataset containing all bikeshare information for the city of New York provided by Udacity.

- Washington.csv - Dataset containing all bikeshare information for the city of Washington provided by Udacity. Note: This does not include the 'Gender' or 'Birth Year' data.
