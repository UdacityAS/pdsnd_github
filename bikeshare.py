from __future__ import division
import time
import pandas as pd
import numpy as np



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city_name = ['chicago', 'new york city', 'washington']
    
  
    
    while True:
            city = input('Enter the city name ').lower()
            if city in city_name:
                print (city)
                break
            else: 
                print ('No info: try another name')
    

    # TO DO: get user input for month (all, january, february, ... , june)
    #Adding extra comment for git
    month_name = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
          
    while True:
            month = input('Enter the month ').lower()
            if month in month_name:
                print (month)
                break
            else: 
                print ('No info: try another name')         

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #Added second comment for phase 4
    day_name = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    while True:
            day = input('Enter the day ').lower()
            if day in day_name:
                print (day)
                break
            else: 
                print ('No info: try another name')  

    print('-'*40)
    return city, month, day

Initial commit
#def print_five_rows_at_a_time(df):
    #i=0
    #while True:
        #print(df.iloc[i+0:i+5])
        #five_more_rows = input("Would you like to see 5 more rows of data? Enter yes or no\n")
        #i=i+5
        #if five_more_rows.lower() != 'yes':
            #break      
    

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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['Month'] = df['Start Time'].dt.month
    
    df['Weekday'] = df['Start Time'].dt.weekday
    
    #while not asked in this section, bringing in the hour due to calculations needed below
    df['Start hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]
        
    if day != 'all':   
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        df = df[df['Weekday'] == day]
        
    return df    
        
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['Month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = months[most_common_month-1] 
    print("the most common month is", most_common_month)

    # TO DO: display the most common day of week
    most_common_weekday = df['Weekday'].mode()[0]
    weekdays = ['sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    most_common_weekday = weekdays[most_common_weekday-1] 
    print("the most common weekday is", most_common_weekday)

    # TO DO: display the most common start hour
    most_common_start_hour = df['Start hour'].mode()
    print("the most common start hour is", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("the most common start station is", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("the most common end station is", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination_start_to_end_station'] = df['Start Station'] + df['End Station']
    print("the most common combination of start station to end station is",                df['combination_start_to_end_station'].value_counts()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_summary_seconds = df['Trip Duration'].sum()
    
    trip_summary_hours = (trip_summary_seconds/60/60)
    
    print('Total trip duration is', trip_summary_hours, 'hours.\n\n')
    

    # TO DO: display mean travel time
    trip_mean_seconds = df['Trip Duration'].mean()
         
    trip_mean_minutes = (trip_mean_seconds/60)
    
    print('Mean travel time is', trip_mean_minutes, 'minutes.\n\n')
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print("Counts by user type are",user_counts)

    # TO DO: Display counts of gender
    gender_counts = df['Gender'].value_counts()
    print("Counts of each gender are",gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth_year = int(df['Birth Year'].min())
    print("Earliest birth year is", earliest_birth_year)
    
    most_recent_birth_year = int(df['Birth Year'].max())
    print("The most recent birth year is",most_recent_birth_year)
    
    most_common_birth_year = int(df['Birth Year'].mode())
    print("The most common birth year is",most_common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        rows = input('Do you want to see five rows? Enter yes or no\n')
        if rows.lower() == 'yes': 
           print_five_rows_at_a_time(df)     

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
