import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': "C:/Users/Trojan/Downloads/submit-ee3820b0-b0c4-424d-ad19-f580012800db/home/chicago.csv",
              'new york city': "C:/Users/Trojan/Downloads/submit-ee3820b0-b0c4-424d-ad19-f580012800db/home/new_york_city.csv",
              'washington': "C:/Users/Trojan/Downloads/submit-ee3820b0-b0c4-424d-ad19-f580012800db/home/washington.csv" }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city=input("Enter Name of city => ")
    while city not in  CITY_DATA:
        city=input("city should be chicago, new york city or washington => ").lower()



    # TO DO: get user input for month (all, january, february, ... , june)

    month = input("Enter month => ").lower()
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month = input("month should be january, february, ... , june => ").lower()





    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input("Enter day => ").lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input("day should be monday, tuesday, ... sunday => ").lower()

    print('-'*40)
    return city, month, day





def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('the most common month:', popular_month,'\n')

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('the most common day of week:', popular_day,'\n')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('the most common start hour:', popular_hour,'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    used_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', used_start_station)

    # TO DO: display most commonly used end station
    used_end_station =  df['End Station'].mode()[0]
    print('Most commonly used end station:', used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination_start_and_end_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('Most commonly combination of start station and end station trip: ', frequent_combination_start_and_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is : {}".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time is : {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The counts of user type : {} ".format(user_types))

    # TO DO: Display counts of gender
    if 'Gender' not in df.columns :
        print("no gender here \n")
    else:
        gender = df['Gender'].value_counts()
        print("The counts of user type : {} ".format(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print("no birth year here \n")
    else:
        earliest = df['Birth Year'].min()
        print("The earliest year : {} ".format(earliest))
        most_recent = df['Birth Year'].max()
        print("The most recent year : {} ".format(most_recent))
        most_common = df['Birth Year'].mode()[0]
        print("The most common year : {} ".format(most_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        start_loc = 0
        view_data = input("\nWould you like to view 5 rows of individual trip data? Enter yes or no\n")
        while view_data == 'yes':
            start_loc+=5
            print(df.head(start_loc))
            view_data = input("Do you wish to continue?: ").lower()

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
