# def calculate_mean(weather_data):

#     # weather_data = [10, '20', '30.5', 'invalid', 40, '50.0', 'text']

#     """Calculates the mean value from a list of numbers. 
#     Mean - The average value
#     Median - The mid point value
#     Mode - The most common value

#     Args:
#         weather_data: a list of numbers.
#     Returns:
#         A float representing the mean value.
#     """
#     # Check if the list is empty
#     if not weather_data:
#         raise ValueError("The list of weather data cannot be empty.")
    
#     # Convert valid elements to floats and ignore invalid ones. To add any item to which can be converted to numberical data for the underneath calc.
#     numeric_data = []
#     for item in weather_data:
#         try:
#             numeric_data.append(float(item))
#         except ValueError:
#             # Skip items that cannot be converted to float
#             continue

#     if not numeric_data:
#         raise ValueError("No valid numeric data found in the list.")
    
    
#     # Calculate the sum of all numbers in the list
#     total_sum = sum(weather_data)
    
#     # Calculate the number of elements in the list
#     count = len(weather_data)
    
#     # Compute the mean value
#     mean_value = total_sum / count
    
#     return mean_value

# weather_data = [10, '20', '30.5', 'invalid', 40, '50.0', 'text']

# # Print the type of each item in weather_data
# print("Types of items in weather_data:")

# #This loop prints each item in the list along with its type. This helps to understand what types of data are present in the dataset.
# for item in weather_data:
#     print(f"Item: {item}, Type: {type(item)}")

# # Call the calculate_mean function with the example data and print the mean value. If an error occurs, it’s caught and printed.
# try:
#     mean_value = calculate_mean(weather_data)
#     print(f"Mean value: {mean_value}")
# except ValueError as e:
#     print(f"Error: {e}")


# def find_min(weather_data):
#     """Calculates the minimum value in a list of numbers.

#     Args:
#         weather_data: A list of numbers.
#     Returns:
#         The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
#     """
    
#     # Check if the list is empty
#     if not weather_data:
#         raise ValueError("The list of weather data cannot be empty.")
    
#     # Initialize variables to store the minimum value and its position
#     min_value = float('inf')
#     min_index = -1
    
#     # Iterate over the list to find the minimum value and its last occurrence
#     for index, value in enumerate(weather_data):
#         if value < min_value:
#             min_value = value
#             min_index = index
#         elif value == min_value:
#             min_index = index
    
#     return min_value, min_index

# weather_data = [34, 12, 78, 12, 56, 12]

# # Call the find_min function
# min_value, min_index = find_min(weather_data)

# # Print the results
# print(f"The minimum value is {min_value}.")
# print(f"The index of the last occurrence of the minimum value is {min_index}.")

# def convert_f_to_c(temp_in_fahrenheit):
#     """Converts a temperature from Fahrenheit to Celcius.

#     Args:
#         temp_in_fahrenheit: float representing a temperature.
#     Returns:
#         A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
#     """
#     return round((float(temp_in_fahrenheit)- 32) * 5 / 9 ,1)
# print(convert_f_to_c("77"))

from weather import convert_date
from weather import convert_f_to_c
from weather import find_max
from weather import find_min
from weather import format_temperature, calculate_mean



# def generate_daily_summary(weather_data):
#     """Outputs a daily summary for the given weather data.

#     Args:
#         weather_data: A list of lists, where each sublist represents a day of weather data.
#     Returns:
#         A string containing the summary information.
#     """

#     summary_lines = []
    
#     for entry in weather_data:
#         date = convert_date(entry[0])  # Convert the date to a readable format
#         temperatures = entry[1:]

#         if not temperatures:
#             continue

#         # Convert temperatures from Fahrenheit to Celsius if needed
#         temperatures_in_celsius = [convert_f_to_c(temp) for temp in temperatures]

#         # Call Min and Max functions. however, the function would contains temperatures and index

#         min_temp_tuple = find_min(temperatures_in_celsius)
#         max_temp_tuple = find_max(temperatures_in_celsius)

#         # Exclude the index part from tuple
#         min_temp = min_temp_tuple [0]
#         max_temp = max_temp_tuple [0]

#         # Add formatted output to the summary list
#         summary_lines.append(
#             f"---- {date} ----\n  Minimum Temperature: {format_temperature(min_temp)}\n  Maximum Temperature: {format_temperature(max_temp)}"
#         )
#         print(summary_lines)
    
#     # Join all daily summaries with exactly one newline between each day
#     return "\n\n".join(summary_lines)

# checkdailysum = generate_daily_summary(""2021-07-02T07:00:00+08:00", 49, 67")
# print (checkdailysum)



def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary_lines = []
    all_temperatures_in_celsius = []

    min_temp_overall = float('inf')
    max_temp_overall = float('-inf')
    min_temp_date = ""
    max_temp_date = ""

    # Determine the number of days
    num_days = len(weather_data)
    
    for data in weather_data:
        date = convert_date(data[0])
        temperatures = data[1:]

        if not temperatures:
            continue

        # Convert temperatures from Fahrenheit to Celsius if needed
        temperatures_in_celsius = [convert_f_to_c(temp) for temp in temperatures]
        all_temperatures_in_celsius.extend(temperatures_in_celsius)

        # Find the minimum and maximum temperatures for the day
        min_temp, _ = find_min(temperatures_in_celsius)
        max_temp, _ = find_max(temperatures_in_celsius)

        # Update overall min and max temperatures
        if min_temp < min_temp_overall:
            min_temp_overall = min_temp
            min_temp_date = date

        if max_temp > max_temp_overall:
            max_temp_overall = max_temp
            max_temp_date = date

    # Calculate the mean temperatures across the entire data set
    mean_low_temp = calculate_mean([convert_f_to_c(temp) for temp in find_min(all_temperatures_in_celsius)[1]])
    mean_high_temp = calculate_mean([convert_f_to_c(temp) for temp in find_max(all_temperatures_in_celsius)[1]])

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

    return "\n".join(summary_lines)

example_data = [
    ["2021-07-02T07:00:00+08:00", 49, 67],
    ["2021-07-03T07:00:00+08:00", 57, 68],
    ["2021-07-04T07:00:00+08:00", 56, 62],
    ["2021-07-05T07:00:00+08:00", 55, 61],
    ["2021-07-06T07:00:00+08:00", 53, 62]
]

result = generate_summary(example_data)
print(result)

