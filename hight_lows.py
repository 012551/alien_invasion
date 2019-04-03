import csv

filname = 'sitka_weather_07-2014.csv'
with open(filname) as f:
    reder = csv.reader(f)
    header_row = next(reder)

    hights = []
    for row in reder:
        hights.append(1)
    print(hights)
    # for index, colunm_head in enumerate(header_row):
    #     print(index, colunm_head)
