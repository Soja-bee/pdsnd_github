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
    print('Would you like to see data for Chicago, New York City or Washington')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    str.lower()
    city_name  ['chicago', 'new york city','washington']
    while (city not in city_names):
        print('\nWrong city? please enter Chicago, New York City or Washington.\n')
    while city != 'all':
        city =['chicago', 'new york city', 'washington']

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    print('Would you like to filter the data by month, day or both')
    # TO DO: get user input for month (all, january, february, ... , june)
  if month != 'all':
     df['month'] =  pd.to_datetime(df['month'], format='%m').dt.month_name()
     df = df[df['month']
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
  if day != 'all':
     df = df[df['day_of_week']

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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]

    # TO DO: display the most common day of week

    most_common_day_of_week = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['Start - End Station'] = df['Start Station'] + df['End Station']
    df['Start - End Station'].mode()[0]
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Trip Duration'].sum()

    # TO DO: display mean travel time
    df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

if city = 'washington':
   user_stats(df) == False
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    gender_types = df['Gender'].value_counts()

    # TO DO: Display earliest, most recent, and most common year of birth
    df['Birth Year'].max()
    df['Birth Year'].min()
    df['Birth Year'].value_counts()
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

     while True:
            view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n')
         if view_data.lower() = 'yes':
            yes_count = 0
            start_index = 0
            end_index = 5
            print(df.iloc[start_index : end_index])
            yes_count +=1
            start_index +=5
            end_index +=5
         else:
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
