import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_data = {'all', 'january', 'february', 'march', 'april', 'may', 'june'}
day_data = {'all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday'}


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
    city = input("Please enter a city name: ")
    while city not in CITY_DATA:
        city = input("Oh sorry, Please choose from these three cities (chicago, new york city, washington): ")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please select a month or choose all for all months: ")
    while month not in month_data:
        month = input("Sorry, Please select a month between january and june or choose all for all months:" )


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter a day or choose all for all days: ")
    while day not in day_data:
        day = input("Sorry, Please choose a day of the week or choose all for all months:" )
    


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
     
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1


        df = df[df['month'] == month]


    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("the recurring month is:", common_month)


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("the weekday most frequently used is:", common_day)


    # TO DO: display the most common start hour
    start_hour = df['hour'].mode()[0]
    print("the most frequently start time is:", start_hour) 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("The most popular starting point is: ", start_station)


    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("The most frequently end station: ", end_station)


    # TO DO: display most frequent combination of start station and end station trip
    group_station = df.groupby(['Start Station','End Station'])
    start_end_station =  group_station.size().sort_values(ascending=False).head(1)
    print("The most common route between a start station and an end station: ", start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = str(df['Trip Duration'].sum())
    print("The total travel time is: ", total_duration)


    # TO DO: display mean travel time
    mean_duration = str(df['Trip Duration'].mean())
    print("The mean travel time is: ", mean_duration)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

  # Display counts of user types
    print('The user type is:')
    print(df['User Type'].value_counts())
    if city != 'washington':
        # Display counts of gender
        print('The user gender is:')
        print(df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
    earlist_date = df['Birth Year'].min()
    newest_date = df['Birth Year'].max()
    common_date = df['Birth Year'].mode()[0]
    print('Earliest birth records are: {}\n'.format(earlist_date))
    print('Newest birth records are: {}\n'.format(newest_date))
    print('Most common birth data are: {}\n'.format(common_date))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
