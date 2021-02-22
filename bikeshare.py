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
    while True:
      city = input("\nWould you like to see data for Chicago, New York City, or Washington?\n")
      city = city.lower()
      if city not in ('new york city', 'chicago', 'washington'):
        print("Please choose Chicago, New York City, or Washington ")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("\nWould you like to filter by month? Choose January, February, March, April, May, June or type 'all'\n") 
      month = month.lower()
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("Please choose January, February, March, April, May, June or type 'all'.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("\nWould you like to filter by day of week? Choose Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all'.\n")
      day = day.lower()
      if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        print("Please choose Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' ")
        continue
      else:
        break

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
    common_month = df['month'].mode()[0]
    print('The most common month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['start end station'] = df['Start Station'] + ' and ' + df['End Station'] 
    common_start_end_station = df['start end station'].mode()[0]
    print('Most frequent combination of start station and end station trip :', common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time in seconds : ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean of travel time in seconds : ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('Calculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    n_user_types = df['User Type'].value_counts()
    
    print('Counts of user types:\n', n_user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        n_gender = df['Gender'].value_counts()
        print('Counts of gender:\n', n_gender)
    else:
        print('There is no information for gender')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode())
        print('The earliest year of birth: ', earliest_year)
        print('The most recent year of birth: ', most_recent_year)
        print('The most common year of birth: ', most_common_year)
    else:
        print('There is no information for year of birth')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    index=0
    user_input=input('would you like to display five rows of raw data? Please type Yes or No.\n').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display five more rows of raw data? Please type Yes or No.\n').lower()
        
def main():
    while True:
      city, month, day = get_filters()
      df = load_data(city, month, day)

      time_stats(df)
      station_stats(df)
      trip_duration_stats(df)
      user_stats(df)
      display_data(df)
    
      restart = input('\nWould you like to restart? Enter yes or no.\n')
      if restart.lower() != 'yes':
          break


if __name__ == "__main__":
	main()

