DATA_FILE = 'weather.csv'

# This is a tedious process
# with open(DATA_FILE) as file:
#     data = file.readlines()
# weather_list = [line.strip() for line in data]
# print(weather_list)

# Use this instead:
import csv

# Here, extracting temperatures does NOT work so we need pandas!
# with open(DATA_FILE) as file:
#     data = csv.reader(file)
#     temps = []
#     for row in data:
#         temps.append(int(row[1]))
#     print(temps)

import pandas

data = pandas.read_csv(DATA_FILE)
temps = data['temp']
# temps = data.temps
temps_list = temps.to_list()
print(f'Average temperature (long method!!) = {sum(temps_list) / len(temps_list)}')
print(f'Average temperature (direct method) = {data["temp"].mean()}')
print(f'Max temperature recorded was: {data["temp"].max()}')
# print(type(data))
# <class 'pandas.core.frame.DataFrame'>
# print(type(temps))
# <class 'pandas.core.series.Series'>

# To get the row where day = monday
print(data[data.day == 'Monday'])

# print(type(data[data.day == 'Monday']))
# <class 'pandas.core.frame.DataFrame'>

# To get row with max temp:
print(data[data.temp == data.temp.max()])

# Create Data Frame from scratch
data_dict = {
    'students': ['sam', 'raj', 'sheldon'],
    'scores': [70, 80, 100]
}
print(pandas.DataFrame(data_dict))
pandas.DataFrame(data_dict).to_csv('my_new_file.csv')
