import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
new_data = []
for fur_color in data['Primary Fur Color'].dropna().unique():
    total = len(data[data['Primary Fur Color'] == fur_color])
    row = [fur_color, total]
    new_data.append(row)
pandas.DataFrame(new_data).to_csv('my_csv.csv')
