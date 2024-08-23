import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"
    # return f"{temp:.1f}°C"



def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    #formatted iso_string into a datetime object
    iso_date = datetime.fromisoformat(iso_string)

    #cover the date to readable format
    readable_date = iso_date.strftime('%A %d %B %Y')

    return readable_date

#test with example variable

# print(f"{convert_date('2021-07-06T07:00:00+08:00')}", {type(convert_date)})



def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    return round((float(temp_in_fahrenheit)- 32) * 5 / 9 ,1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers. 
    Mean - The average value
    Median - The mid point value
    Mode - The most common value

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # Check if the list is empty
    if not weather_data:
        raise ValueError("The list of weather data cannot be empty.")
    
    # Convert valid elements to floats and ignore invalid ones. To add any item to which can be converted to numberical data for the underneath calc.
    numeric_data = []

    for value in weather_data:
        try:
            float_value = float(value)
            numeric_data.append(float_value)

        except ValueError:
            # Skip items that cannot be converted to float
            continue

    if not numeric_data:
        raise ValueError("No valid numeric data found in the list.")
    
    
    # Calculate the sum of all numbers in the list
    total_sum = sum(numeric_data)
    
    # Calculate the number of elements in the list
    count = len(numeric_data)
    
    # Compute the mean value
    mean_value = total_sum / count
    
    return mean_value


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    import csv

    # list = []

    # with open(csv_file) as file:
    #     csv_reader = csv.reader(file)
    #     next(csv_reader)       

    #     for row in csv_reader:
    #         if not row:
    #             return ()
            
    #         elif row != "":
    #             int_row = int()
    #             list.append(int_row)

    # return list

    list_of_lists = []

    try:
        with open(csv_file, newline='') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row

            for row in csv_reader:
                if row:  # Check if the row is not empty
                    # Convert the first element to a string (date), and the rest to integers
                    date = row[0]  # Date remains a string
                    # Convert temperature values to integers
                    temp_values = []
                    for value in row[1:]:
                        try:
                            temp_values.append(int(value))
                        except ValueError:
                            print(f"Warning: '{value}' could not be converted to integer and will be skipped.")
                    
                    list_of_lists.append([date] + temp_values)

    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return list_of_lists




def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    
    # Check if the list is empty
    if not weather_data:
        return ()  # Return an empty tuple for an empty list
    
    # Initialize variables to store the minimum value and its position. In Python, float('inf') is a special value that is larger than any finite number
    min_value = float('inf')
    min_index = -1
    
    # Iterate over the list to find the minimum value and its last occurrence
    for index, value in enumerate(weather_data):

        try:
            # Convert value to float to handle numbers and numeric strings
            float_value = float(value)
        except ValueError:
            # Skip non-numeric values
            continue


        if float_value < min_value:
            min_value = float_value
            min_index = index

        elif float_value == min_value:
            min_index = index
        
        if min_index == -1:
            raise ValueError("No valid numeric data found in the list.")
        
        # print(f"Value: {value}, Float Value: {float_value}, Min Value: {min_value}, Min Index: {min_index}")
    
    return min_value, min_index



def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    
    if not weather_data:
        return ()  # Return an empty tuple for an empty list
    
    max_value = float('-inf')  # Initialize max_value to negative infinity
    max_index = -1  # Initialize max_index to -1 to indicate no valid index found yet
    
    for index, value in enumerate(weather_data):
        try:
            # Convert the value to a float if possible
            float_value = float(value)
        except ValueError:
            # If conversion fails, skip this value
            continue

        # Update max_value and max_index if a new maximum is found
        if float_value > max_value:
            max_value = float_value
            max_index = index
        elif float_value == max_value:
            # Update to the last occurrence of the maximum value
            max_index = index
    
    if max_index == -1:
        raise ValueError("No valid numeric data found in the list.")
    
    return max_value, max_index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary_lines = []

    # Lists to hold all low and high temperatures in Celsius
    low_temperatures_in_celsius = []
    high_temperatures_in_celsius = []

    min_temp_overall = float('inf')
    max_temp_overall = float('-inf')
    min_temp_date = ""
    max_temp_date = ""

    # Determine the number of days
    num_days = len(weather_data)
    
    for data in weather_data:
        date = convert_date(data[0])
        low_temp_f = data[1]
        high_temp_f = data[2]

        # Convert temperatures from Fahrenheit to Celsius
        low_temp_c = convert_f_to_c(low_temp_f)
        high_temp_c = convert_f_to_c(high_temp_f)


        # Add to respective lists
        low_temperatures_in_celsius.append(low_temp_c)
        high_temperatures_in_celsius.append(high_temp_c)


        # # Find the minimum and maximum temperatures for the day
        # min_temp_tuple = find_min(low_temperatures_in_celsius)
        # max_temp_tuple = find_max(high_temperatures_in_celsius)

        # # Exclude the index part from tuple
        # min_temp = min_temp_tuple [0]
        # max_temp = max_temp_tuple [0]

        # # Update overall min and max temperatures
        # if min_temp < min_temp_overall:
        #     min_temp_overall = min_temp

        # Update overall min and max temperatures
        if low_temp_c < min_temp_overall:
            min_temp_overall = low_temp_c

            min_temp_date = date

        # if max_temp > max_temp_overall:
        #     max_temp_overall = max_temp

        if high_temp_c > max_temp_overall:
            max_temp_overall = high_temp_c
            max_temp_date = date

    # Calculate the average temperatures
    
    mean_low_temp = round(calculate_mean(low_temperatures_in_celsius),1)
    mean_high_temp = round(calculate_mean(high_temperatures_in_celsius),1)


    # Format the output
    summary_lines.append(
        f"{num_days} Day Overview"
    )
    summary_lines.append(
        f"  The lowest temperature will be {format_temperature(min_temp_overall)}, and will occur on {min_temp_date}."
    )
    summary_lines.append(
        f"  The highest temperature will be {format_temperature(max_temp_overall)}, and will occur on {max_temp_date}."
    )
    summary_lines.append(
        f"  The average low this week is {format_temperature(mean_low_temp)}."
    )
    summary_lines.append(
        f"  The average high this week is {format_temperature(mean_high_temp)}."
    )

    return "\n".join(summary_lines) + "\n"

    


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    summary_lines = []
    
    for entry in weather_data:
        date = convert_date(entry[0])  # Convert the date to a readable format
        min_temp_f = entry[1]
        max_temp_f = entry[2]

        #Convert temperatures from Fahrenheit to Celsius if needed
        min_temp = convert_f_to_c(min_temp_f)
        max_temp = convert_f_to_c(max_temp_f)

        # temperatures_in_celsius = [convert_f_to_c(temp) for temp in temperatures]

        # # Call Min and Max functions. however, the function would contains temperatures and index

        # min_temp_tuple = find_min(temperatures_in_celsius)
        # max_temp_tuple = find_max(temperatures_in_celsius)

        # # Exclude the index part from tuple
        # min_temp = min_temp_tuple [0]
        # max_temp = max_temp_tuple [0]

        # Add formatted output to the summary list

        summary_lines.append(
            f"---- {date} ----"
        )
        summary_lines.append(
            f"  Minimum Temperature: {format_temperature(min_temp)}"
        )
        summary_lines.append(
            f"  Maximum Temperature: {format_temperature(max_temp)}\n"
        )
    
    # Join all daily summaries with exactly one newline between each day
    return "\n".join(summary_lines) + "\n"

