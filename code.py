import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
test_data = pd.read_csv("HW4_Test_Data.csv")
size = len(test_data)
random_data = np.random.rand(size, 3)
time_splited_data = pd.DataFrame(random_data, columns=[ 'day_of_week', 'hour_of_day',"normalized_energy"])
for i in range(len(test_data)):
    temp = test_data.loc[i]
    date_string = temp["TestTime"]
    date_obj = datetime.datetime.strptime(date_string, '%m/%d/%y %H:%M')
    day_of_week = date_obj.weekday()
    hour_of_day = date_obj.hour
    value = test_data.loc[i,"TestBldg"]
    time_splited_data.loc[index] = [day_of_week,hour_of_day, value ]